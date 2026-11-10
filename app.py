"""
Ontological Silence & Paranoia Engine — V3
Context-aware research prototype.
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

app_code = r'''"""
Ontological Silence & Paranoia Engine — V4
Streamlit Cloud-compatible contextual dialogue research prototype.

This is an exploratory research aid, not a validated psychological detector.
Sentence-transformer cosine similarities are ranking signals, NOT probabilities.
"""
from __future__ import annotations

import hashlib
import json
import re
import datetime as dt
from collections import Counter, defaultdict
from typing import Optional

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    precision_recall_fscore_support, cohen_kappa_score
)
from sklearn.preprocessing import MultiLabelBinarizer

APP_VERSION = "4.0.0"
DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

CATEGORY_DESCRIPTIONS = {
    "Silence / Void": (
        "An utterance explicitly describes silence, not speaking, refusing to answer, "
        "withholding speech, muteness, a pause, or an absence in communication."
    ),
    "Aggression": (
        "An utterance expresses hostility, a threat, coercion, insult, intimidation, "
        "or an explicit intention to physically or verbally harm someone."
    ),
    "Emotional Withdrawal": (
        "An utterance expresses emotional distance, disengagement, loneliness, fear, "
        "sadness, vulnerability, reluctance to communicate, or a wish to withdraw."
    ),
    "Defensive Rationalization": (
        "An utterance justifies or excuses an action, denies responsibility, deflects blame, "
        "rejects an accusation, or explains why the speaker acted as they did."
    ),
    "Direct Inquiry": (
        "An utterance asks a question, requests information, seeks clarification, "
        "challenges a claim, or investigates an issue."
    ),
    "Surveillance / Control": (
        "An utterance describes observing, monitoring, tracking, inspecting, controlling, "
        "restricting, or being watched by another person or institution."
    ),
    "Lack / Desire": (
        "An utterance expresses wanting, needing, longing, loss, absence, incompleteness, "
        "or an unmet desire."
    ),
    "Bad Faith Indicators": (
        "An utterance linguistically presents a choice as unavoidable, hides behind duty, "
        "denies agency, or avoids responsibility. This is a textual indicator only."
    ),
    "Dynamic Interaction": (
        "An ordinary conversational utterance that does not clearly fit the other categories."
    ),
}

LEXICON = {
    "Silence / Void": {
        "silence", "silent", "quiet", "hush", "mute", "speechless", "wordless",
        "soundless", "muteness"
    },
    "Aggression": {
        "attack", "kill", "destroy", "threat", "force", "obey", "punish", "fight",
        "hate", "furious", "violent", "brutal", "cruel", "murder", "weapon",
        "enemy", "revenge", "idiot", "stupid", "hurt", "harm", "strike"
    },
    "Emotional Withdrawal": {
        "sad", "cry", "tears", "pain", "fear", "afraid", "scared", "anxious",
        "broken", "lonely", "regret", "sorry", "goodbye", "leave", "miserable",
        "grief", "miss", "longing", "fragile", "helpless", "vulnerable", "tired",
        "exhausted", "heartbroken", "wounded"
    },
    "Defensive Rationalization": {
        "because", "explain", "justify", "rationalize", "deny", "deflect",
        "pretend", "excuse", "defend", "responsibility", "forced", "impossible"
    },
    "Direct Inquiry": {
        "what", "where", "when", "who", "whom", "whose", "which", "why", "how",
        "ask", "question", "inquire", "wonder", "investigate", "examine", "doubt"
    },
    "Surveillance / Control": {
        "watch", "watched", "watching", "observe", "observed", "monitor",
        "monitoring", "control", "surveillance", "record", "recording", "follow",
        "followed", "authority", "discipline", "prison", "camera", "guard",
        "inspect", "track"
    },
    "Lack / Desire": {
        "missing", "desire", "want", "need", "lost", "lack", "incomplete",
        "unfulfilled", "longing", "absence", "empty", "void"
    },
    "Bad Faith Indicators": {
        "pretend", "deny", "excuse", "justify", "rationalize", "responsibility",
        "choice", "freedom", "forced", "duty", "must", "unavoidable"
    },
}

PHRASES = {
    "Silence / Void": [
        "say nothing", "not a word", "fell silent", "kept quiet",
        "refused to speak", "would not answer"
    ],
    "Emotional Withdrawal": [
        "leave me alone", "stay away", "i feel alone", "i don't want to talk",
        "i do not want to talk", "need some space"
    ],
    "Defensive Rationalization": [
        "that is not my fault", "that's not my fault", "i had no choice",
        "you misunderstood", "it was not my decision"
    ],
    "Surveillance / Control": [
        "i am watching you", "i'm watching you", "you are being watched",
        "under observation"
    ],
    "Bad Faith Indicators": [
        "i had no choice", "i couldn't do otherwise", "i could not do otherwise",
        "that is just how things are"
    ],
}

NEGATORS = {
    "not", "no", "never", "neither", "nor", "hardly", "barely", "without",
    "isn't", "aren't", "wasn't", "weren't", "don't", "doesn't", "didn't",
    "can't", "cannot", "couldn't", "won't", "wouldn't", "shouldn't"
}

def tokenize(text: str) -> list[str]:
    return re.findall(r"[^\W_]+(?:['’][^\W_]+)?", str(text).lower(), flags=re.UNICODE)

def parse_corpus(text: str) -> list[dict]:
    """Parse 'Speaker: utterance'; unlabelled lines receive Actor N."""
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
                "beat": len(beats) + 1,
                "source_line": line_no,
                "speaker": speaker,
                "text": utterance
            })
    return beats

def _is_negated(tokens: list[str], index: int, window: int = 3) -> bool:
    """Approximate local negation scope; not a syntactic parser."""
    left = tokens[max(0, index-window):index]
    return any(token in NEGATORS for token in left)

def lexical_evidence(text: str) -> dict:
    tokens = tokenize(text)
    positives = defaultdict(list)
    negated = defaultdict(list)

    for i, token in enumerate(tokens):
        for category, vocabulary in LEXICON.items():
            if token in vocabulary:
                target = negated if _is_negated(tokens, i) else positives
                target[category].append(token)

    lowered = str(text).lower()
    # Phrase matching is also checked for local negation, so "I did not refuse to speak"
    # is not automatically treated as a positive silence marker.
    for category, phrases in PHRASES.items():
        for phrase in phrases:
            start = lowered.find(phrase)
            if start >= 0:
                preceding = tokenize(lowered[:start])
                target = negated if any(t in NEGATORS for t in preceding[-3:]) else positives
                target[category].append(phrase)

    if "?" in str(text):
        positives["Direct Inquiry"].append("question mark")

    if re.search(r"[\[(]\s*(silence|pause|long pause|beat)\s*[\])]", lowered):
        positives["Silence / Void"].append("explicit stage direction")

    return {
        category: {
            "positive": sorted(set(positives.get(category, []))),
            "negated": sorted(set(negated.get(category, [])))
        }
        for category in CATEGORY_DESCRIPTIONS
    }

def tfidf_similarity(a: str, b: str) -> Optional[float]:
    if not a.strip() or not b.strip():
        return None
    try:
        vectorizer = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)
        matrix = vectorizer.fit_transform([a, b])
        return float(cosine_similarity(matrix[0], matrix[1])[0, 0])
    except ValueError:
        return 0.0

def build_context(beats: list[dict], index: int, history_size: int) -> dict:
    current = beats[index]
    previous = beats[max(0, index-history_size):index]
    same_speaker = [b for b in previous if b["speaker"] == current["speaker"]]
    return {
        "previous_turns": previous,
        "context_text": " ".join(b["text"] for b in previous),
        "speaker_history": " ".join(b["text"] for b in same_speaker[-3:])
    }

class SemanticEngine:
    """Sentence-embedding category matcher; outputs similarities, not probabilities."""
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.model = None
        self.description_embeddings = None
        self.error = None
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(model_name)
            descriptions = list(CATEGORY_DESCRIPTIONS.values())
            self.description_embeddings = self.model.encode(
                descriptions, normalize_embeddings=True, convert_to_numpy=True
            )
        except Exception as exc:
            self.error = f"{type(exc).__name__}: {exc}"

    def score(self, text: str) -> dict[str, float]:
        if self.model is None or not text.strip():
            return {}
        embedding = self.model.encode(
            [text], normalize_embeddings=True, convert_to_numpy=True
        )
        scores = cosine_similarity(embedding, self.description_embeddings)[0]
        return {
            label: float(score)
            for label, score in zip(CATEGORY_DESCRIPTIONS, scores)
        }

@st.cache_resource(show_spinner=False)
def load_semantic_engine(model_name: str) -> SemanticEngine:
    return SemanticEngine(model_name)

def analyze_turn(
    beats: list[dict],
    index: int,
    engine: Optional[SemanticEngine],
    threshold: float,
    history_size: int,
    context_weight: float
) -> dict:
    beat = beats[index]
    context = build_context(beats, index, history_size)
    lexical = lexical_evidence(beat["text"])

    # Score the current utterance separately from the context-enriched representation.
    # This reduces (but does not eliminate) attribution of prior speakers' words to this turn.
    current_scores = engine.score(beat["text"]) if engine and engine.model else {}
    contextual_text = (
        f"Current speaker: {beat['speaker']}. "
        f"Current utterance: {beat['text']}. "
        f"Recent dialogue: {context['context_text'][-1000:]}. "
        f"Previous utterances by this speaker: {context['speaker_history'][-500:]}."
    )
    contextual_scores = (
        engine.score(contextual_text) if engine and engine.model and context["context_text"] else current_scores
    )

    final_scores = {}
    if current_scores:
        for label in CATEGORY_DESCRIPTIONS:
            current = current_scores.get(label, 0.0)
            contextual = contextual_scores.get(label, current)
            final_scores[label] = (
                (1.0-context_weight) * current + context_weight * contextual
            )

    ranked = sorted(final_scores.items(), key=lambda item: item[1], reverse=True)
    semantic_labels = []
    if ranked:
        # Dynamic Interaction is a fallback, not a competing semantic label.
        semantic_labels = [
            label for label, score in ranked
            if label != "Dynamic Interaction" and score >= threshold
        ]
        if not semantic_labels:
            semantic_labels = ["Dynamic Interaction"]
        top_score = ranked[0][1]
        second_score = ranked[1][1] if len(ranked) > 1 else None
        margin = top_score-second_score if second_score is not None else None
        semantic_status = "Candidate labels; human review required"
    else:
        top_score, margin = None, None
        semantic_status = "Semantic model unavailable"

    lexical_labels = [
        label for label, evidence in lexical.items() if evidence["positive"]
    ]
    combined = list(dict.fromkeys(lexical_labels + semantic_labels))
    if not combined:
        combined = ["Dynamic Interaction"]

    return {
        **beat,
        "context_text": context["context_text"],
        "speaker_history": context["speaker_history"],
        "lexical_evidence": lexical,
        "lexical_labels": lexical_labels,
        "current_semantic_scores": current_scores,
        "contextual_semantic_scores": contextual_scores,
        "semantic_scores": final_scores,
        "semantic_labels": semantic_labels,
        "combined_labels": combined,
        "top_similarity": top_score,
        "top_margin": margin,
        "semantic_status": semantic_status,
        "word_count": len(tokenize(beat["text"])),
        "is_question": "?" in beat["text"],
        "stage_silence": "explicit stage direction" in lexical["Silence / Void"]["positive"],
        "interpretation_warning": (
            "Similarity is not a probability. Context is limited and may introduce speaker/topic "
            "contamination. Metaphor, irony, sarcasm and pragmatic meaning require human review."
        )
    }

def analyze_corpus(
    corpus: str,
    engine: Optional[SemanticEngine] = None,
    threshold: float = 0.34,
    history_size: int = 4,
    context_weight: float = 0.25
) -> list[dict]:
    beats = parse_corpus(corpus)
    results = [
        analyze_turn(
            beats, i, engine, threshold, history_size, context_weight
        )
        for i in range(len(beats))
    ]
    previous_words = {}
    for row in results:
        old = previous_words.get(row["speaker"])
        row["previous_same_speaker_words"] = old
        row["within_speaker_word_change"] = (
            row["word_count"] - old if old is not None else None
        )
        previous_words[row["speaker"]] = row["word_count"]
    return results

def corpus_metrics(results: list[dict]) -> dict:
    if not results:
        return {}
    tokens = [token for row in results for token in tokenize(row["text"])]
    labels = Counter(
        label for row in results for label in row["combined_labels"]
    )
    return {
        "turns": len(results),
        "speakers": len({row["speaker"] for row in results}),
        "words": len(tokens),
        "average_turn_length": round(float(np.mean([r["word_count"] for r in results])), 2),
        "questions": sum(row["is_question"] for row in results),
        "lexical_diversity": round(len(set(tokens))/len(tokens), 3) if tokens else 0,
        "label_counts": dict(labels)
    }

def participation_table(results: list[dict]) -> pd.DataFrame:
    stats = defaultdict(lambda: {"turns": 0, "words": 0, "questions": 0})
    for row in results:
        item = stats[row["speaker"]]
        item["turns"] += 1
        item["words"] += row["word_count"]
        item["questions"] += int(row["is_question"])
    total_turns = max(1, len(results))
    total_words = max(1, sum(row["word_count"] for row in results))
    rows = [{
        "Speaker": speaker,
        "Turns": item["turns"],
        "Words": item["words"],
        "Turn share (%)": round(100*item["turns"]/total_turns, 1),
        "Word share (%)": round(100*item["words"]/total_words, 1),
        "Questions": item["questions"]
    } for speaker, item in stats.items()]
    return pd.DataFrame(rows).sort_values("Turn share (%)", ascending=False)

def question_audit(beats: list[dict], lookahead: int = 3) -> list[dict]:
    rows = []
    for i, beat in enumerate(beats):
        if "?" not in beat["text"]:
            continue
        candidate = next(
            (
                beats[j] for j in range(i+1, min(len(beats), i+1+lookahead))
                if beats[j]["speaker"] != beat["speaker"]
            ),
            None
        )
        overlap = tfidf_similarity(beat["text"], candidate["text"]) if candidate else None
        rows.append({
            "Beat": beat["beat"],
            "Question speaker": beat["speaker"],
            "Question": beat["text"],
            "Candidate speaker": candidate["speaker"] if candidate else None,
            "Candidate response": candidate["text"] if candidate else None,
            "TF-IDF lexical overlap (not answer score)": round(overlap, 3) if overlap is not None else None,
            "Review": "Candidate only; human review must determine whether it answers the question."
        })
    return rows

def turning_point_candidates(results: list[dict]) -> list[dict]:
    if len(results) < 3:
        return []
    lengths = np.array([row["word_count"] for row in results], dtype=float)
    median = float(np.median(lengths))
    mad = float(np.median(np.abs(lengths-median)))
    output = []
    for row in results:
        robust_deviation = 0.6745*(row["word_count"]-median)/mad if mad else 0.0
        flags = []
        if abs(robust_deviation) >= 2.5:
            flags.append("Turn length outlier")
        if row["stage_silence"]:
            flags.append("Explicit pause/silence direction")
        if row["is_question"]:
            flags.append("Question form")
        if len(row["combined_labels"]) >= 3:
            flags.append("Multiple candidate labels")
        if flags:
            output.append({
                "Beat": row["beat"],
                "Speaker": row["speaker"],
                "Text": row["text"],
                "Word count": row["word_count"],
                "Robust length deviation": round(float(robust_deviation), 2),
                "Observable flags": "; ".join(flags),
                "Interpretation": "Descriptive candidate only, not a validated turning-point prediction."
            })
    return output

def parse_label_cell(value) -> list[str]:
    if pd.isna(value):
        return []
    return [part.strip() for part in re.split(r"[;|]", str(value)) if part.strip()]

def multilabel_validation(df: pd.DataFrame, gold_col: str, pred_col: str) -> Optional[dict]:
    clean = df[[gold_col, pred_col]].dropna()
    if clean.empty:
        return None
    y_true_lists = clean[gold_col].apply(parse_label_cell).tolist()
    y_pred_lists = clean[pred_col].apply(parse_label_cell).tolist()
    labels = sorted(set(x for row in y_true_lists+y_pred_lists for x in row))
    if not labels:
        return None
    mlb = MultiLabelBinarizer(classes=labels)
    y_true = mlb.fit_transform(y_true_lists)
    y_pred = mlb.transform(y_pred_lists)
    p, r, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average="macro", zero_division=0
    )
    micro_p, micro_r, micro_f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average="micro", zero_division=0
    )
    exact_match = float(np.mean(np.all(y_true == y_pred, axis=1)))
    return {
        "n": len(clean),
        "labels": labels,
        "macro_precision": float(p),
        "macro_recall": float(r),
        "macro_f1": float(f1),
        "micro_precision": float(micro_p),
        "micro_recall": float(micro_r),
        "micro_f1": float(micro_f1),
        "exact_match": exact_match,
        "y_true": y_true,
        "y_pred": y_pred
    }

def corpus_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def show_turns(results: list[dict]) -> None:
    for row in results:
        heading = f"Beat {row['beat']} · {row['speaker']} · {', '.join(row['combined_labels'])}"
        with st.expander(heading):
            st.write("**Utterance:**", row["text"])
            c1, c2, c3 = st.columns(3)
            c1.metric("Words", row["word_count"])
            c2.metric(
                "Top similarity",
                f"{row['top_similarity']:.3f}" if row["top_similarity"] is not None else "N/A"
            )
            c3.metric("Semantic status", row["semantic_status"])
            st.write("**Semantic candidate labels:**", ", ".join(row["semantic_labels"]) or "Unavailable")
            st.write("**Lexical labels:**", ", ".join(row["lexical_labels"]) or "No positive lexical markers")
            evidence = {
                key: value for key, value in row["lexical_evidence"].items()
                if value["positive"] or value["negated"]
            }
            if evidence:
                st.json(evidence)
            if row["context_text"]:
                st.write("**Recent dialogue:**", row["context_text"])
            if row["speaker_history"]:
                st.write("**This speaker's recent history:**", row["speaker_history"])
            st.caption(row["interpretation_warning"])

# ------------------------------- Streamlit UI -------------------------------

st.set_page_config(
    page_title="Ontological Silence Engine V4",
    page_icon="👁️",
    layout="wide"
)
st.title("👁️ Ontological Silence & Paranoia Engine")
st.caption("V4 · Context-aware semantic research prototype · Computational Dramaturgy")
st.warning(
    "This is an exploratory text-analysis tool. It does not establish intent, deception, "
    "psychological states, or truth. Semantic similarities are not calibrated probabilities."
)

with st.sidebar:
    st.header("Research controls")
    module = st.radio(
        "Module",
        [
            "Research framework",
            "Contextual scene analyzer",
            "Participation analysis",
            "Question-response audit",
            "Turning-point candidates",
            "Validation workspace",
            "Export & reproducibility"
        ]
    )
    st.divider()
    use_semantic = st.checkbox("Enable sentence embeddings", value=True)
    model_name = st.text_input("Embedding model", value=DEFAULT_MODEL)
    threshold = st.slider("Similarity threshold (exploratory)", 0.10, 0.80, 0.34, 0.01)
    history_size = st.slider("Previous turns in context", 0, 8, 4)
    context_weight = st.slider("Context contribution", 0.0, 0.70, 0.25, 0.05)
    st.caption(f"Version {APP_VERSION} · {dt.date.today().isoformat()}")

engine = None
if use_semantic:
    with st.spinner("Loading sentence-embedding model (first run may take time)..."):
        engine = load_semantic_engine(model_name.strip() or DEFAULT_MODEL)
    if engine.model is None:
        st.error("Semantic model unavailable. Lexical analysis remains available.")
        with st.expander("Model loading details"):
            st.code(engine.error or "No error details available.")

if module == "Research framework":
    st.header("Research framework")
    st.markdown("""
