from pathlib import Path
import zipfile, textwrap

app_code = r'''import re
import html
import math
import json
import hashlib
import datetime as dt
from collections import Counter, defaultdict

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import cohen_kappa_score, confusion_matrix, precision_recall_fscore_support

# =============================================================================
# ONTOLOGICAL SILENCE & PARANOIA ENGINE — RESEARCH PROTOTYPE V2
# A transparent, rule-assisted discourse-analysis tool.
# IMPORTANT: outputs are indicators for human review, not psychological facts.
# =============================================================================

st.set_page_config(
    page_title="Ontological Silence & Paranoia Engine",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded",
)

APP_VERSION = "2.0.0"
CATEGORIES = [
    "Silence / Void",
    "Aggression",
    "Emotional Withdrawal",
    "Defensive Rationalization",
    "Direct Inquiry",
    "Surveillance / Control",
    "Lack / Desire",
    "Bad Faith Indicators",
    "Dynamic Interaction",
]

CATEGORY_COLORS = {
    "Silence / Void": "#f85149",
    "Aggression": "#ff7b72",
    "Emotional Withdrawal": "#bc8cff",
    "Defensive Rationalization": "#f0883e",
    "Direct Inquiry": "#58a6ff",
    "Surveillance / Control": "#d2a8ff",
    "Lack / Desire": "#79c0ff",
    "Bad Faith Indicators": "#ffa657",
    "Dynamic Interaction": "#3fb950",
}

# Phrase-level patterns are deliberately conservative. They are indicators,
# not a complete ontology or a validated psychological lexicon.
LEXICON = {
    "AGGRESSIVE": {
        "attack", "kill", "destroy", "threat", "force", "obey", "punish",
        "fight", "hate", "angry", "furious", "violent", "brutal", "cruel",
        "murder", "weapon", "enemy", "war", "shut", "order", "demand",
        "strike", "break", "revenge", "idiot", "stupid", "damn", "bomb",
        "gun", "knife", "hurt", "harm", "revenge",
    },
    "SILENCE": {
        "silence", "quiet", "hush", "mute", "speechless", "wordless",
        "nothing", "empty", "void", "absence", "forgotten", "missing",
        "hollow", "abyss", "blank", "desolate", "abandoned", "soundless",
    },
    "WITHDRAWAL": {
        "sad", "cry", "tears", "pain", "hurt", "fear", "afraid", "scared",
        "anxious", "broken", "lonely", "regret", "sorry", "goodbye",
        "leave", "depressed", "miserable", "unhappy", "sorrow", "grief",
        "miss", "longing", "nostalgia", "weak", "fragile", "helpless",
        "vulnerable", "tired", "exhausted", "heartbroken", "wounded",
    },
    "DEFENSE": {
        "truth", "reality", "reason", "logic", "because", "understand",
        "explain", "justify", "rationalize", "deny", "avoid", "deflect",
        "distract", "divert", "escape", "pretend", "excuse", "defend",
        "responsibility", "forced", "cannot", "impossible",
    },
    "INQUIRY": {
        "what", "where", "when", "who", "whom", "whose", "which", "why",
        "how", "ask", "question", "inquire", "wonder", "investigate",
        "examine", "interrogate", "challenge", "doubt", "suspect",
    },
    "SURVEILLANCE": {
        "watch", "watched", "watching", "observe", "observed", "monitor",
        "monitoring", "control", "surveillance", "record", "recording",
        "follow", "followed", "authority", "power", "discipline", "prison",
        "camera", "guard", "inspect", "inspection", "institution", "track",
    },
    "LACK": {
        "empty", "nothing", "absence", "missing", "desire", "want", "need",
        "lost", "void", "alone", "lack", "incomplete", "unfulfilled",
    },
    "BAD_FAITH": {
        "pretend", "deny", "excuse", "justify", "rationalize", "avoid",
        "responsibility", "truth", "choice", "freedom", "cannot",
        "impossible", "forced", "duty", "must",
    },
}

PHRASES = {
    "SILENCE": [
        "say nothing", "not a word", "fell silent", "kept quiet",
        "refused to speak", "there was a pause", "long silence",
    ],
    "WITHDRAWAL": [
        "leave me alone", "stay away", "i cannot go on", "i feel alone",
        "i do not want to talk", "i don't want to talk",
    ],
    "DEFENSE": [
        "that is not my fault", "that's not my fault", "you misunderstood",
        "i had no choice", "it was not my decision", "it wasn't my decision",
        "i was only trying", "you have to understand",
    ],
    "SURVEILLANCE": [
        "i am watching you", "i'm watching you", "you are being watched",
        "someone is watching", "under observation",
    ],
    "BAD_FAITH": [
        "i had no choice", "i couldn't do otherwise", "i could not do otherwise",
        "that is just how things are", "that's just how things are",
    ],
}

NEGATORS = {
    "not", "no", "never", "neither", "nor", "hardly", "barely", "without",
    "isn't", "aren't", "wasn't", "weren't", "don't", "doesn't", "didn't",
    "can't", "cannot", "couldn't", "won't", "wouldn't", "shouldn't",
}
NEGATION_WINDOW = 3
QUESTION_WORDS = {"what", "where", "when", "who", "whom", "whose", "which", "why", "how"}
STOP_WORDS = {
    "the", "and", "for", "but", "with", "from", "this", "that", "was",
    "were", "are", "has", "have", "had", "there", "here", "they", "them",
    "she", "him", "her", "its", "you", "your", "his", "our", "their",
    "then", "than", "into", "about", "just", "very", "been", "being",
    "will", "would", "could", "should", "does", "did", "a", "an", "to",
    "of", "in", "on", "it", "i", "we", "he", "as", "at", "by", "or",
}

st.markdown("""
<style>
.stApp { background:#07090e; color:#f1f5f9; font-family:'Courier New',monospace; }
[data-testid="stSidebar"] { background:#0d1117; border-right:1px solid #30363d; }
[data-testid="stSidebar"] * { color:#c9d1d9; }
h1,h2,h3,h4,label { color:#fff !important; font-family:'Courier New',monospace !important; }
.stTextArea textarea,.stTextInput input { background:#0d1117 !important; color:#58a6ff !important; border:1px solid #30363d !important; }
.stButton button { background:#f0883e !important; color:#07090e !important; font-weight:bold !important; border-radius:5px; }
.lab-card { background:#0d1117; border:1px solid #30363d; border-left:4px solid #f0883e; padding:16px; border-radius:6px; margin-bottom:12px; }
.context-box { background:#0f1c2e; border:1px solid #1f3864; padding:16px; border-radius:6px; margin-bottom:15px; }
[data-testid="stMetricValue"] { color:#f0883e !important; }
.small-note { color:#9da7b3; font-size:0.85rem; }
</style>
""", unsafe_allow_html=True)


# =============================================================================
# CORE TEXT FUNCTIONS
# =============================================================================

def tokenize(text):
    """Unicode-aware word tokenizer; keeps apostrophes inside contractions."""
    return re.findall(r"[^\W_]+(?:['’][^\W_]+)?", str(text).lower(), flags=re.UNICODE)


def normalize_text(text):
    return re.sub(r"\s+", " ", str(text)).strip()


def lexical_vector(text):
    tokens = tokenize(text)
    return Counter(t for t in tokens if len(t) > 2 and t not in STOP_WORDS)


def safe_html(value):
    return html.escape(str(value))


def parse_corpus(text):
    """Parse 'Speaker: dialogue'. Unlabelled lines get stable Actor labels."""
    beats = []
    for line_no, raw in enumerate(str(text).splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        match = re.match(r"^([^:]{1,60}):\s*(.*)$", line)
        if match:
            speaker = match.group(1).strip()
            dialogue = match.group(2).strip().lstrip("-— ").strip()
        else:
            speaker = f"Actor {line_no}"
            dialogue = line.lstrip("-— ").strip()
        if dialogue:
            beats.append({
                "beat": len(beats) + 1,
                "source_line": line_no,
                "speaker": speaker,
                "text": dialogue,
                "original": line,
            })
    return beats


def _negated(tokens, index, window=NEGATION_WINDOW):
    start = max(0, index - window)
    preceding = tokens[start:index]
    # A conjunction/punctuation boundary is handled before tokenization only
    # approximately; this conservative window avoids claiming full syntax.
    return any(token in NEGATORS for token in preceding)


def classify_text(text, context_text=""):
    """
    Transparent multi-label lexical baseline.
    Negated lexical hits are retained as evidence but excluded from positive
    marker counts. This is not full syntactic scope resolution.
    """
    raw = str(text)
    tokens = tokenize(raw)
    token_set = set(tokens)
    positive = defaultdict(list)
    negated = defaultdict(list)
    phrase_hits = defaultdict(list)

    for category, lexicon in LEXICON.items():
        for i, token in enumerate(tokens):
            if token in lexicon:
                if _negated(tokens, i):
                    negated[category].append(token)
                else:
                    positive[category].append(token)

    lowered = raw.lower()
    for category, phrases in PHRASES.items():
        for phrase in phrases:
            if phrase in lowered:
                phrase_hits[category].append(phrase)

    # Explicit stage directions are distinct from a lexical mention of silence.
    stage_silence = bool(re.search(
        r"[\[(]\s*(silence|pause|long pause|beat)\s*[\])]", lowered
    ))
    if stage_silence:
        phrase_hits["SILENCE"].append("stage direction: silence/pause")

    # Question form is a structural feature; it does not imply a psychological state.
    is_question = "?" in raw or (tokens and tokens[0] in QUESTION_WORDS)
    if is_question:
        positive["INQUIRY"].append("question structure")

    # Map internal markers to public labels.
    mapping = {
        "SILENCE": "Silence / Void",
        "AGGRESSIVE": "Aggression",
        "WITHDRAWAL": "Emotional Withdrawal",
        "DEFENSE": "Defensive Rationalization",
        "INQUIRY": "Direct Inquiry",
        "SURVEILLANCE": "Surveillance / Control",
        "LACK": "Lack / Desire",
        "BAD_FAITH": "Bad Faith Indicators",
    }

    evidence = {}
    active_labels = []
    for key, label in mapping.items():
        pos = sorted(set(positive.get(key, []) + phrase_hits.get(key, [])))
        neg = sorted(set(negated.get(key, [])))
        if pos:
            active_labels.append(label)
        evidence[label] = {"positive": pos, "negated": neg}

    if not active_labels:
        active_labels = ["Dynamic Interaction"]

    # Primary label is only a display convenience; all labels remain visible.
    priority = [
        "Silence / Void", "Aggression", "Emotional Withdrawal",
        "Defensive Rationalization", "Surveillance / Control",
        "Bad Faith Indicators", "Lack / Desire", "Direct Inquiry",
        "Dynamic Interaction",
    ]
    primary = next((x for x in priority if x in active_labels), "Dynamic Interaction")

    return {
        "category": primary,
        "labels": active_labels,
        "evidence": evidence,
        "is_question": bool(is_question),
        "stage_silence": stage_silence,
        "token_count": len(tokens),
        "method": "Transparent lexical + phrase rules",
        "limitations": [
            "Negation scope is approximate, not a full syntactic parse.",
            "Metaphor, irony, sarcasm and speaker intention require human/contextual review.",
            "Lexical indicators do not establish psychological states or intent.",
        ],
    }


def _tfidf_pair_similarity(text_a, text_b):
    """Word+character TF-IDF similarity; lexical-semantic proxy, not meaning."""
    a, b = normalize_text(text_a), normalize_text(text_b)
    if not a or not b:
        return None
    if a == b:
        return 1.0
    try:
        vec = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            analyzer="word",
            sublinear_tf=True,
            token_pattern=r"(?u)\b\w+\b",
        )
        matrix = vec.fit_transform([a, b])
        if matrix.shape[1] == 0:
            return 0.0
        return float(cosine_similarity(matrix[0], matrix[1])[0, 0])
    except ValueError:
        return 0.0


def analyze_corpus(corpus):
    beats = parse_corpus(corpus)
    if not beats:
        return []

    previous_by_speaker = {}
    results = []
    for i, beat in enumerate(beats):
        text = beat["text"]
        speaker = beat["speaker"]
        tokens = tokenize(text)
        word_count = len(tokens)
        previous = previous_by_speaker.get(speaker)
        if previous is None or previous == 0:
            compression = None
        else:
            compression = (previous - word_count) / previous
        previous_by_speaker[speaker] = word_count

        if i > 0:
            prev_beat = beats[i - 1]
            similarity = _tfidf_pair_similarity(prev_beat["text"], text)
            transition = {
                "previous_speaker": prev_beat["speaker"],
                "speaker_changed": prev_beat["speaker"] != speaker,
                "similarity": similarity,
                "lexical_divergence": (1 - similarity) if similarity is not None else None,
                "interpretation": (
                    "Low lexical overlap; may reflect topic shift, paraphrase, or non-response. "
                    "Not proof of evasion."
                ),
            }
        else:
            transition = {
                "previous_speaker": None,
                "speaker_changed": False,
                "similarity": None,
                "lexical_divergence": None,
                "interpretation": "No preceding turn.",
            }

        classification = classify_text(text)
        results.append({
            **beat,
            **classification,
            "words": word_count,
            "questions": text.count("?"),
            "same_speaker_previous_words": previous,
            "compression": round(compression, 3) if compression is not None else None,
            **transition,
        })
    return results


def corpus_metrics(results):
    if not results:
        return {}
    counts = [r["words"] for r in results]
    all_tokens = [t for r in results for t in tokenize(r["text"])]
    return {
        "turns": len(results),
        "words": sum(counts),
        "average_words": round(float(np.mean(counts)), 2),
        "median_words": round(float(np.median(counts)), 2),
        "speakers": len(set(r["speaker"] for r in results)),
        "questions": sum(r["questions"] for r in results),
        "unique_words": len(set(all_tokens)),
        "lexical_diversity": round(len(set(all_tokens)) / len(all_tokens), 3) if all_tokens else 0,
        "category_counts": dict(Counter(label for r in results for label in r["labels"])),
    }


def speaker_statistics(results):
    stats = defaultdict(lambda: {"turns": 0, "words": 0, "questions": 0, "labels": Counter()})
    for r in results:
        s = stats[r["speaker"]]
        s["turns"] += 1
        s["words"] += r["words"]
        s["questions"] += r["questions"]
        s["labels"].update(r["labels"])
    total_turns = max(1, len(results))
    total_words = max(1, sum(r["words"] for r in results))
    rows = []
    for speaker, s in stats.items():
        rows.append({
            "Speaker": speaker,
            "Turns": s["turns"],
            "Words": s["words"],
            "Turn Share (%)": round(100 * s["turns"] / total_turns, 1),
            "Word Share (%)": round(100 * s["words"] / total_words, 1),
            "Questions": s["questions"],
            "Most Frequent Marker": s["labels"].most_common(1)[0][0] if s["labels"] else "None",
        })
    return pd.DataFrame(rows).sort_values("Turn Share (%)", ascending=False)


def question_response_audit(beats, max_lookahead=3):
    """Candidate response window; flags are review prompts, not intent judgments."""
    audit = []
    for i, beat in enumerate(beats):
        if "?" not in beat["text"]:
            continue
        candidate = None
        for j in range(i + 1, min(len(beats), i + 1 + max_lookahead)):
            if beats[j]["speaker"] != beat["speaker"]:
                candidate = beats[j]
                break
        if candidate is None:
            status = "No candidate response in look-ahead window"
            similarity = None
            response_labels = []
        else:
            similarity = _tfidf_pair_similarity(beat["text"], candidate["text"])
            response_labels = classify_text(candidate["text"])["labels"]
            # The score is not an evasion probability; it is an overlap diagnostic.
            if similarity is None:
                status = "Manual review required"
            elif similarity < 0.05:
                status = "Low lexical overlap — manual review"
            else:
                status = "Lexical overlap detected — manual review"
        audit.append({
            "Question Beat": beat["beat"],
            "Question Speaker": beat["speaker"],
            "Question": beat["text"],
            "Candidate Response Speaker": candidate["speaker"] if candidate else "None",
            "Candidate Response": candidate["text"] if candidate else "None",
            "TF-IDF Lexical Similarity": round(similarity, 3) if similarity is not None else None,
            "Candidate Response Labels": ", ".join(response_labels),
            "Review Status": status,
        })
    return audit


def turning_point_candidates(results):
    """Robust descriptive outlier flags based on observable lexical features."""
    if len(results) < 3:
        return []
    word_counts = np.array([r["words"] for r in results], dtype=float)
    median = float(np.median(word_counts))
    mad = float(np.median(np.abs(word_counts - median)))
    rows = []
    for i, r in enumerate(results):
        prev = results[i - 1]["words"] if i > 0 else None
        change = (r["words"] - prev) if prev is not None else None
        robust_z = (0.6745 * (r["words"] - median) / mad) if mad > 0 else 0.0
        marker_count = sum(len(v["positive"]) for v in r["evidence"].values())
        flags = []
        if abs(robust_z) >= 2.5:
            flags.append("Unusually long/short turn")
        if r["stage_silence"]:
            flags.append("Explicit silence/pause stage direction")
        if r["is_question"]:
            flags.append("Question-form turn")
        if marker_count >= 3:
            flags.append("Multiple lexical marker groups")
        if flags:
            rows.append({
                "Beat": r["beat"],
                "Speaker": r["speaker"],
                "Text": r["text"],
                "Word Count": r["words"],
                "Change From Previous Turn": change,
                "Robust Length Deviation": round(float(robust_z), 2),
                "Observable Flags": "; ".join(flags),
                "Interpretation": "Candidate for human narrative analysis; not a validated turning-point prediction.",
            })
    return rows


def theoretical_markers(text):
    tokens = tokenize(text)
    token_count = len(tokens)
    mapping = {
        "Sartrean Bad Faith (lexical proxy)": "BAD_FAITH",
        "Lacanian Lack / Desire (lexical proxy)": "LACK",
        "Foucauldian Surveillance (lexical proxy)": "SURVEILLANCE",
    }
    rows = []
    for name, key in mapping.items():
        hits = [t for t in tokens if t in LEXICON[key]]
        rows.append({
            "Framework (operational proxy)": name,
            "Matched token occurrences": len(hits),
            "Distinct matched terms": ", ".join(sorted(set(hits))) or "None",
            "Density per 100 tokens": round(100 * len(hits) / token_count, 2) if token_count else 0,
            "Interpretation": "Lexical density only; does not measure the philosophical construct.",
        })
    return rows


def _nominal_alpha_two_annotators(a, b):
    pairs = [(x, y) for x, y in zip(a, b) if pd.notna(x) and pd.notna(y)]
    if not pairs:
        return None
    observed_disagreement = sum(x != y for x, y in pairs) / len(pairs)
    pooled = [z for pair in pairs for z in pair]
    counts = Counter(pooled)
    n = len(pooled)
    expected_disagreement = 1 - sum((v / n) ** 2 for v in counts.values())
    if expected_disagreement == 0:
        return None
    return 1 - observed_disagreement / expected_disagreement


def validation_summary(df):
    complete = df.dropna(subset=["Annotator A", "Annotator B"]).copy()
    if complete.empty:
        return None
    a = complete["Annotator A"].tolist()
    b = complete["Annotator B"].tolist()
    return {
        "n": len(complete),
        "agreement": float(np.mean(np.array(a) == np.array(b))),
        "cohen_kappa": float(cohen_kappa_score(a, b)) if len(set(a) | set(b)) > 1 else None,
        "krippendorff_alpha_nominal": _nominal_alpha_two_annotators(a, b),
    }


def engine_vs_annotator_metrics(engine_labels, human_labels):
    pairs = [(e, h) for e, h in zip(engine_labels, human_labels) if pd.notna(h)]
    if not pairs:
        return None
    y_pred = [x[0] for x in pairs]
    y_true = [x[1] for x in pairs]
    p, r, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, labels=CATEGORIES, average="macro", zero_division=0
    )
    accuracy = float(np.mean(np.array(y_true) == np.array(y_pred)))
    return {"n": len(pairs), "accuracy": accuracy, "macro_precision": p, "macro_recall": r, "macro_f1": f1}


def show_results_cards(results):
    for r in results:
        labels = ", ".join(r["labels"])
        ev = []
        for label, data in r["evidence"].items():
            if data["positive"]:
                ev.append(f"{label}: {', '.join(data['positive'])}")
            if data["negated"]:
                ev.append(f"{label} (negated context): {', '.join(data['negated'])}")
        st.markdown(
            f"""<div class="lab-card">
            <b>Beat {r['beat']} | {safe_html(r['speaker'])}</b><br><br>
            <i style="color:#58a6ff">“{safe_html(r['text'])}”</i><br><br>
            <b>Primary display label:</b> {safe_html(r['category'])}<br>
            <b>All detected labels:</b> {safe_html(labels)}<br>
            <b>Word count:</b> {r['words']}<br>
            <b>Within-speaker length change:</b> {r['compression'] if r['compression'] is not None else 'Not available'}<br>
            <b>Adjacent-turn lexical similarity:</b> {round(r['similarity'], 3) if r['similarity'] is not None else 'Not available'}<br>
            <b>Evidence:</b> {safe_html(' | '.join(ev) if ev else 'No positive lexical evidence')}
            </div>""",
            unsafe_allow_html=True,
        )


def get_corpus_input(label, key, height=220):
    return st.text_area(
        label, key=key, height=height,
        placeholder="Character A: What happened?\nCharacter B: I don't know.",
    )


# =============================================================================
# SIDEBAR
# =============================================================================

MODULES = [
    "🏛️ Research Framework",
    "💬 Universal NLP Scene Analyzer",
    "🕸️ Character Relationship & Participation Map",
    "❓ Unanswered Question Tracker",
    "📈 Narrative Turning Point Candidates",
    "🔍 Explainable Analysis (XAI)",
    "⚖️ Comparative Dialogue Analyzer",
    "🔄 Rule-Based Branching Demonstrator",
    "⚛️ Theoretical Marker Index",
    "📊 Validation Protocol",
    "📜 Core Artifact & Limitations",
]

with st.sidebar:
    st.markdown("### 👁️ Terminal Control")
    st.caption("Computational Dramaturgy Lab | Research Prototype V2")
    selected_module = st.radio("Navigation Matrix", MODULES)
    st.divider()
    st.markdown("**Framework Architect:** Agil Chiragli")
    st.markdown(f"**Version:** {APP_VERSION}")
    st.caption(dt.date.today().isoformat())

st.title("👁️ Ontological Silence & Paranoia Engine")
st.caption("Transparent computational indicators for dialogue and narrative analysis")
st.warning(
    "Research-use notice: this version is a transparent lexical/discourse baseline. "
    "It does not understand every text, infer private mental states, or provide validated "
    "psychological measurements. Interpret outputs as candidates for human review."
)

# =============================================================================
# MODULE 1 — FRAMEWORK
# =============================================================================

if selected_module == MODULES[0]:
    st.header("Research Framework")
    st.markdown("""
    <div class="context-box">
    <b>RESEARCH QUESTION</b><br><br>
    Can transparent computational features help researchers identify observable
    textual patterns associated with silence, withdrawal, evasion candidates,
    surveillance language and shifts in dramatic interaction?
    </div>
    """, unsafe_allow_html=True)
    st.subheader("Operational principles")
    principles = [
        ("Observable evidence", "Every label must be linked to visible text or a measurable feature."),
        ("Multi-label output", "A turn may contain several co-occurring discourse markers."),
        ("Uncertainty", "The engine flags ambiguity rather than inventing certainty."),
        ("Human validation", "Independent annotators and held-out examples are required."),
        ("Construct validity", "Lexical proxies are not equivalent to philosophical or psychological constructs."),
        ("Reproducibility", "Version, settings, input corpus hash and exported outputs should be retained."),
    ]
    for title, body in principles:
        st.markdown(f"<div class='lab-card'><b>{title}</b><br>{body}</div>", unsafe_allow_html=True)
    st.subheader("What this version can and cannot claim")
    st.write("Can: count turns, words, speakers, lexical markers, question forms, participation shares, and candidate structural anomalies.")
    st.write("Cannot: reliably infer intention, diagnose paranoia, prove evasion, measure real power, or predict how a character will behave.")

# =============================================================================
# MODULE 2 — UNIVERSAL SCENE ANALYZER
# =============================================================================

elif selected_module == MODULES[1]:
    st.header("Universal NLP Scene Analyzer")
    corpus = get_corpus_input("Enter dialogue, scene or narrative text:", "xray_corpus")
    if st.button("⚡ Execute Scene Analysis", key="xray"):
        results = analyze_corpus(corpus)
        if not results:
            st.warning("Enter text before running analysis.")
        else:
            st.session_state["last_results"] = results
            st.session_state["last_corpus"] = corpus
            metrics = corpus_metrics(results)
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Turns", metrics["turns"])
            c2.metric("Words", metrics["words"])
            c3.metric("Speakers", metrics["speakers"])
            c4.metric("Questions", metrics["questions"])
            st.subheader("Beat-by-beat evidence")
            show_results_cards(results)
            st.subheader("Detected marker frequency")
            marker_counts = Counter(label for r in results for label in r["labels"])
            st.bar_chart(pd.DataFrame.from_dict(marker_counts, orient="index", columns=["Occurrences"]))
            st.subheader("Corpus statistics")
            st.dataframe(pd.DataFrame([{k: v for k, v in metrics.items() if k != "category_counts"}]), use_container_width=True)
            st.caption("Multi-label counts can exceed the number of turns because a turn can receive multiple labels.")

# =============================================================================
# MODULE 3 — PARTICIPATION MAP
# =============================================================================

elif selected_module == MODULES[2]:
    st.header("Character Relationship & Participation Map")
    corpus = get_corpus_input("Enter character dialogue:", "power_corpus")
    if st.button("⚡ Generate Participation Map", key="power"):
        results = analyze_corpus(corpus)
        if not results:
            st.warning("No dialogue detected.")
        else:
            df = speaker_statistics(results)
            st.subheader("Speaker participation matrix")
            st.dataframe(df, use_container_width=True)
            st.bar_chart(df.set_index("Speaker")[["Turn Share (%)", "Word Share (%)"]])
            st.info(
                "Turn share and word share describe participation volume only. "
                "They are not a measure of social dominance, authority, coercion or power."
            )

# =============================================================================
# MODULE 4 — QUESTION RESPONSE TRACKER
# =============================================================================

elif selected_module == MODULES[3]:
    st.header("Unanswered Question & Response Candidate Tracker")
    corpus = get_corpus_input("Enter dialogue:", "question_corpus")
    lookahead = st.slider("Maximum subsequent turns to inspect", 1, 6, 3)
    if st.button("⚡ Audit Questions", key="questions"):
        beats = parse_corpus(corpus)
        if not beats:
            st.warning("Enter dialogue first.")
        else:
            audit = question_response_audit(beats, lookahead)
            if not audit:
                st.info("No question marks were detected.")
            else:
                df = pd.DataFrame(audit)
                st.dataframe(df, use_container_width=True)
                st.caption(
                    "The next eligible speaker turn is a candidate response, not a guaranteed answer. "
                    "Lexical similarity cannot determine whether a question was pragmatically answered."
                )

# =============================================================================
# MODULE 5 — TURNING POINT CANDIDATES
# =============================================================================

elif selected_module == MODULES[4]:
    st.header("Narrative Turning Point Candidates")
    corpus = get_corpus_input("Enter a narrative or dramatic scene:", "turning_corpus")
    if st.button("⚡ Detect Observable Changes", key="turning"):
        results = analyze_corpus(corpus)
        if len(results) < 3:
            st.warning("At least three turns are recommended for robust descriptive comparisons.")
        else:
            lengths = pd.DataFrame({
                "Word Count": [r["words"] for r in results],
            }, index=[f"Beat {r['beat']}" for r in results])
            st.line_chart(lengths)
            candidates = turning_point_candidates(results)
            if candidates:
                st.dataframe(pd.DataFrame(candidates), use_container_width=True)
            else:
                st.info("No candidate flags were generated by the current descriptive rules.")
            st.caption(
                "These flags identify observable deviations (turn length, explicit pauses, "
                "question form, marker co-occurrence). They are not validated narrative-turning-point predictions."
            )

# =============================================================================
# MODULE 6 — XAI AUDITOR
# =============================================================================

elif selected_module == MODULES[5]:
    st.header("Explainable Analysis Auditor")
    target = st.text_area("Enter a dialogue line or passage:", key="xai_input", height=160)
    if st.button("⚡ Execute Evidence Audit", key="xai"):
        if not target.strip():
            st.warning("Enter text first.")
        else:
            result = classify_text(target)
            st.subheader("Classification")
            st.write("Primary display label:", result["category"])
            st.write("All detected labels:", ", ".join(result["labels"]))
            st.subheader("Evidence trace")
            rows = []
            for label, evidence in result["evidence"].items():
                rows.append({
                    "Category": label,
                    "Positive evidence": ", ".join(evidence["positive"]) or "None",
                    "Negated-context matches": ", ".join(evidence["negated"]) or "None",
                })
            st.dataframe(pd.DataFrame(rows), use_container_width=True)
            st.subheader("Decision method")
            st.write(result["method"])
            st.subheader("Known uncertainty")
            for limitation in result["limitations"]:
                st.write(f"- {limitation}")
            st.caption(
                "This is a rule trace, not model feature attribution, causal explanation, "
                "or a calibrated confidence estimate."
            )

# =============================================================================
# MODULE 7 — COMPARATIVE ANALYZER
# =============================================================================

elif selected_module == MODULES[6]:
    st.header("Comparative Dialogue Analyzer")
    col_a, col_b = st.columns(2)
    with col_a:
        corpus_a = st.text_area("Corpus A", key="compare_a", height=220)
    with col_b:
        corpus_b = st.text_area("Corpus B", key="compare_b", height=220)
    if st.button("⚡ Execute Comparison", key="compare"):
        a, b = analyze_corpus(corpus_a), analyze_corpus(corpus_b)
        if not a or not b:
            st.warning("Both corpora must contain text.")
        else:
            ma, mb = corpus_metrics(a), corpus_metrics(b)
            metrics = ["turns", "words", "average_words", "median_words", "speakers", "questions", "unique_words", "lexical_diversity"]
            rows = [{
                "Metric": m.replace("_", " ").title(),
                "Corpus A": ma[m],
                "Corpus B": mb[m],
                "Difference (B - A)": round(float(mb[m]) - float(ma[m]), 3),
            } for m in metrics]
            st.dataframe(pd.DataFrame(rows), use_container_width=True)
            ca, cb = Counter(label for r in a for label in r["labels"]), Counter(label for r in b for label in r["labels"])
            cat_df = pd.DataFrame({
                "Corpus A": [ca[x] for x in CATEGORIES],
                "Corpus B": [cb[x] for x in CATEGORIES],
            }, index=CATEGORIES)
            st.subheader("Multi-label marker frequency")
            st.bar_chart(cat_df)
            st.caption("Raw counts are affected by corpus length. For fair comparison, also inspect rates per 100 turns or per 100 words.")

# =============================================================================
# MODULE 8 — HYPOTHETICAL BRANCHING
# =============================================================================

elif selected_module == MODULES[7]:
    st.header("Rule-Based Branching Demonstrator")
    corpus = get_corpus_input("Enter original dialogue:", "branch_corpus")
    intervention = st.text_area("Enter a possible new character line:", key="branch_intervention")
    branch_type = st.selectbox(
        "Choose a hypothetical narrative direction",
        ["Boundary / disengagement", "Confrontation", "Disclosure / reconciliation"],
    )
    if st.button("⚡ Generate Hypothetical Branch", key="branch"):
        original = analyze_corpus(corpus)
        if not original or not intervention.strip():
            st.warning("Provide both original dialogue and an intervention.")
        else:
            intervention_result = classify_text(intervention)
            st.subheader("Intervention evidence")
            st.write("Detected labels:", ", ".join(intervention_result["labels"]))
            st.write("Primary display label:", intervention_result["category"])
            descriptions = {
                "Boundary / disengagement": "A possible continuation in which a character limits further engagement.",
                "Confrontation": "A possible continuation in which disagreement becomes more explicit.",
                "Disclosure / reconciliation": "A possible continuation in which a character shares information or attempts repair.",
            }
            st.markdown(
                f"<div class='context-box'><b>Hypothetical branch:</b> {safe_html(branch_type)}<br><br>{safe_html(descriptions[branch_type])}<br><br><b>Suggested next analytical question:</b> What new evidence in the next turns would support or contradict this trajectory?</div>",
                unsafe_allow_html=True,
            )
            st.warning(
                "This module generates a narrative prompt, not a numerical forecast. "
                "The selected branch is a researcher-defined scenario, not a prediction."
            )

# =============================================================================
# MODULE 9 — THEORETICAL MARKERS
# =============================================================================

elif selected_module == MODULES[8]:
    st.header("Theoretical Marker Index")
    corpus = get_corpus_input("Enter text for theoretical marker analysis:", "theory_corpus")
    if st.button("⚡ Calculate Lexical Proxies", key="theory"):
        if not tokenize(corpus):
            st.warning("Enter text first.")
        else:
            df = pd.DataFrame(theoretical_markers(corpus))
            st.dataframe(df, use_container_width=True)
            st.bar_chart(df.set_index("Framework (operational proxy)")["Density per 100 tokens"])
            st.caption(
                "Sartre, Lacan and Foucault's concepts cannot be reduced to word lists. "
                "These are transparent lexical proxies requiring theoretical interpretation."
            )

# =============================================================================
# MODULE 10 — VALIDATION
# =============================================================================

elif selected_module == MODULES[9]:
    st.header("Validation Protocol & Human Annotation")
    st.markdown(
        "Annotate each turn independently. Do not use the engine's label as the answer key. "
        "For a stronger study, blind annotators to engine outputs and provide written annotation guidelines."
    )
    corpus = get_corpus_input("Enter a pilot corpus:", "validation_corpus")
    if st.button("⚡ Prepare Annotation Sheet", key="validation"):
        results = analyze_corpus(corpus)
        if not results:
            st.warning("Enter a corpus first.")
        else:
            st.session_state["validation_items"] = results
            st.session_state["validation_annotations"] = {
                r["beat"]: {"Annotator A": None, "Annotator B": None} for r in results
            }

    items = st.session_state.get("validation_items", [])
    if items:
        st.subheader("Independent annotation")
        with st.form("annotation_form"):
            annotation_rows = []
            for r in items:
                st.markdown(f"**Beat {r['beat']} — {safe_html(r['text'])}**")
                c1, c2 = st.columns(2)
                with c1:
                    ann_a = st.selectbox(
                        f"Annotator A — Beat {r['beat']}",
                        ["— Not annotated —"] + CATEGORIES,
                        key=f"v2_a_{r['beat']}",
                    )
                with c2:
                    ann_b = st.selectbox(
                        f"Annotator B — Beat {r['beat']}",
                        ["— Not annotated —"] + CATEGORIES,
                        key=f"v2_b_{r['beat']}",
                    )
                annotation_rows.append({
                    "Beat": r["beat"], "Text": r["text"], "Engine": r["category"],
                    "Annotator A": None if ann_a.startswith("—") else ann_a,
                    "Annotator B": None if ann_b.startswith("—") else ann_b,
                })
            submitted = st.form_submit_button("Save annotations and calculate reliability")
        if submitted:
            df = pd.DataFrame(annotation_rows)
            st.session_state["validation_df"] = df
            st.success("Annotations saved for this session.")

    df = st.session_state.get("validation_df")
    if df is not None and not df.empty:
        summary = validation_summary(df)
        if summary:
            st.subheader("Inter-annotator reliability")
            c1, c2, c3 = st.columns(3)
            c1.metric("Complete double-coded turns", summary["n"])
            c2.metric("Observed agreement", f"{summary['agreement'] * 100:.1f}%")
            c3.metric("Cohen's kappa", f"{summary['cohen_kappa']:.3f}" if summary["cohen_kappa"] is not None else "Undefined")
            alpha = summary["krippendorff_alpha_nominal"]
            st.metric("Krippendorff's alpha (nominal)", f"{alpha:.3f}" if alpha is not None else "Undefined")
            st.caption("Alpha is computed for two complete nominal annotations per included unit. Small or highly imbalanced samples can make reliability estimates unstable.")
        st.subheader("Engine agreement with each annotator")
        for annotator in ["Annotator A", "Annotator B"]:
            m = engine_vs_annotator_metrics(df["Engine"].tolist(), df[annotator].tolist())
            if m:
                st.write(f"**{annotator}** — n={m['n']}, accuracy={m['accuracy']:.3f}, macro-F1={m['macro_f1']:.3f}, macro-precision={m['macro_precision']:.3f}, macro-recall={m['macro_recall']:.3f}")
        st.dataframe(df, use_container_width=True)
        st.download_button(
            "⬇️ Download annotations CSV",
            df.to_csv(index=False).encode("utf-8-sig"),
            "human_annotations.csv",
            "text/csv",
        )
    else:
        st.info("Prepare an annotation sheet and submit at least one complete annotation pair to calculate reliability.")

# =============================================================================
# MODULE 11 — REPORT & LIMITATIONS
# =============================================================================

elif selected_module == MODULES[10]:
    st.header("Core Artifact & Methodological Report")
    corpus = get_corpus_input("Enter corpus for report generation:", "artifact_corpus")
    if st.button("⚡ Generate Research Report", key="artifact"):
        results = analyze_corpus(corpus)
        if not results:
            st.warning("No corpus available.")
        else:
            metrics = corpus_metrics(results)
            corpus_hash = hashlib.sha256(corpus.encode("utf-8")).hexdigest()
            report = {
                "App version": APP_VERSION,
                "Generated at": dt.datetime.now().isoformat(timespec="seconds"),
                "Corpus SHA-256": corpus_hash,
                "Turns": metrics["turns"],
                "Words": metrics["words"],
                "Speakers": metrics["speakers"],
                "Mean words per turn": metrics["average_words"],
                "Median words per turn": metrics["median_words"],
                "Questions": metrics["questions"],
                "Unique words": metrics["unique_words"],
                "Lexical diversity": metrics["lexical_diversity"],
                "Method": "Rule-assisted lexical and descriptive discourse analysis",
            }
            st.dataframe(pd.DataFrame(report.items(), columns=["Parameter", "Value"]), use_container_width=True)
            st.subheader("Limitations")
            limitations = [
                "No general-purpose contextual language model is used in this version.",
                "Lexicon and phrase patterns have not been empirically validated against a representative benchmark.",
                "Negation scope is approximate; complex syntax, irony, sarcasm and metaphor can be misclassified.",
                "TF-IDF similarity measures lexical overlap, not semantic equivalence or evasion.",
                "Question-response links are candidate links within a configurable turn window.",
                "Participation share is not interpersonal power or dominance.",
                "Theoretical marker densities are lexical proxies, not measurements of philosophical constructs.",
                "Turning-point flags are descriptive anomalies, not validated narrative predictions.",
                "Reliability metrics require independent annotators, clear guidelines and enough representative items.",
                "A strong validity claim requires held-out data, error analysis, baseline comparisons and replication.",
            ]
            for item in limitations:
                st.write(f"- {item}")
            st.download_button(
                "⬇️ Download report CSV",
                pd.DataFrame(report.items(), columns=["Parameter", "Value"]).to_csv(index=False).encode("utf-8-sig"),
                "ontological_silence_research_report.csv",
                "text/csv",
            )
            st.download_button(
                "⬇️ Download beat-level analysis CSV",
                pd.DataFrame(results).to_csv(index=False).encode("utf-8-sig"),
                "beat_level_analysis.csv",
                "text/csv",
            )
            st.download_button(
                "⬇️ Download machine-readable JSON",
                json.dumps({"report": report, "results": results}, ensure_ascii=False, indent=2).encode("utf-8"),
                "ontological_silence_analysis.json",
                "application/json",
            )

st.divider()
st.markdown(
    f"<p style='text-align:center;color:#8b949e;font-size:11px;'>"
    f"ONTOLOGICAL SILENCE & PARANOIA ENGINE | RESEARCH PROTOTYPE V{APP_VERSION} | AGIL CHIRAGLI"
    f"</p>",
    unsafe_allow_html=True,
)
'''

