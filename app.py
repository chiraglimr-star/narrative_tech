from pathlib import Path
import zipfile, textwrap, os, py_compile, json

root = Path("/mnt/data/ontological_silence_v3")
root.mkdir(parents=True, exist_ok=True)

app_code = r'''"""
Ontological Silence & Paranoia Engine — V3
Context-aware research prototype for dialogue analysis.

Important:
- Sentence embeddings provide semantic similarity to operational descriptions.
- Similarity scores are NOT calibrated probabilities.
- The engine does not infer real psychological states, intentions, diagnoses, or truth.
- Always inspect context and validate against independently annotated data.
"""
from __future__ import annotations

import hashlib
import json
import re
import datetime as dt
from collections import Counter, defaultdict
from typing import Any

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import cohen_kappa_score, precision_recall_fscore_support

APP_VERSION = "3.0.0"

CATEGORY_DESCRIPTIONS = {
    "Silence / Void": (
        "The speaker explicitly remains silent, refuses to speak, withholds a verbal answer, "
        "or describes absence, muteness, a pause, or an empty communicative space."
    ),
    "Aggression": (
        "The speaker uses hostile, threatening, coercive, insulting, or explicitly violent language "
        "directed at someone or something."
    ),
    "Emotional Withdrawal": (
        "The speaker expresses emotional distancing, retreat, reluctance to engage, loneliness, "
        "fear, sadness, vulnerability, or a wish to disengage."
    ),
    "Defensive Rationalization": (
        "The speaker justifies, excuses, deflects responsibility, denies agency, explains away an action, "
        "or resists an accusation."
    ),
    "Direct Inquiry": (
        "The speaker requests information, asks a question, seeks clarification, challenges a claim, "
        "or explicitly investigates something."
    ),
    "Surveillance / Control": (
        "The speaker describes watching, monitoring, tracking, inspecting, controlling, or being observed."
    ),
    "Lack / Desire": (
        "The speaker expresses wanting, needing, longing, incompleteness, absence, loss, or an unmet desire."
    ),
    "Bad Faith Indicators": (
        "The speaker appears in the wording to deny choice, hide behind duty, evade responsibility, "
        "or present a chosen action as unavoidable. This is only a textual indicator, not a philosophical diagnosis."
    ),
    "Dynamic Interaction": (
        "The utterance mainly performs an ordinary conversational move or does not strongly match another category."
    ),
}

# Lexical patterns are retained as transparent evidence alongside semantic matching.
LEXICON = {
    "Silence / Void": {
        "silence", "silent", "quiet", "hush", "mute", "speechless", "wordless",
        "nothing", "empty", "void", "absence", "hollow", "soundless"
    },
    "Aggression": {
        "attack", "kill", "destroy", "threat", "force", "obey", "punish",
        "fight", "hate", "angry", "furious", "violent", "brutal", "cruel",
        "murder", "weapon", "enemy", "war", "strike", "revenge", "idiot",
        "stupid", "hurt", "harm"
    },
    "Emotional Withdrawal": {
        "sad", "cry", "tears", "pain", "fear", "afraid", "scared", "anxious",
        "broken", "lonely", "regret", "sorry", "goodbye", "leave", "miserable",
        "unhappy", "sorrow", "grief", "miss", "longing", "fragile", "helpless",
        "vulnerable", "tired", "exhausted", "heartbroken", "wounded"
    },
    "Defensive Rationalization": {
        "truth", "reason", "logic", "because", "explain", "justify", "rationalize",
        "deny", "avoid", "deflect", "distract", "escape", "pretend", "excuse",
        "defend", "responsibility", "forced", "cannot", "impossible"
    },
    "Direct Inquiry": {
        "what", "where", "when", "who", "whom", "whose", "which", "why", "how",
        "ask", "question", "inquire", "wonder", "investigate", "examine", "doubt"
    },
    "Surveillance / Control": {
        "watch", "watched", "watching", "observe", "observed", "monitor",
        "monitoring", "control", "surveillance", "record", "recording", "follow",
        "followed", "authority", "power", "discipline", "prison", "camera",
        "guard", "inspect", "track"
    },
    "Lack / Desire": {
        "empty", "nothing", "absence", "missing", "desire", "want", "need",
        "lost", "void", "alone", "lack", "incomplete", "unfulfilled", "longing"
    },
    "Bad Faith Indicators": {
        "pretend", "deny", "excuse", "justify", "rationalize", "avoid",
        "responsibility", "truth", "choice", "freedom", "cannot", "impossible",
        "forced", "duty", "must"
    },
}

PHRASES = {
    "Silence / Void": ["say nothing", "not a word", "fell silent", "kept quiet", "refused to speak"],
    "Emotional Withdrawal": ["leave me alone", "stay away", "i feel alone", "i don't want to talk"],
    "Defensive Rationalization": ["that is not my fault", "that's not my fault", "i had no choice", "you misunderstood"],
    "Surveillance / Control": ["i am watching you", "i'm watching you", "you are being watched", "under observation"],
    "Bad Faith Indicators": ["i had no choice", "i couldn't do otherwise", "that is just how things are"],
}

NEGATORS = {
    "not", "no", "never", "neither", "nor", "hardly", "barely", "without",
    "isn't", "aren't", "wasn't", "weren't", "don't", "doesn't", "didn't",
    "can't", "cannot", "couldn't", "won't", "wouldn't", "shouldn't"
}
STOP_WORDS = {
    "the","and","for","but","with","from","this","that","was","were","are","has","have",
    "had","there","here","they","them","she","him","her","its","you","your","his","our",
    "their","then","than","into","about","just","very","been","being","will","would",
    "could","should","does","did","a","an","to","of","in","on","it","i","we","he","as","at","by","or"
}

def tokenize(text: str) -> list[str]:
    return re.findall(r"[^\W_]+(?:['’][^\W_]+)?", str(text).lower(), flags=re.UNICODE)

def parse_corpus(text: str) -> list[dict]:
    """Parse Speaker: text lines; preserve unlabelled lines as Actor N."""
    beats = []
    for line_no, raw in enumerate(str(text).splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        match = re.match(r"^([^:]{1,60}):\s*(.*)$", line)
        if match:
            speaker, utterance = match.group(1).strip(), match.group(2).strip()
        else:
            speaker, utterance = f"Actor {line_no}", line.lstrip("-— ").strip()
        utterance = utterance.lstrip("-— ").strip()
        if utterance:
            beats.append({
                "beat": len(beats) + 1, "source_line": line_no,
                "speaker": speaker, "text": utterance
            })
    return beats

def lexical_evidence(text: str) -> dict:
    tokens = tokenize(text)
    positives, negated = defaultdict(list), defaultdict(list)
    # Approximate negation scope: intentionally labelled as approximate.
    for i, token in enumerate(tokens):
        for category, vocab in LEXICON.items():
            if token in vocab:
                left = tokens[max(0, i - 3):i]
                if any(x in NEGATORS for x in left):
                    negated[category].append(token)
                else:
                    positives[category].append(token)
    lowered = str(text).lower()
    for category, phrases in PHRASES.items():
        for phrase in phrases:
            if phrase in lowered:
                positives[category].append(phrase)
    if "?" in str(text):
        positives["Direct Inquiry"].append("question mark")
    if re.search(r"[\[(]\s*(silence|pause|long pause|beat)\s*[\])]", lowered):
        positives["Silence / Void"].append("explicit stage direction")
    return {
        c: {"positive": sorted(set(positives.get(c, []))),
            "negated": sorted(set(negated.get(c, [])))}
        for c in CATEGORY_DESCRIPTIONS
    }

class SemanticEngine:
    """
    Sentence-embedding similarity against written category descriptions.
    Similarity is a ranking signal, not a probability or a validated classifier.
    """
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.model = None
        self.error = None
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(model_name)
            self.description_embeddings = self.model.encode(
                list(CATEGORY_DESCRIPTIONS.values()),
                normalize_embeddings=True
            )
        except Exception as exc:
            self.error = f"{type(exc).__name__}: {exc}"
            self.model = None
            self.description_embeddings = None

    def score(self, text: str) -> dict[str, float]:
        if self.model is None or not str(text).strip():
            return {}
        emb = self.model.encode([text], normalize_embeddings=True)
        sims = cosine_similarity(emb, self.description_embeddings)[0]
        return {name: float(score) for name, score in zip(CATEGORY_DESCRIPTIONS, sims)}

def context_for_turn(beats: list[dict], index: int, history_size: int = 4) -> dict:
    current = beats[index]
    previous = beats[max(0, index-history_size):index]
    same_speaker = [b for b in previous if b["speaker"] == current["speaker"]]
    context = " ".join(b["text"] for b in previous)
    speaker_history = " ".join(b["text"] for b in same_speaker[-3:])
    return {
        "previous_turns": previous,
        "context_text": context,
        "speaker_history": speaker_history,
        "speaker": current["speaker"],
        "current_text": current["text"]
    }

def tfidf_similarity(a: str, b: str) -> float | None:
    if not a.strip() or not b.strip():
        return None
    try:
        vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)
        matrix = vec.fit_transform([a, b])
        return float(cosine_similarity(matrix[0], matrix[1])[0, 0])
    except ValueError:
        return 0.0

def analyze_turn(beats: list[dict], index: int, engine: SemanticEngine | None,
                 threshold: float = 0.34, margin: float = 0.025,
                 history_size: int = 4) -> dict:
    beat = beats[index]
    ctx = context_for_turn(beats, index, history_size)
    lexical = lexical_evidence(beat["text"])
    # Context is bounded and transparent. The current utterance is not replaced by history.
    enriched = (
        f"Current utterance: {beat['text']}. "
        f"Recent dialogue: {ctx['context_text'][-1200:]}. "
        f"Previous utterances by this speaker: {ctx['speaker_history'][-700:]}."
    )
    semantic = engine.score(enriched) if engine and engine.model else {}
    ranked = sorted(semantic.items(), key=lambda x: x[1], reverse=True)
    if ranked:
        top_score = ranked[0][1]
        second_score = ranked[1][1] if len(ranked) > 1 else -1.0
        gap = top_score - second_score
        selected = [
            name for name, score in ranked
            if score >= threshold and (top_score - score) <= max(margin, 0.12)
        ]
        if not selected:
            selected = ["Dynamic Interaction"]
        status = "Ambiguous" if gap < margin else "Semantic candidate"
    else:
        top_score, gap, selected, status = None, None, [], "Semantic model unavailable"

    lexical_labels = [name for name, ev in lexical.items() if ev["positive"]]
    combined = list(dict.fromkeys(lexical_labels + selected))
    if not combined:
        combined = ["Dynamic Interaction"]
    # Don't present semantic score as confidence.
    return {
        **beat,
        "context_text": ctx["context_text"],
        "speaker_history": ctx["speaker_history"],
        "lexical_evidence": lexical,
        "lexical_labels": lexical_labels,
        "semantic_scores": semantic,
        "semantic_labels": selected,
        "combined_labels": combined,
        "top_similarity": top_score,
        "top_margin": gap,
        "semantic_status": status,
        "word_count": len(tokenize(beat["text"])),
        "is_question": "?" in beat["text"],
        "stage_silence": any("explicit stage direction" in ev["positive"] for ev in lexical.values()),
        "interpretation_warning": (
            "Semantic similarity is not a calibrated probability. "
            "Context window is limited; irony, metaphor, sarcasm and pragmatics may be misread."
        )
    }

def analyze_corpus(corpus: str, engine: SemanticEngine | None = None,
                   threshold: float = 0.34, margin: float = 0.025,
                   history_size: int = 4) -> list[dict]:
    beats = parse_corpus(corpus)
    results = [
        analyze_turn(beats, i, engine, threshold, margin, history_size)
        for i in range(len(beats))
    ]
    # Within-speaker word-count changes are descriptive only.
    prev_words = {}
    for row in results:
        old = prev_words.get(row["speaker"])
        row["previous_same_speaker_words"] = old
        row["within_speaker_word_change"] = (
            (row["word_count"] - old) if old is not None else None
        )
        prev_words[row["speaker"]] = row["word_count"]
    return results

def corpus_metrics(results: list[dict]) -> dict:
    if not results:
        return {}
    tokens = [t for r in results for t in tokenize(r["text"])]
    return {
        "turns": len(results),
        "speakers": len(set(r["speaker"] for r in results)),
        "words": len(tokens),
        "average_turn_length": round(float(np.mean([r["word_count"] for r in results])), 2),
        "questions": sum(r["is_question"] for r in results),
        "lexical_diversity": round(len(set(tokens))/len(tokens), 3) if tokens else 0,
        "label_counts": dict(Counter(x for r in results for x in r["combined_labels"]))
    }

def participation_table(results: list[dict]) -> pd.DataFrame:
    stats = defaultdict(lambda: {"turns": 0, "words": 0, "questions": 0})
    for r in results:
        s = stats[r["speaker"]]
        s["turns"] += 1
        s["words"] += r["word_count"]
        s["questions"] += int(r["is_question"])
    total_turns = max(1, len(results))
    total_words = max(1, sum(r["word_count"] for r in results))
    rows = [{
        "Speaker": name, "Turns": x["turns"], "Words": x["words"],
        "Turn share (%)": round(100*x["turns"]/total_turns, 1),
        "Word share (%)": round(100*x["words"]/total_words, 1),
        "Questions": x["questions"]
    } for name, x in stats.items()]
    return pd.DataFrame(rows).sort_values("Turn share (%)", ascending=False)

def question_audit(beats: list[dict], lookahead: int = 3) -> list[dict]:
    rows = []
    for i, beat in enumerate(beats):
        if "?" not in beat["text"]:
            continue
        candidate = next(
            (beats[j] for j in range(i+1, min(len(beats), i+1+lookahead))
             if beats[j]["speaker"] != beat["speaker"]), None
        )
        sim = tfidf_similarity(beat["text"], candidate["text"]) if candidate else None
        rows.append({
            "Beat": beat["beat"], "Question speaker": beat["speaker"],
            "Question": beat["text"],
            "Candidate speaker": candidate["speaker"] if candidate else None,
            "Candidate response": candidate["text"] if candidate else None,
            "TF-IDF overlap (not answer score)": round(sim, 3) if sim is not None else None,
            "Review": "Human review required; response relation is not automatically established."
        })
    return rows

def turning_point_candidates(results: list[dict]) -> list[dict]:
    if len(results) < 3:
        return []
    lengths = np.array([r["word_count"] for r in results], dtype=float)
    median = float(np.median(lengths))
    mad = float(np.median(np.abs(lengths-median)))
    rows = []
    for i, r in enumerate(results):
        rz = 0.6745*(r["word_count"]-median)/mad if mad else 0.0
        flags = []
        if abs(rz) >= 2.5: flags.append("Turn length outlier")
        if r["stage_silence"]: flags.append("Explicit pause/silence direction")
        if r["is_question"]: flags.append("Question form")
        if len(r["combined_labels"]) >= 3: flags.append("Multiple candidate labels")
        if flags:
            rows.append({
                "Beat": r["beat"], "Speaker": r["speaker"], "Text": r["text"],
                "Word count": r["word_count"], "Robust length deviation": round(float(rz), 2),
                "Observable flags": "; ".join(flags),
                "Interpretation": "Descriptive candidate only; not a validated turning-point prediction."
            })
    return rows

def validation_metrics(df: pd.DataFrame, gold_col: str, pred_col: str) -> dict | None:
    clean = df[[gold_col, pred_col]].dropna()
    if clean.empty:
        return None
    y_true, y_pred = clean[gold_col].astype(str), clean[pred_col].astype(str)
    labels = sorted(set(y_true) | set(y_pred))
    p, r, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, average="macro", zero_division=0
    )
    kappa = cohen_kappa_score(y_true, y_pred) if len(set(y_true) | set(y_pred)) > 1 else np.nan
    return {
        "n": len(clean), "accuracy": float(np.mean(y_true == y_pred)),
        "macro_precision": float(p), "macro_recall": float(r),
        "macro_f1": float(f1), "cohen_kappa": float(kappa) if not np.isnan(kappa) else None,
        "labels": labels
    }

def corpus_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

@st.cache_resource(show_spinner=False)
def load_semantic_engine(model_name: str):
    return SemanticEngine(model_name)

def show_turns(results: list[dict]):
    for r in results:
        with st.expander(f"Beat {r['beat']} · {r['speaker']} · {', '.join(r['combined_labels'])}"):
            st.write(f"**Utterance:** {r['text']}")
            c1, c2, c3 = st.columns(3)
            c1.metric("Words", r["word_count"])
            c2.metric("Semantic top similarity", f"{r['top_similarity']:.3f}" if r["top_similarity"] is not None else "N/A")
            c3.metric("Semantic status", r["semantic_status"])
            st.write("**Semantic candidate labels:**", ", ".join(r["semantic_labels"]) or "Unavailable")
            st.write("**Lexical labels:**", ", ".join(r["lexical_labels"]) or "No positive lexical markers")
            evidence = {
                k: v for k, v in r["lexical_evidence"].items()
                if v["positive"] or v["negated"]
            }
            st.json(evidence)
            if r["context_text"]:
                st.write("**Recent dialogue context:**", r["context_text"])
            st.caption(r["interpretation_warning"])

st.set_page_config(
    page_title="Ontological Silence Engine V3",
    page_icon="👁️",
    layout="wide"
)
st.markdown("""
<style>
.stApp {background:#090c12;color:#e6edf3}
[data-testid="stSidebar"] {background:#111722}
h1,h2,h3 {font-family: 'Courier New', monospace}
div[data-testid="stMetricValue"] {color:#58a6ff}
</style>
""", unsafe_allow_html=True)

st.title("👁️ Ontological Silence & Paranoia Engine")
st.caption("V3 · Context-aware semantic research prototype · Computational Dramaturgy")
st.warning(
    "Research limitation: semantic similarity is not human-level understanding, calibrated confidence, "
    "or evidence of psychological intent. All interpretations require human review."
)

with st.sidebar:
    st.header("Research controls")
    module = st.radio("Module", [
        "Research framework", "Contextual scene analyzer",
        "Participation analysis", "Question-response audit",
        "Turning-point candidates", "Validation workspace", "Export & reproducibility"
    ])
    st.divider()
    use_semantic = st.checkbox("Enable sentence-embedding model", value=True)
    model_name = st.text_input(
        "Embedding model",
        value="sentence-transformers/all-MiniLM-L6-v2",
        help="First run downloads the model. Requires internet access; afterward it may run locally."
    )
    threshold = st.slider("Semantic similarity threshold", 0.10, 0.80, 0.34, 0.01)
    history_size = st.slider("Previous turns in context", 0, 8, 4)
    st.caption(f"Version {APP_VERSION} · {dt.date.today().isoformat()}")

@st.cache_resource(show_spinner=False)
def get_engine(name):
    return SemanticEngine(name)

engine = None
if use_semantic:
    with st.spinner("Loading contextual sentence-embedding model..."):
        engine = get_engine(model_name)
    if engine.model is None:
        st.error(
            "Semantic model could not be loaded. Check internet access, model availability, "
            "and installed dependencies. The lexical baseline remains available."
        )
        with st.expander("Technical loading error"):
            st.code(engine.error or "Unknown error")

if module == "Research framework":
    st.header("Research framework")
    st.markdown("""
**Research question:** Can transparent lexical indicators and contextual semantic representations
help researchers identify observable patterns associated with silence, conversational avoidance,
withdrawal, control language, and changes in dramatic interaction?

**V3 architecture**
1. **Lexical evidence:** visible words, phrases, approximate negation scope.
2. **Context window:** preceding turns and recent utterances by the same speaker.
3. **Semantic representation:** sentence embeddings compared with explicit operational descriptions.
4. **Decision layer:** semantic candidates + lexical evidence + ambiguity status.
5. **Human validation:** independent labels, held-out evaluation, error analysis.

The model does not literally understand all language. Embedding similarity can miss irony, metaphor,
sarcasm, cultural references, pragmatic intent, and long-range narrative dependencies.
""")
    st.subheader("Research principles")
    st.write("- Do not interpret a similarity score as a probability.")
    st.write("- Do not diagnose characters or infer real mental states.")
    st.write("- Keep lexical evidence and semantic suggestions separate.")
    st.write("- Record model name, threshold, context window, corpus hash, and software version.")
    st.write("- Evaluate on human-labelled data before making performance claims.")

elif module == "Contextual scene analyzer":
    st.header("Contextual scene analyzer")
    corpus = st.text_area(
        "Paste dialogue (format: Speaker: sentence)",
        height=260,
        placeholder="Mia: Why did you leave?\nJohn: I had to.\nMia: That is not an answer."
    )
    if st.button("Analyze dialogue", type="primary"):
        if not corpus.strip():
            st.warning("Please enter dialogue.")
        else:
            results = analyze_corpus(
                corpus, engine, threshold=threshold, history_size=history_size
            )
            st.session_state["results"] = results
            st.session_state["corpus"] = corpus
            metrics = corpus_metrics(results)
            a,b,c,d = st.columns(4)
            a.metric("Turns", metrics["turns"])
            b.metric("Speakers", metrics["speakers"])
            c.metric("Words", metrics["words"])
            d.metric("Questions", metrics["questions"])
            st.subheader("Turn-by-turn analysis")
            show_turns(results)
            st.subheader("Candidate label frequency")
            counts = pd.Series(metrics["label_counts"], dtype=int)
            if not counts.empty:
                st.bar_chart(counts)
            st.caption(f"Corpus SHA-256: {corpus_hash(corpus)}")

elif module == "Participation analysis":
    st.header("Character participation analysis")
    corpus = st.text_area("Dialogue corpus", height=240, key="participation_text")
    if st.button("Calculate participation"):
        results = analyze_corpus(corpus, engine, threshold, history_size=history_size)
        if not results:
            st.warning("No dialogue found.")
        else:
            df = participation_table(results)
            st.dataframe(df, use_container_width=True)
            st.bar_chart(df.set_index("Speaker")[["Turn share (%)", "Word share (%)"]])
            st.info("Participation volume is not social dominance, authority, or psychological power.")

elif module == "Question-response audit":
    st.header("Question-response audit")
    corpus = st.text_area("Dialogue corpus", height=240, key="qa_text")
    lookahead = st.slider("Maximum turns to inspect", 1, 8, 3)
    if st.button("Audit questions"):
        audit = question_audit(parse_corpus(corpus), lookahead)
        if audit:
            st.dataframe(pd.DataFrame(audit), use_container_width=True)
        else:
            st.info("No question marks found.")
        st.caption("A candidate response is not necessarily an answer. Human pragmatic review is required.")

elif module == "Turning-point candidates":
    st.header("Turning-point candidates")
    corpus = st.text_area("Dialogue corpus", height=240, key="turning_text")
    if st.button("Find observable changes"):
        results = analyze_corpus(corpus, engine, threshold, history_size=history_size)
        if len(results) < 3:
            st.warning("At least three turns are recommended.")
        else:
            st.line_chart(pd.DataFrame(
                {"Word count": [r["word_count"] for r in results]},
                index=[f"Beat {r['beat']}" for r in results]
            ))
            candidates = turning_point_candidates(results)
            if candidates:
                st.dataframe(pd.DataFrame(candidates), use_container_width=True)
            else:
                st.info("No candidates flagged by the current descriptive rules.")

elif module == "Validation workspace":
    st.header("Validation workspace")
    st.write(
        "Upload a CSV with columns `gold_label` and `predicted_label`. "
        "Use the same held-out items for all compared systems. Do not tune on the test set."
    )
    uploaded = st.file_uploader("Upload annotation/evaluation CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        required = {"gold_label", "predicted_label"}
        if not required.issubset(df.columns):
            st.error("CSV must contain gold_label and predicted_label columns.")
        else:
            metrics = validation_metrics(df, "gold_label", "predicted_label")
            if metrics:
                c1,c2,c3,c4 = st.columns(4)
                c1.metric("N", metrics["n"])
                c2.metric("Accuracy", f"{metrics['accuracy']:.3f}")
                c3.metric("Macro-F1", f"{metrics['macro_f1']:.3f}")
                c4.metric("Cohen's κ", f"{metrics['cohen_kappa']:.3f}" if metrics["cohen_kappa"] is not None else "N/A")
                st.write("**Per-class report**")
                from sklearn.metrics import classification_report, confusion_matrix
                st.text(classification_report(
                    df["gold_label"].astype(str), df["predicted_label"].astype(str),
                    zero_division=0
                ))
                labels = metrics["labels"]
                cm = confusion_matrix(df["gold_label"].astype(str), df["predicted_label"].astype(str), labels=labels)
                st.dataframe(pd.DataFrame(cm, index=labels, columns=labels))
            else:
                st.warning("No complete annotation rows found.")

elif module == "Export & reproducibility":
    st.header("Export & reproducibility")
    results = st.session_state.get("results")
    corpus = st.session_state.get("corpus", "")
    if not results:
        st.info("Run the contextual scene analyzer first.")
    else:
        model_used = model_name if engine and engine.model else "lexical-only fallback"
        metadata = {
            "app_version": APP_VERSION,
            "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "corpus_sha256": corpus_hash(corpus),
            "embedding_model": model_used,
            "semantic_threshold": threshold,
            "context_history_turns": history_size,
            "note": "Similarity values are not calibrated probabilities."
        }
        export = {"metadata": metadata, "results": results}
        st.json(metadata)
        st.download_button(
            "Download analysis JSON",
            data=json.dumps(export, ensure_ascii=False, indent=2),
            file_name="ontological_silence_analysis.json",
            mime="application/json"
        )
        flat = []
        for r in results:
            flat.append({
                "beat": r["beat"], "speaker": r["speaker"], "text": r["text"],
                "lexical_labels": "; ".join(r["lexical_labels"]),
                "semantic_labels": "; ".join(r["semantic_labels"]),
                "combined_labels": "; ".join(r["combined_labels"]),
                "top_similarity": r["top_similarity"],
                "semantic_status": r["semantic_status"]
            })
        st.download_button(
            "Download turn-level CSV",
            data=pd.DataFrame(flat).to_csv(index=False).encode("utf-8-sig"),
            file_name="ontological_silence_turns.csv",
            mime="text/csv"
        )
'''