**Research question:** Can transparent lexical evidence and contextual semantic representations
help researchers identify observable patterns associated with silence, conversational avoidance,
withdrawal, control language, and changes in dramatic interaction?

**Pipeline**
1. Dialogue parsing and speaker attribution.
2. Transparent lexical evidence and approximate negation handling.
3. Sentence-embedding similarity on the current utterance.
4. A separate context-enriched representation using recent turns and speaker history.
5. Human annotation, held-out evaluation, and error analysis.

The model does not understand every word or infer hidden intentions. Embeddings can misread
metaphor, irony, sarcasm, cultural references, pragmatics, and long-range narrative dependencies.
""")
    st.subheader("Research safeguards")
    st.write("- Treat similarity values as ranking signals, not probabilities.")
    st.write("- Keep lexical evidence separate from semantic suggestions.")
    st.write("- Treat participation volume as participation, not social dominance.")
    st.write("- Treat question-response links and turning-point flags as candidates for human review.")
    st.write("- Use independent annotators and held-out test data before making performance claims.")

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
                corpus, engine, threshold, history_size, context_weight
            )
            st.session_state["results"] = results
            st.session_state["corpus"] = corpus
            st.session_state["analysis_settings"] = {
                "threshold": threshold,
                "history_size": history_size,
                "context_weight": context_weight,
                "model": model_name if engine and engine.model else "lexical-only"
            }
            metrics = corpus_metrics(results)
            a, b, c, d = st.columns(4)
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
        results = analyze_corpus(corpus, engine, threshold, history_size, context_weight)
        if not results:
            st.warning("No dialogue found.")
        else:
            frame = participation_table(results)
            st.dataframe(frame, use_container_width=True)
            st.bar_chart(frame.set_index("Speaker")[["Turn share (%)", "Word share (%)"]])
            st.info("Participation volume does not establish social dominance, authority, or power.")

elif module == "Question-response audit":
    st.header("Question-response audit")
    corpus = st.text_area("Dialogue corpus", height=240, key="question_text")
    lookahead = st.slider("Maximum later turns to inspect", 1, 8, 3)
    if st.button("Audit questions"):
        audit = question_audit(parse_corpus(corpus), lookahead)
        if audit:
            st.dataframe(pd.DataFrame(audit), use_container_width=True)
        else:
            st.info("No question marks found.")
        st.caption("A nearby turn is only a response candidate; human review is required.")

elif module == "Turning-point candidates":
    st.header("Turning-point candidates")
    corpus = st.text_area("Dialogue corpus", height=240, key="turning_text")
    if st.button("Find observable changes"):
        results = analyze_corpus(corpus, engine, threshold, history_size, context_weight)
        if len(results) < 3:
            st.warning("At least three turns are recommended.")
        else:
            chart_data = pd.DataFrame(
                {"Word count": [row["word_count"] for row in results]},
                index=[f"Beat {row['beat']}" for row in results]
            )
            st.line_chart(chart_data)
            candidates = turning_point_candidates(results)
            if candidates:
                st.dataframe(pd.DataFrame(candidates), use_container_width=True)
            else:
                st.info("No candidates were flagged by the current descriptive rules.")

elif module == "Validation workspace":
    st.header("Multi-label validation workspace")
    st.markdown("""