requirements = """streamlit>=1.35
pandas>=2.0
numpy>=1.24
scikit-learn>=1.3
plotly>=5.18
"""

readme = """# Ontological Silence & Paranoia Engine — V2

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run app.py
```

## What changed in V2

- Multi-label lexical/phrase indicators instead of one exclusive label.
- Approximate negation handling; negated matches are shown separately.
- TF-IDF lexical similarity is explicitly not called evasion or semantic understanding.
- Speaker participation is reported as turn share and word share, not dominance.
- Question-response tracker reports candidate responses and requires human review.
- Turning-point module reports observable anomalies rather than fabricated tension percentages.
- XAI reports rule evidence, not misleading feature-attribution scores.
- Validation includes observed agreement, Cohen's kappa, nominal Krippendorff's alpha, and engine-vs-annotator macro metrics.
- Exports CSV and JSON with corpus hash and app version.

## Scientific limitations

This is still a transparent rule-assisted baseline, not a general contextual language-understanding system.
It cannot reliably interpret all metaphors, irony, sarcasm, pragmatics, cultural references, or authorial intent.
No confidence probabilities are reported because the system is not trained and calibrated.
A research-grade validity claim requires a representative labelled dataset, written annotation guidelines,
independent annotators, held-out evaluation, error analysis, and comparison with appropriate baselines.

## Suggested next research stage

1. Build a pilot corpus with clear inclusion/exclusion criteria.
2. Write annotation guidelines and have at least two annotators label turns independently.
3. Keep a held-out test set that is not used to tune rules.
4. Report per-class precision, recall, F1, confusion matrices, agreement and uncertainty.
5. Compare this rule baseline with a supervised contextual classifier and human performance.
"""