requirements = """streamlit>=1.35
pandas>=2.0
numpy>=1.24
scikit-learn>=1.3
sentence-transformers>=3.0
torch>=2.0
"""

tests = r'''import unittest
from app import tokenize, parse_corpus, lexical_evidence, analyze_corpus, corpus_metrics, question_audit

class EngineTests(unittest.TestCase):
    def test_tokenize_contractions(self):
        self.assertIn("don't", tokenize("I don't know."))

    def test_parse_dialogue(self):
        beats = parse_corpus("Mia: Are you there?\nJohn: Yes.")
        self.assertEqual(len(beats), 2)
        self.assertEqual(beats[0]["speaker"], "Mia")

    def test_negated_marker_separated(self):
        evidence = lexical_evidence("I am not afraid.")
        self.assertIn("afraid", evidence["Emotional Withdrawal"]["negated"])
        self.assertNotIn("afraid", evidence["Emotional Withdrawal"]["positive"])

    def test_metaphor_not_claimed_as_understood(self):
        # The lexical baseline can flag 'killed'; semantic disambiguation needs model + evaluation.
        evidence = lexical_evidence("I killed the presentation.")
        self.assertIn("kill", evidence["Aggression"]["positive"])

    def test_empty_corpus(self):
        self.assertEqual(analyze_corpus(""), [])

    def test_metrics(self):
        results = analyze_corpus("Mia: Hello.\nJohn: Hello.")
        self.assertEqual(corpus_metrics(results)["turns"], 2)

    def test_question_audit(self):
        rows = question_audit(parse_corpus("Mia: Why?\nJohn: Because I left."), 2)
        self.assertEqual(len(rows), 1)

if __name__ == "__main__":
    unittest.main()
'''