Upload a CSV with `gold_labels` and `predicted_labels` columns.
Separate multiple labels in each cell with semicolons, for example:
`Aggression; Emotional Withdrawal`.

Use independently annotated held-out items. Do not tune thresholds on the test set.
""")
    uploaded = st.file_uploader("Upload evaluation CSV", type=["csv"])
    if uploaded:
        try:
            frame = pd.read_csv(uploaded)
            required = {"gold_labels", "predicted_labels"}
            if not required.issubset(frame.columns):
                st.error("CSV must contain gold_labels and predicted_labels columns.")
            else:
                metrics = multilabel_validation(frame, "gold_labels", "predicted_labels")
                if metrics:
                    c1, c2, c3, c4 = st.columns(4)
                    c1.metric("Items", metrics["n"])
                    c2.metric("Macro-F1", f"{metrics['macro_f1']:.3f}")
                    c3.metric("Micro-F1", f"{metrics['micro_f1']:.3f}")
                    c4.metric("Exact match", f"{metrics['exact_match']:.3f}")
                    st.write({
                        "Macro precision": round(metrics["macro_precision"], 3),
                        "Macro recall": round(metrics["macro_recall"], 3),
                        "Micro precision": round(metrics["micro_precision"], 3),
                        "Micro recall": round(metrics["micro_recall"], 3)
                    })
                    report = classification_report(
                        metrics["y_true"], metrics["y_pred"],
                        target_names=metrics["labels"], zero_division=0
                    )
                    st.text(report)
                    st.caption(
                        "Exact match requires every label for an item to match. "
                        "Macro-F1 weights labels equally; micro-F1 aggregates decisions."
                    )
                else:
                    st.warning("No valid labelled rows found.")
        except Exception as exc:
            st.error(f"Could not read evaluation file: {type(exc).__name__}: {exc}")

elif module == "Export & reproducibility":
    st.header("Export & reproducibility")
    results = st.session_state.get("results")
    corpus = st.session_state.get("corpus", "")
    settings = st.session_state.get("analysis_settings", {})
    if not results:
        st.info("Run the contextual scene analyzer first.")
    else:
        metadata = {
            "app_version": APP_VERSION,
            "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "corpus_sha256": corpus_hash(corpus),
            "embedding_model": settings.get("model", "unknown"),
            "semantic_threshold": settings.get("threshold"),
            "context_history_turns": settings.get("history_size"),
            "context_weight": settings.get("context_weight"),
            "warning": "Similarity values are not calibrated probabilities."
        }
        st.json(metadata)
        payload = {"metadata": metadata, "results": results}
        st.download_button(
            "Download analysis JSON",
            data=json.dumps(payload, ensure_ascii=False, indent=2, default=str),
            file_name="ontological_silence_analysis.json",
            mime="application/json"
        )
        flat_rows = []
        for row in results:
            flat_rows.append({
                "beat": row["beat"],
                "speaker": row["speaker"],
                "text": row["text"],
                "lexical_labels": "; ".join(row["lexical_labels"]),
                "semantic_labels": "; ".join(row["semantic_labels"]),
                "combined_labels": "; ".join(row["combined_labels"]),
                "top_similarity": row["top_similarity"],
                "semantic_status": row["semantic_status"]
            })
        st.download_button(
            "Download turn-level CSV",
            data=pd.DataFrame(flat_rows).to_csv(index=False).encode("utf-8-sig"),
            file_name="ontological_silence_turns.csv",
            mime="text/csv"
        )
'''

requirements = """streamlit==1.40.2
pandas>=2.2,<3
numpy>=1.26,<3
scikit-learn>=1.5,<2
sentence-transformers>=3.3,<6
torch>=2.5,<3
"""

tests = r'''import unittest
from app import (
    tokenize, parse_corpus, lexical_evidence, analyze_corpus,
    corpus_metrics, question_audit, parse_label_cell
)

class EngineTests(unittest.TestCase):
    def test_tokenize_contractions(self):
        self.assertIn("don't", tokenize("I don't know."))

    def test_parse_dialogue(self):
        beats = parse_corpus("Mia: Are you there?\nJohn: Yes.")
        self.assertEqual(len(beats), 2)
        self.assertEqual(beats[0]["speaker"], "Mia")

    def test_negated_marker(self):
        evidence = lexical_evidence("I am not afraid.")
        self.assertIn("afraid", evidence["Emotional Withdrawal"]["negated"])
        self.assertNotIn("afraid", evidence["Emotional Withdrawal"]["positive"])

    def test_empty_corpus(self):
        self.assertEqual(analyze_corpus(""), [])

    def test_metrics(self):
        results = analyze_corpus("Mia: Hello.\nJohn: Hello.")
        self.assertEqual(corpus_metrics(results)["turns"], 2)

    def test_question_audit(self):
        rows = question_audit(parse_corpus("Mia: Why?\nJohn: Because I left."), 2)
        self.assertEqual(len(rows), 1)

    def test_parse_multilabel_cell(self):
        self.assertEqual(
            parse_label_cell("Aggression; Emotional Withdrawal"),
            ["Aggression", "Emotional Withdrawal"]
        )

if __name__ == "__main__":
    unittest.main()
'''

readme = r'''# Ontological Silence & Paranoia Engine — V4

Streamlit Cloud-compatible exploratory research prototype for computational dialogue analysis.

## Repository structure

```text
narrative_tech/
├── app.py
├── requirements.txt
├── README.md
└── test_core.py
```

## Deploy to Streamlit Community Cloud

1. Put these files in the root of your GitHub repository.
2. In Streamlit Community Cloud, select the repository and set **Main file path** to `app.py`.
3. Deploy. Do not paste this README or a ZIP-generation script into `app.py`.

The first semantic-model run downloads `sentence-transformers/all-MiniLM-L6-v2`.
It requires internet access and can take several minutes. If model loading fails,
the app keeps its lexical-analysis functionality.

## Run locally

Python 3.11 is recommended for broad compatibility with PyTorch and sentence-transformers.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Tests

```bash
python -m unittest -v
```

## Methodological limitations

- Sentence embeddings compare text with category descriptions. Similarity values are ranking signals, not probabilities.
- The context-enriched representation can still mix prior speakers' content into a current turn.
- Negation handling uses a local token window, not full syntactic scope.
- Lexical matches can misread metaphor, polysemy, irony, and sarcasm.
- Question-response links are candidate links, not confirmed answers.
- Participation shares do not establish power or dominance.
- Turning-point flags are descriptive candidates, not validated predictions.
- Multi-label validation requires independent human annotations and a held-out test set.

Do not describe this prototype as a mind reader, psychological detector, deception detector,
or validated classifier without appropriate empirical evidence.
'''

(root / "app.py").write_text(app_code, encoding="utf-8")
(root / "requirements.txt").write_text(requirements, encoding="utf-8")
(root / "test_core.py").write_text(tests, encoding="utf-8")
(root / "README.md").write_text(readme, encoding="utf-8")

# Verify Python syntax and create the deliverable archive.
py_compile.compile(str(root / "app.py"), doraise=True)
py_compile.compile(str(root / "test_core.py"), doraise=True)

zip_path = Path("/mnt/data/ontological_silence_v4_streamlit.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
    for file_path in root.iterdir():
        archive.write(file_path, arcname=f"ontological_silence_v4/{file_path.name}")

print("Created:", zip_path)
print("Project files:", ", ".join(p.name for p in root.iterdir()))
print("Python syntax check: passed for app.py and test_core.py")