# Basic smoke tests for the core functions
tests = r'''import unittest
from app import tokenize, parse_corpus, classify_text, analyze_corpus, corpus_metrics

class CoreSmokeTests(unittest.TestCase):
    def test_parse_speakers(self):
        beats = parse_corpus("Mia: Are you there?\nJohn: Yes.")
        self.assertEqual(len(beats), 2)
        self.assertEqual(beats[0]["speaker"], "Mia")

    def test_multi_label(self):
        result = classify_text("I am watching you and I will destroy the evidence.")
        self.assertIn("Surveillance / Control", result["labels"])
        self.assertIn("Aggression", result["labels"])

    def test_negation_is_separated(self):
        result = classify_text("I am not afraid.")
        self.assertIn("afraid", result["evidence"]["Emotional Withdrawal"]["negated"])

    def test_empty_corpus(self):
        self.assertEqual(analyze_corpus(" \n "), [])

    def test_metrics(self):
        results = analyze_corpus("Mia: Hello there.\nJohn: Hello.")
        metrics = corpus_metrics(results)
        self.assertEqual(metrics["turns"], 2)

if __name__ == "__main__":
    unittest.main()
'''

base = Path("/mnt/data/ontological_silence_v2")
base.mkdir(parents=True, exist_ok=True)
(base / "app.py").write_text(app_code, encoding="utf-8")
(base / "requirements.txt").write_text(requirements, encoding="utf-8")
(base / "README.md").write_text(readme, encoding="utf-8")
(base / "test_core.py").write_text(tests, encoding="utf-8")

zip_path = Path("/mnt/data/ontological_silence_v2.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for p in base.iterdir():
        z.write(p, arcname=f"ontological_silence_v2/{p.name}")

print("Created:", zip_path)
print("Files:", [p.name for p in base.iterdir()])