readme = r'''# Ontological Silence & Paranoia Engine — V3

A research prototype for computational dialogue and narrative analysis.

## What V3 adds
- Sentence-embedding semantic similarity to explicit category descriptions.
- Limited dialogue context: preceding turns and recent turns by the same speaker.
- Separate lexical evidence and semantic candidate labels.
- Ambiguity status and transparent model settings.
- Participation metrics, question-response candidates, turning-point candidates.
- CSV/JSON exports with corpus hash, model name, threshold, and version.
- Evaluation workspace for held-out human-labelled data.

## Install
Python 3.10+ recommended.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

The first semantic-model run downloads `sentence-transformers/all-MiniLM-L6-v2`.
It requires internet access and several hundred MB of model/runtime downloads.
If the model cannot load, the app still provides lexical analysis, but semantic
candidate labels will be unavailable.

## Methodological warning
Sentence embeddings compare the utterance-plus-context representation with
operational category descriptions. The returned cosine similarities are ranking
signals, **not probabilities** and not evidence that the system understands
speaker intent. Context is limited to a configurable number of preceding turns.
Metaphor, irony, sarcasm, cultural references, pragmatics, and long-range narrative
structure can still be misinterpreted.

The lexical evidence layer is intentionally transparent and approximate.
Negation scope is a simple local window, not full syntactic negation resolution.
The combined label list is a research aid, not a validated classifier.

## Evaluation protocol
1. Define inclusion/exclusion criteria for the corpus.
2. Write category definitions and annotation examples.
3. Have at least two annotators label a sample independently.
4. Split data into development and held-out test sets before tuning.
5. Report per-class precision, recall, F1, confusion matrix, and inter-annotator agreement.
6. Compare lexical baseline, embedding model, supervised contextual model, and human annotators.
7. Perform error analysis for metaphor, negation, irony, polysemy, and speaker/context effects.

Do not use the test set for threshold tuning. Do not describe the engine as a
psychological detector, a mind reader, or a validated evasion detector.

## Tests
```bash
python -m unittest -v
```
'''

(root/"app.py").write_text(app_code, encoding="utf-8")
(root/"requirements.txt").write_text(requirements, encoding="utf-8")
(root/"test_core.py").write_text(tests, encoding="utf-8")
(root/"README.md").write_text(readme, encoding="utf-8")

# Syntax-check and run unit tests without importing Streamlit app's UI execution.
# Compile catches syntax errors; full test execution needs installed dependencies.
try:
    py_compile.compile(str(root/"app.py"), doraise=True)
    syntax_status = "passed"
except Exception as e:
    syntax_status = f"failed: {e}"

zip_path = Path("/mnt/data/ontological_silence_v3.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for p in root.iterdir():
        z.write(p, arcname=f"ontological_silence_v3/{p.name}")

print("Created:", zip_path)
print("Files:", [p.name for p in root.iterdir()])
print("Python syntax check:", syntax_status)
