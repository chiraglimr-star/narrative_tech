import re
import math
import html
import hashlib
import datetime
from collections import Counter, defaultdict

import pandas as pd
import streamlit as st

from sklearn.metrics import cohen_kappa_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =============================================================================
# 1. CONFIGURATION
# =============================================================================

st.set_page_config(
    page_title="Ontological Silence & Paranoia Engine",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

APP_VERSION = "4.0.0"

CATEGORIES = {
    "AGGRESSIVE": "Aggression",
    "SILENCE": "Silence / Void",
    "WITHDRAWAL": "Emotional Withdrawal",
    "DEFENSE": "Defensive Rationalization",
    "INQUIRY": "Direct Inquiry",
    "SURVEILLANCE": "Surveillance / Control",
    "LACK": "Lack / Absence",
    "BAD_FAITH": "Possible Bad-Faith Markers"
}

CLASS_COLORS = {
    "Silence / Void": "#f85149",
    "Aggression": "#ff7b72",
    "Emotional Withdrawal": "#bc8cff",
    "Defensive Rationalization": "#f0883e",
    "Direct Inquiry": "#58a6ff",
    "Surveillance / Control": "#d2a8ff",
    "Lack / Absence": "#79c0ff",
    "Possible Bad-Faith Markers": "#ffa657",
    "Dynamic Interaction": "#3fb950"
}

PRIMARY_PRIORITY = [
    "SILENCE",
    "AGGRESSIVE",
    "WITHDRAWAL",
    "DEFENSE",
    "INQUIRY",
    "SURVEILLANCE",
    "LACK",
    "BAD_FAITH"
]


# =============================================================================
# 2. LEXICAL RESOURCES
# =============================================================================

LEXICON = {
    "AGGRESSIVE": {
        "attack", "kill", "destroy", "threat", "force", "obey",
        "punish", "fight", "hate", "angry", "furious", "violent",
        "brutal", "cruel", "murder", "weapon", "enemy", "war",
        "shut", "order", "demand", "strike", "break", "revenge",
        "idiot", "stupid", "damn", "bomb", "gun", "knife",
        "threaten", "hurt", "harm", "beat", "dominate"
    },

    "SILENCE": {
        "silence", "quiet", "hush", "mute", "speechless",
        "wordless", "nothing", "empty", "void", "absence",
        "forgotten", "missing", "alone", "hollow", "abyss",
        "blank", "desolate", "abandoned", "death", "grave",
        "tomb", "funeral", "mourning", "still", "soundless"
    },

    "WITHDRAWAL": {
        "sad", "cry", "tears", "pain", "hurt", "fear",
        "afraid", "scared", "anxious", "broken", "lonely",
        "regret", "sorry", "goodbye", "leave", "depressed",
        "miserable", "unhappy", "sorrow", "grief", "miss",
        "memory", "longing", "nostalgia", "weak", "fragile",
        "helpless", "vulnerable", "tired", "exhausted",
        "heartbroken", "wounded", "ashamed", "worried"
    },

    "DEFENSE": {
        "truth", "reality", "reason", "logic", "because",
        "understand", "explain", "philosophy", "theory",
        "maybe", "perhaps", "could", "would", "might",
        "should", "pretend", "mask", "defend", "excuse",
        "justify", "rationalize", "deny", "avoid", "deflect",
        "distract", "divert", "escape", "everyone", "nobody",
        "always", "never", "analyze", "consider", "evaluate",
        "fair", "unfair", "just", "reasonable"
    },

    "INQUIRY": {
        "what", "where", "when", "who", "whom", "whose",
        "which", "why", "how", "ask", "question", "inquire",
        "wonder", "investigate", "examine", "interrogate",
        "challenge", "doubt", "suspect"
    },

    "SURVEILLANCE": {
        "watch", "watched", "watching", "observe", "observed",
        "monitor", "monitoring", "control", "surveillance",
        "record", "recording", "follow", "followed", "report",
        "authority", "power", "discipline", "prison", "camera",
        "guard", "inspect", "inspection", "obey", "institution",
        "tracked", "tracking", "supervise",
        "police", "calling", "call", "arrest", "court"
    },

    "LACK": {
        "empty", "nothing", "absence", "missing", "desire",
        "want", "need", "lost", "void", "alone", "lack",
        "silence", "incomplete", "unfulfilled", "absent",
        "longing", "unavailable"
    },

    "BAD_FAITH": {
        "pretend", "deny", "excuse", "justify", "rationalize",
        "avoid", "responsibility", "truth", "choice", "freedom",
        "cannot", "impossible", "forced", "duty", "must",
        "because", "perhaps", "maybe"
    }
}


STOP_WORDS = {
    "the", "and", "for", "but", "with", "from", "this",
    "that", "was", "were", "are", "has", "have", "had",
    "there", "here", "they", "them", "she", "him", "her",
    "its", "you", "your", "his", "our", "their", "then",
    "than", "into", "about", "just", "very", "been",
    "being", "will", "would", "could", "should", "does",
    "did", "not", "nor", "too", "can", "all", "some"
}

NEGATION_WORDS = {
    "not", "never", "no", "neither", "nor", "hardly",
    "without", "cannot", "can't", "dont", "don't",
    "doesnt", "doesn't", "didnt", "didn't"
}

SILENCE_PATTERNS = [
    r"\(\s*silence\s*\)",
    r"\[\s*silence\s*\]",
    r"\(\s*pause\s*\)",
    r"\[\s*pause\s*\]",
    r"\(\s*long pause\s*\)",
    r"\[\s*long pause\s*\]",
    r"\(\s*no response\s*\)",
    r"\[\s*no response\s*\]"
]


# =============================================================================
# 3. DESIGN SYSTEM
# =============================================================================

st.markdown("""
<style>
.stApp {
    background-color: #07090e;
    color: #f1f5f9;
    font-family: 'Courier New', monospace;
}
[data-testid="stSidebar"] {
    background-color: #0d1117;
    border-right: 1px solid #30363d;
}
[data-testid="stSidebar"] * {
    color: #c9d1d9;
}
h1, h2, h3, h4, label {
    color: #ffffff !important;
    font-family: 'Courier New', monospace !important;
}
.stTextArea textarea, .stTextInput input {
    background-color: #0d1117 !important;
    color: #58a6ff !important;
    border: 1px solid #30363d !important;
}
.stButton button {
    background-color: #f0883e !important;
    color: #07090e !important;
    font-weight: bold !important;
    border-radius: 5px;
}
.stButton button:hover {
    background-color: #ffa657 !important;
}
.lab-card {
    background: #0d1117;
    border: 1px solid #30363d;
    border-left: 4px solid #f0883e;
    padding: 17px;
    border-radius: 6px;
    margin-bottom: 12px;
}
.context-box {
    background: #0f1c2e;
    border: 1px solid #1f3864;
    padding: 16px;
    border-radius: 6px;
    margin-bottom: 15px;
}
.warning-terminal {
    background: #490202;
    border: 1px solid #86181d;
    padding: 16px;
    border-radius: 6px;
    margin-bottom: 12px;
}
[data-testid="stMetricValue"] {
    color: #f0883e !important;
}
small {
    color: #8b949e;
}
</style>
""", unsafe_allow_html=True)


# =============================================================================
# 4. TEXT PROCESSING
# =============================================================================

def tokenize(text):
    """
    Unicode-aware tokenizer.
    Preserves English letters and common apostrophe forms.
    """
    text = str(text).lower().replace("’", "'")
    return re.findall(r"[a-z]+(?:'[a-z]+)?", text)


def get_text_vector(text):
    return Counter(
        word for word in tokenize(text)
        if len(word) > 2 and word not in STOP_WORDS
    )


def cosine_similarity_native(v1, v2):
    common = set(v1) & set(v2)

    numerator = sum(v1[w] * v2[w] for w in common)

    denominator = (
        math.sqrt(sum(v ** 2 for v in v1.values())) *
        math.sqrt(sum(v ** 2 for v in v2.values()))
    )

    return numerator / denominator if denominator else 0.0


def semantic_divergence(text_a, text_b):
    """
    TF-IDF lexical similarity proxy.
    This is NOT semantic understanding.
    """
    if not text_a.strip() or not text_b.strip():
        return 0.0, 0.0

    try:
        vectorizer = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            stop_words="english"
        )

        matrix = vectorizer.fit_transform([text_a, text_b])

        similarity = float(
            cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
        )

        return similarity, 1.0 - similarity

    except ValueError:
        return 0.0, 1.0


def has_explicit_silence(text):
    lower = text.lower()

    return any(
        re.search(pattern, lower)
        for pattern in SILENCE_PATTERNS
    )


def is_negated(tokens, index, window=2):
    """
    Approximate local negation scope.

    This is a heuristic. It does not perform full syntactic parsing.
    """
    start = max(0, index - window)
    previous = tokens[start:index]

    return any(
        token in NEGATION_WORDS
        for token in previous
    )


def matched_evidence(text, category):
    tokens = tokenize(text)
    matches = []

    for i, token in enumerate(tokens):
        if token in LEXICON[category]:
            negated = is_negated(tokens, i)
            
            # "No choice" is a classic Sartrean bad-faith expression.
            # Do not treat the noun as negated.
            if category == "BAD_FAITH" and token in {"choice", "freedom", "responsibility"}:
                if negated and any(t in {"no", "without"} for t in tokens[max(0, i-2):i]):
                    negated = False

            matches.append({
                "term": token,
                "negated": negated
            })

    return matches


def matched_words(text, category):
    return sorted({
        item["term"]
        for item in matched_evidence(text, category)
    })


def classify_text(text):
    """
    Multi-label lexical classification.

    A turn can contain multiple categories.
    The primary category is selected only for visualization
    and single-label validation.
    """
    tokens = tokenize(text)

    evidence = {}
    active_categories = []

    for category in LEXICON:
        matches = matched_evidence(text, category)

        positive = [
            item["term"]
            for item in matches
            if not item["negated"]
        ]

        negated = [
            item["term"]
            for item in matches
            if item["negated"]
        ]

        evidence[category] = {
            "positive": sorted(set(positive)),
            "negated": sorted(set(negated))
        }

        if positive:
            active_categories.append(category)

    explicit_silence = has_explicit_silence(text)

    if explicit_silence and "SILENCE" not in active_categories:
        active_categories.append("SILENCE")

    if "?" in text and "INQUIRY" not in active_categories:
        active_categories.append("INQUIRY")

    if active_categories:
        # Primary = category with the most positive matches,
        # with PRIMARY_PRIORITY as tie-breaker.
        def _priority_key(cat):
            count = len(evidence[cat]["positive"])
            prio = PRIMARY_PRIORITY.index(cat) if cat in PRIMARY_PRIORITY else 99
            return (-count, prio)

        primary = sorted(active_categories, key=_priority_key)[0]
        category_name = CATEGORIES[primary]
    else:
        primary = "DYNAMIC"
        category_name = "Dynamic Interaction"

    all_evidence = {
        CATEGORIES[category]: evidence[category]["positive"]
        for category in LEXICON
        if evidence[category]["positive"]
    }

    return {
        "category": category_name,
        "primary_category": primary,
        "categories": [
            CATEGORIES[c] for c in active_categories
        ],
        "evidence": evidence,
        "all_evidence": all_evidence,
        "silence": evidence["SILENCE"]["positive"],
        "aggressive": evidence["AGGRESSIVE"]["positive"],
        "withdrawal": evidence["WITHDRAWAL"]["positive"],
        "defense": evidence["DEFENSE"]["positive"],
        "inquiry": evidence["INQUIRY"]["positive"],
        "surveillance": evidence["SURVEILLANCE"]["positive"],
        "lack": evidence["LACK"]["positive"],
        "bad_faith": evidence["BAD_FAITH"]["positive"],
        "negated_evidence": {
            CATEGORIES[c]: evidence[c]["negated"]
            for c in LEXICON
            if evidence[c]["negated"]
        },
        "color": CLASS_COLORS.get(
            category_name,
            CLASS_COLORS["Dynamic Interaction"]
        )
    }


# =============================================================================
# 5. CORPUS PARSING
# =============================================================================

def parse_corpus(text):
    parsed = []

    for raw_line in str(text).splitlines():
        line = raw_line.strip()

        if not line:
            continue

        match = re.match(
            r"^([A-Za-z][A-Za-z0-9 _.'-]{0,39}):\s*(.*)$",
            line
        )

        if match:
            speaker = match.group(1).strip()
            dialogue = match.group(2).strip()
        else:
            speaker = "Unspecified Speaker"
            dialogue = line.lstrip("-").strip()

        if not dialogue:
            continue

        parsed.append({
            "beat": len(parsed) + 1,
            "speaker": speaker,
            "text": dialogue,
            "original": line
        })

    return parsed


# =============================================================================
# 6. HEURISTIC INDICATORS
# =============================================================================

def calculate_compression(current_count, previous_count):
    """
    Measures change in word count between consecutive turns
    by the same speaker.

    It does not establish psychological withdrawal.
    """
    if previous_count is None or previous_count == 0:
        return 0.0

    return max(
        0.0,
        (previous_count - current_count) / previous_count
    )


def calculate_tension_index(classification, divergence, compression, question_count):
    """
    Transparent heuristic index.

    Components are equally weighted and normalized.
    It is not a probability, diagnosis, or validated psychological scale.
    """
    active_count = len(classification["categories"])

    category_component = min(active_count / 4.0, 1.0)
    divergence_component = max(0.0, min(1.0, divergence))
    compression_component = max(0.0, min(1.0, compression))
    question_component = min(question_count / 3.0, 1.0)

    components = {
        "lexical_category_density": category_component,
        "lexical_divergence": divergence_component,
        "intra_speaker_compression": compression_component,
        "question_density": question_component
    }

    score = sum(components.values()) / len(components) * 100

    return round(score, 1), components


def analyze_corpus(corpus):
    beats = parse_corpus(corpus)

    if not beats:
        return []

    previous_speaker_words = {}
    results = []

    for i, beat in enumerate(beats):
        text = beat["text"]
        speaker = beat["speaker"]

        tokens = tokenize(text)
        word_count = len(tokens)

        previous_count = previous_speaker_words.get(speaker)

        compression = calculate_compression(
            word_count,
            previous_count
        )

        previous_speaker_words[speaker] = word_count

        if i > 0:
            previous = beats[i - 1]

            similarity, divergence = semantic_divergence(
                previous["text"],
                text
            )

            same_speaker = previous["speaker"] == speaker
        else:
            similarity = 0.0
            divergence = 0.0
            same_speaker = False

        classification = classify_text(text)

        question_count = text.count("?")

        tension, tension_components = calculate_tension_index(
            classification,
            divergence,
            compression,
            question_count
        )

        results.append({
            **beat,
            **classification,
            "words": word_count,
            "questions": question_count,
            "lexical_similarity": round(similarity, 3),
            "lexical_divergence": round(divergence, 3),
            "same_speaker_as_previous": same_speaker,
            "compression": round(compression, 3),
            "tension_index": tension,
            "tension_components": tension_components
        })

    return results


# =============================================================================
# 7. CORPUS METRICS
# =============================================================================

def corpus_metrics(results):
    if not results:
        return {}

    total_words = sum(r["words"] for r in results)
    total_turns = len(results)

    tension_values = [
        r["tension_index"] for r in results
    ]

    all_tokens = [
        word
        for r in results
        for word in tokenize(r["text"])
    ]

    return {
        "turns": total_turns,
        "words": total_words,
        "average_words": round(total_words / total_turns, 2),
        "average_tension_index": round(
            sum(tension_values) / len(tension_values), 2
        ),
        "maximum_tension_index": max(tension_values),
        "minimum_tension_index": min(tension_values),
        "questions": sum(r["questions"] for r in results),
        "speakers": len(set(r["speaker"] for r in results)),
        "unique_words": len(set(all_tokens)),
        "lexical_diversity": round(
            len(set(all_tokens)) / len(all_tokens), 3
        ) if all_tokens else 0
    }


def category_distribution(results):
    counts = Counter()

    for result in results:
        for category in result["categories"]:
            counts[category] += 1

    return counts


def safe_html(value):
    return html.escape(str(value))


# =============================================================================
# 8. VISUALIZATION HELPERS
# =============================================================================

def show_analysis_cards(results):
    for r in results:
        categories = (
            ", ".join(r["categories"])
            if r["categories"]
            else "Dynamic Interaction"
        )

        evidence = []

        for category, words in r["all_evidence"].items():
            if words:
                evidence.append(
                    f"{category}: {', '.join(words)}"
                )

        evidence_text = (
            " | ".join(evidence)
            if evidence
            else "No category-specific lexical match"
        )

        st.markdown(
            f"""
            <div class="lab-card"
                 style="border-left-color:{r['color']}">
                <b>Beat {r['beat']} | {safe_html(r['speaker'])}</b>
                <br><br>
                <i style="color:#58a6ff">
                    "{safe_html(r['text'])}"
                </i>
                <br><br>
                <b>Primary classification:</b>
                {safe_html(r['category'])}<br>
                <b>All detected categories:</b>
                {safe_html(categories)}<br>
                <b>Heuristic tension index:</b>
                {r['tension_index']}/100<br>
                <b>Lexical divergence proxy:</b>
                {r['lexical_divergence']}<br>
                <b>Intra-speaker compression:</b>
                {r['compression']}<br>
                <b>Word count:</b> {r['words']}<br>
                <b>Evidence:</b> {safe_html(evidence_text)}
            </div>
            """,
            unsafe_allow_html=True
        )


def get_corpus_input(label, key, height=220):
    return st.text_area(
        label,
        key=key,
        height=height,
        placeholder=(
            "Enter your dialogue here...\n"
            "Character A: What happened?\n"
            "Character B: I don't know."
        )
    )


def results_dataframe(results):
    rows = []

    for r in results:
        rows.append({
            "Beat": r["beat"],
            "Speaker": r["speaker"],
            "Text": r["text"],
            "Primary Category": r["category"],
            "All Categories": "; ".join(r["categories"]),
            "Words": r["words"],
            "Questions": r["questions"],
            "Tension Index": r["tension_index"],
            "Lexical Similarity": r["lexical_similarity"],
            "Lexical Divergence": r["lexical_divergence"],
            "Compression": r["compression"]
        })

    return pd.DataFrame(rows)


def show_method_warning():
    st.caption(
        "Methodological note: all indicators are heuristic textual "
        "features. They do not establish intention, emotion, deception, "
        "psychological state, or actual interpersonal power."
    )


# =============================================================================
# 9. SIDEBAR
# =============================================================================

with st.sidebar:
    st.markdown("### 👁️ Terminal Control")
    st.caption("Computational Dramaturgy Lab | Research Prototype")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏛️ Research Framework",
            "💬 Universal NLP Scene Analyzer",
            "🕸️ Character Relationship & Power Map",
            "❓ Unanswered Question Tracker",
            "📈 Narrative Turning Point Detector",
            "🔍 Explainable Analysis (XAI)",
            "⚖️ Comparative Dialogue Analyzer",
            "🔄 Rule-Based Branching Demonstrator",
            "⚛️ Dynamic Theoretical Marker Index",
            "📊 Validation Protocol",
            "📜 Core Artifact & Limitations"
        ]
    )

    st.divider()

    st.markdown("### ⚙️ Analysis Settings")

    st.caption(
        "The current model is deterministic and lexicon-based. "
        "These settings do not train a machine-learning model."
    )

    st.markdown("### Research Metadata")
    st.write("Version:", APP_VERSION)
    st.write("Framework:", "Rule-based NLP")
    st.write("Classification:", "Multi-label lexical")
    st.write("Similarity:", "TF-IDF proxy")

    st.divider()

    st.markdown("**Framework Architect:** Agil Chiragli")
    st.markdown("**Research Prototype:** Independent")
    st.caption(datetime.date.today().isoformat())


# =============================================================================
# 10. MODULE 1: RESEARCH FRAMEWORK
# =============================================================================

if selected_module == "🏛️ Research Framework":

    st.title("👁️ Ontological Silence & Paranoia Engine")

    st.markdown(
        "### A Dynamic Computational Framework for Narrative "
        "Silence, Psychological Withdrawal and Conversational Power"
    )

    st.markdown("""
    <div class="context-box">
    <b>RESEARCH ARCHITECTURE</b><br><br>
    This platform applies transparent computational methods
    to dramatic dialogue and narrative text.

    It identifies lexical patterns, speaker participation,
    local textual divergence, response candidates and
    potential narrative transitions.

    Outputs are exploratory indicators that require
    contextual interpretation and empirical validation.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Research Objectives")

    objectives = [
        (
            "Quantifying Subtext",
            "Identifying lexical indicators associated with silence, "
            "withdrawal, absence and evasion."
        ),
        (
            "Conversational Power",
            "Describing speaker participation, turn distribution "
            "and lexical volume."
        ),
        (
            "Narrative Dynamics",
            "Detecting changes in heuristic textual indicators "
            "and potential structural turning points."
        ),
        (
            "Explainable Analysis",
            "Displaying the lexical evidence and decision rules "
            "behind each classification."
        ),
        (
            "Theoretical Mapping",
            "Exploring lexical proxies associated with selected "
            "concepts from Sartre, Lacan and Foucault."
        ),
        (
            "Empirical Validation",
            "Providing a workspace for human annotation and "
            "inter-annotator reliability analysis."
        )
    ]

    for title, description in objectives:
        st.markdown(
            f"""
            <div class="lab-card">
                <b>{title}</b><br>
                {description}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("Analytical Pipeline")

    st.code(
        "Input Text\n"
        "    ↓\n"
        "Dialogue Parsing\n"
        "    ↓\n"
        "Tokenization and Lexical Evidence\n"
        "    ↓\n"
        "Multi-label Classification\n"
        "    ↓\n"
        "Speaker and Turn-Level Features\n"
        "    ↓\n"
        "Heuristic Indicators\n"
        "    ↓\n"
        "XAI / Validation / Export",
        language="text"
    )

    st.warning(
        "This system does not infer psychological states, "
        "intentions, deception or truth. Its scores are not "
        "validated psychological measurements."
    )


# =============================================================================
# 11. MODULE 2: UNIVERSAL NLP SCENE ANALYZER
# =============================================================================

elif selected_module == "💬 Universal NLP Scene Analyzer":

    st.title("💬 Universal NLP Scene Analyzer")

    corpus = get_corpus_input(
        "Enter dialogue, scene or narrative text:",
        "xray_corpus"
    )

    if st.button("⚡ Execute Universal X-Ray", key="xray"):

        results = analyze_corpus(corpus)

        if not results:
            st.warning("Enter text before executing the analysis.")

        else:
            st.session_state["last_results"] = results
            st.session_state["last_corpus"] = corpus

            metrics = corpus_metrics(results)

            st.divider()
            st.subheader("Dynamic Diagnostic Results")

            c1, c2, c3, c4 = st.columns(4)

            c1.metric("Beats", metrics["turns"])
            c2.metric("Words", metrics["words"])
            c3.metric(
                "Mean Tension Index",
                metrics["average_tension_index"]
            )
            c4.metric("Speakers", metrics["speakers"])

            st.subheader("Beat-by-Beat Analysis")
            show_analysis_cards(results)

            st.subheader("Heuristic Tension Trajectory")

            tension_df = pd.DataFrame({
                "Tension Index": [
                    r["tension_index"] for r in results
                ]
            }, index=[
                f"Beat {r['beat']}" for r in results
            ])

            st.line_chart(tension_df)

            st.subheader("Multi-label Category Distribution")

            distribution = category_distribution(results)

            if distribution:
                st.bar_chart(
                    pd.DataFrame.from_dict(
                        distribution,
                        orient="index",
                        columns=["Frequency"]
                    )
                )
            else:
                st.info("No lexical category matches detected.")

            st.subheader("Corpus Statistics")

            st.dataframe(
                pd.DataFrame([metrics]),
                use_container_width=True
            )

            st.download_button(
                "⬇️ Download Beat-Level Analysis",
                data=results_dataframe(results).to_csv(
                    index=False
                ).encode("utf-8-sig"),
                file_name="beat_level_analysis.csv",
                mime="text/csv"
            )

            show_method_warning()


# =============================================================================
# 12. MODULE 3: CHARACTER RELATIONSHIP & POWER MAP
# =============================================================================

elif selected_module == "🕸️ Character Relationship & Power Map":

    st.title("🕸️ Character Relationship & Power Map")

    corpus = get_corpus_input(
        "Enter character dialogue:",
        "power_corpus"
    )

    if st.button("⚡ Generate Participation Map", key="power"):

        results = analyze_corpus(corpus)

        if not results:
            st.warning("No dialogue detected.")

        else:
            stats = defaultdict(lambda: {
                "turns": 0,
                "words": 0,
                "questions": 0,
                "tension": [],
                "defense": 0,
                "aggression": 0,
                "silence": 0
            })

            for r in results:
                s = stats[r["speaker"]]

                s["turns"] += 1
                s["words"] += r["words"]
                s["questions"] += r["questions"]
                s["tension"].append(r["tension_index"])
                s["defense"] += len(r["defense"])
                s["aggression"] += len(r["aggressive"])
                s["silence"] += len(r["silence"])

            total_turns = len(results)
            total_words = sum(r["words"] for r in results)

            rows = []

            for speaker, s in stats.items():

                turn_share = s["turns"] / total_turns * 100

                word_share = (
                    s["words"] / total_words * 100
                    if total_words else 0
                )

                participation_index = (
                    turn_share + word_share
                ) / 2

                rows.append({
                    "Speaker": speaker,
                    "Turns": s["turns"],
                    "Words": s["words"],
                    "Turn Share (%)": round(turn_share, 2),
                    "Word Share (%)": round(word_share, 2),
                    "Participation Index (%)": round(
                        participation_index, 2
                    ),
                    "Questions": s["questions"],
                    "Defensive Markers": s["defense"],
                    "Aggressive Markers": s["aggression"],
                    "Silence Markers": s["silence"],
                    "Mean Tension Index": round(
                        sum(s["tension"]) / len(s["tension"]), 2
                    )
                })

            df = pd.DataFrame(rows).sort_values(
                "Participation Index (%)",
                ascending=False
            )

            st.subheader("Speaker Participation Matrix")
            st.dataframe(df, use_container_width=True)

            st.subheader("Conversational Participation")

            st.bar_chart(
                df.set_index("Speaker")[
                    ["Turn Share (%)", "Word Share (%)"]
                ]
            )

            st.subheader("Participation Index")

            st.bar_chart(
                df.set_index("Speaker")[
                    ["Participation Index (%)"]
                ]
            )

            highest = df.iloc[0]

            st.markdown(
                f"""
                <div class="context-box">
                <b>Highest Linguistic Participation:</b>
                {safe_html(highest["Speaker"])}<br>
                <b>Participation Index:</b>
                {highest["Participation Index (%)"]}%<br><br>
                This speaker has the highest combined share
                of conversational turns and lexical volume.
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption(
                "Participation is not equivalent to dominance, "
                "social authority, coercive power or narrative control."
            )

            st.download_button(
                "⬇️ Download Participation Data",
                data=df.to_csv(index=False).encode("utf-8-sig"),
                file_name="speaker_participation.csv",
                mime="text/csv"
            )


# =============================================================================
# 13. MODULE 4: UNANSWERED QUESTION TRACKER
# =============================================================================

elif selected_module == "❓ Unanswered Question Tracker":

    st.title("❓ Unanswered Question & Response Audit")

    corpus = get_corpus_input(
        "Enter dialogue for question-response analysis:",
        "question_corpus"
    )

    if st.button("⚡ Audit Questions", key="questions"):

        beats = parse_corpus(corpus)

        if not beats:
            st.warning("Enter dialogue first.")

        else:
            audit = []

            for i, beat in enumerate(beats):

                if "?" not in beat["text"]:
                    continue

                response = None

                if i + 1 < len(beats):
                    candidate = beats[i + 1]

                    if candidate["speaker"] != beat["speaker"]:
                        response = candidate

                if response is None:
                    status = "No immediate response candidate"
                    similarity = 0.0
                    evidence = []
                    score = 0
                else:
                    response_class = classify_text(response["text"])

                    similarity, divergence = semantic_divergence(
                        beat["text"],
                        response["text"]
                    )

                    evidence = []

                    for category, words in response_class[
                        "all_evidence"
                    ].items():
                        evidence.extend(words)

                    if has_explicit_silence(response["text"]):
                        status = "Explicit silence marker"
                    elif response_class["defense"]:
                        status = "Possible defensive-language marker"
                    elif response_class["withdrawal"]:
                        status = "Possible withdrawal-language marker"
                    elif similarity >= 0.25:
                        status = "Lexically related response candidate"
                    else:
                        status = "Response relevance requires review"

                    score = round(similarity * 100, 1)

                audit.append({
                    "Question Speaker": beat["speaker"],
                    "Question": beat["text"],
                    "Response Speaker": (
                        response["speaker"] if response else "None"
                    ),
                    "Response Candidate": (
                        response["text"] if response else "None"
                    ),
                    "Lexical Similarity (%)": score,
                    "Status": status,
                    "Lexical Evidence": ", ".join(sorted(set(evidence)))
                })

            if not audit:
                st.info("No question marks were detected.")

            else:
                df = pd.DataFrame(audit)

                st.subheader("Question-Response Audit")
                st.dataframe(df, use_container_width=True)

                st.subheader("Candidate Response Similarity")

                chart_df = df[
                    ["Question Speaker", "Lexical Similarity (%)"]
                ].copy()

                chart_df.index = [
                    f"Question {i + 1}"
                    for i in range(len(chart_df))
                ]

                st.bar_chart(
                    chart_df["Lexical Similarity (%)"]
                )

                unresolved = sum(
                    x["Status"] in {
                        "No immediate response candidate",
                        "Explicit silence marker",
                        "Response relevance requires review"
                    }
                    for x in audit
                )

                st.metric(
                    "Questions Requiring Human Review",
                    unresolved
                )

                st.download_button(
                    "⬇️ Download Question Audit",
                    data=df.to_csv(
                        index=False
                    ).encode("utf-8-sig"),
                    file_name="question_response_audit.csv",
                    mime="text/csv"
                )

                st.caption(
                    "Lexical similarity does not establish whether "
                    "a response answers a question. Human contextual "
                    "review is necessary."
                )


# =============================================================================
# 14. MODULE 5: TURNING POINT DETECTOR
# =============================================================================

elif selected_module == "📈 Narrative Turning Point Detector":

    st.title("📈 Narrative Turning Point Detector")

    corpus = get_corpus_input(
        "Enter a narrative or dramatic scene:",
        "turning_corpus"
    )

    if st.button("⚡ Detect Turning Points", key="turning"):

        results = analyze_corpus(corpus)

        if len(results) < 2:
            st.warning("At least two dialogue beats are required.")

        else:
            tensions = [
                r["tension_index"] for r in results
            ]

            mean_tension = sum(tensions) / len(tensions)

            points = []

            for i, r in enumerate(results):

                previous = (
                    tensions[i - 1]
                    if i > 0
                    else tensions[i]
                )

                following = (
                    tensions[i + 1]
                    if i < len(tensions) - 1
                    else tensions[i]
                )

                change = r["tension_index"] - previous

                if r["tension_index"] >= mean_tension + 20:
                    label = "Elevated Heuristic Index"
                    significance = (
                        "This beat has an index notably above "
                        "the corpus mean."
                    )

                elif change >= 20:
                    label = "Potential Escalation"
                    significance = (
                        "A notable increase in the heuristic index."
                    )

                elif change <= -20:
                    label = "Potential De-escalation"
                    significance = (
                        "A notable decrease in the heuristic index."
                    )

                elif (
                    r["tension_index"] >= previous
                    and r["tension_index"] >= following
                ):
                    label = "Potential Local Apex"
                    significance = (
                        "A local maximum in the heuristic sequence."
                    )

                else:
                    label = "Structural Continuation"
                    significance = (
                        "No large local index shift detected."
                    )

                speaker_shift = (
                    i > 0
                    and results[i - 1]["speaker"] != r["speaker"]
                )

                points.append({
                    "Beat": r["beat"],
                    "Speaker": r["speaker"],
                    "Text": r["text"],
                    "Tension Index": r["tension_index"],
                    "Change": round(change, 2),
                    "Structural Label": label,
                    "Speaker Shift": speaker_shift,
                    "Interpretation": significance
                })

            st.subheader("Heuristic Trajectory")

            chart_df = pd.DataFrame({
                "Index": tensions
            }, index=[
                f"Beat {i + 1}"
                for i in range(len(tensions))
            ])

            st.line_chart(chart_df)

            st.subheader("Detected Structural Points")

            point_df = pd.DataFrame(points)

            st.dataframe(
                point_df,
                use_container_width=True
            )

            for p in points:
                if p["Structural Label"] != "Structural Continuation":
                    st.markdown(
                        f"""
                        <div class="lab-card">
                            <b>{p["Structural Label"]} |
                            Beat {p["Beat"]}</b><br>
                            <i>{safe_html(p["Text"])}</i><br><br>
                            <b>Index:</b> {p["Tension Index"]}<br>
                            <b>Change:</b> {p["Change"]}<br>
                            <b>Interpretation:</b>
                            {p["Interpretation"]}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            st.caption(
                "A turning-point candidate is a computational flag, "
                "not proof of a narrative turning point."
            )


# =============================================================================
# 15. MODULE 6: EXPLAINABLE ANALYSIS
# =============================================================================

elif selected_module == "🔍 Explainable Analysis (XAI)":

    st.title("🔍 Explainable Analysis Auditor")

    target = st.text_area(
        "Enter a dialogue line or narrative passage:",
        key="xai_input",
        height=150
    )

    if st.button("⚡ Execute XAI Audit", key="xai"):

        if not target.strip():
            st.warning("Enter text before running the audit.")

        else:
            classification = classify_text(target)

            attribution = []

            for category in LEXICON:

                evidence = matched_evidence(target, category)

                positive = [
                    x["term"] for x in evidence
                    if not x["negated"]
                ]

                negated = [
                    x["term"] for x in evidence
                    if x["negated"]
                ]

                attribution.append({
                    "Category": CATEGORIES[category],
                    "Positive Evidence": ", ".join(
                        sorted(set(positive))
                    ),
                    "Negated Evidence": ", ".join(
                        sorted(set(negated))
                    ),
                    "Positive Match Count": len(positive)
                })

            st.subheader("Classification Result")

            st.metric(
                "Primary Classification",
                classification["category"]
            )

            st.write(
                "**All detected categories:**",
                ", ".join(classification["categories"])
                if classification["categories"]
                else "None"
            )

            st.markdown(
                f"""
                <div class="context-box">
                    <b>Input:</b>
                    {safe_html(target)}<br><br>
                    <b>Primary classification:</b>
                    {safe_html(classification["category"])}<br>
                    <b>Positive lexical evidence:</b>
                    {safe_html(
                        str(classification["all_evidence"])
                    )}<br>
                    <b>Negated lexical evidence:</b>
                    {safe_html(
                        str(classification["negated_evidence"])
                    )}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.subheader("Category-Level Evidence")

            attribution_df = pd.DataFrame(attribution)

            st.dataframe(
                attribution_df,
                use_container_width=True
            )

            st.subheader("Decision Rule Trace")

            st.write(
                "**Explicit silence marker:**",
                has_explicit_silence(target)
            )

            st.write(
                "**Question mark detected:**",
                "?" in target
            )

            for category in LEXICON:
                evidence = classification["evidence"][category]

                st.write(
                    f"**{CATEGORIES[category]}**",
                    "Positive:",
                    ", ".join(evidence["positive"]) or "None",
                    "| Negated:",
                    ", ".join(evidence["negated"]) or "None"
                )

            st.caption(
                "This is a rule trace, not a causal explanation "
                "of human behaviour. Lexical evidence does not "
                "prove a character's intention."
            )


# =============================================================================
# 16. MODULE 7: COMPARATIVE ANALYZER
# =============================================================================

elif selected_module == "⚖️ Comparative Dialogue Analyzer":

    st.title("⚖️ Comparative Dialogue Analyzer")

    col_a, col_b = st.columns(2)

    with col_a:
        corpus_a = st.text_area(
            "Corpus A",
            key="compare_a",
            height=200
        )

    with col_b:
        corpus_b = st.text_area(
            "Corpus B",
            key="compare_b",
            height=200
        )

    if st.button("⚡ Execute Comparative Analysis", key="compare"):

        a = analyze_corpus(corpus_a)
        b = analyze_corpus(corpus_b)

        if not a or not b:
            st.warning("Both corpora must contain text.")

        else:
            ma = corpus_metrics(a)
            mb = corpus_metrics(b)

            metric_names = [
                "turns",
                "words",
                "average_words",
                "average_tension_index",
                "maximum_tension_index",
                "questions",
                "speakers",
                "unique_words",
                "lexical_diversity"
            ]

            rows = []

            for metric in metric_names:
                rows.append({
                    "Metric": metric.replace("_", " ").title(),
                    "Corpus A": ma[metric],
                    "Corpus B": mb[metric],
                    "Difference (B - A)": round(
                        mb[metric] - ma[metric], 3
                    )
                })

            comparison = pd.DataFrame(rows)

            st.subheader("Statistical Comparison")

            st.dataframe(
                comparison,
                use_container_width=True
            )

            c1, c2 = st.columns(2)

            c1.metric(
                "Corpus A Mean Index",
                ma["average_tension_index"]
            )

            c2.metric(
                "Corpus B Mean Index",
                mb["average_tension_index"]
            )

            st.subheader("Multi-label Category Distribution")

            dist_a = category_distribution(a)
            dist_b = category_distribution(b)

            all_categories = sorted(
                set(dist_a) | set(dist_b)
            )

            category_data = pd.DataFrame({
                "Corpus A": [
                    dist_a.get(c, 0)
                    for c in all_categories
                ],
                "Corpus B": [
                    dist_b.get(c, 0)
                    for c in all_categories
                ]
            }, index=all_categories)

            if not category_data.empty:
                st.bar_chart(category_data)

            difference = (
                ma["average_tension_index"]
                - mb["average_tension_index"]
            )

            if difference > 0:
                conclusion = (
                    "Corpus A has the higher mean heuristic index."
                )
            elif difference < 0:
                conclusion = (
                    "Corpus B has the higher mean heuristic index."
                )
            else:
                conclusion = (
                    "Both corpora have equal mean heuristic indices."
                )

            st.markdown(
                f"""
                <div class="context-box">
                    <b>Computed Observation:</b><br>
                    {conclusion}<br>
                    <b>Absolute Difference:</b>
                    {abs(difference):.2f} index points.
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption(
                "Comparisons are descriptive. Different corpus lengths, "
                "genres, speakers and annotation conventions can affect "
                "the results."
            )

            st.download_button(
                "⬇️ Download Comparison",
                data=comparison.to_csv(
                    index=False
                ).encode("utf-8-sig"),
                file_name="corpus_comparison.csv",
                mime="text/csv"
            )


# =============================================================================
# 17. MODULE 8: RULE-BASED BRANCHING DEMONSTRATOR
# =============================================================================

elif selected_module == "🔄 Rule-Based Branching Demonstrator":

    st.title("🔄 Rule-Based Branching Demonstrator")

    corpus = get_corpus_input(
        "Enter the original dialogue:",
        "branch_corpus"
    )

    intervention = st.text_area(
        "Enter a new character intervention:",
        key="branch_intervention",
        placeholder="Enter a new line of dialogue..."
    )

    if st.button("⚡ Simulate Dynamic Branches", key="branch"):

        original = analyze_corpus(corpus)

        if not original or not intervention.strip():
            st.warning(
                "Provide both an original dialogue "
                "and an intervention."
            )

        else:
            base = original[-1]["tension_index"]

            intervention_class = classify_text(intervention)

            intervention_analysis = analyze_corpus(
                corpus + "\nNew Character: " + intervention
            )

            new_index = intervention_analysis[-1]["tension_index"]

            if new_index == 0.0:
                new_index = 15.0

            branch_a = max(0, min(100, base * 0.85))
            branch_b = max(0, min(100, new_index * 1.15))
            branch_c = max(0, min(100, base * 0.75))

            branches = [
                {
                    "name": "A: Evasion / Closure",
                    "index": round(branch_a, 1),
                    "description": (
                        "A hypothetical continuation with reduced "
                        "interaction and limited disclosure."
                    )
                },
                {
                    "name": "B: Confrontation / Escalation",
                    "index": round(branch_b, 1),
                    "description": (
                        "A hypothetical continuation with increased "
                        "lexical conflict markers."
                    )
                },
                {
                    "name": "C: Softening / Resolution",
                    "index": round(branch_c, 1),
                    "description": (
                        "A hypothetical continuation with reduced "
                        "heuristic indicators."
                    )
                }
            ]

            st.subheader("Input Diagnostic")

            st.write(
                "**Intervention categories:**",
                ", ".join(intervention_class["categories"])
                or "No lexical category match"
            )

            st.write("Original final index:", base)
            st.write("Intervention index:", new_index)

            st.subheader("Alternative Hypothetical Trajectories")

            cols = st.columns(3)

            for i, branch in enumerate(branches):
                with cols[i]:
                    st.markdown(
                        f"""
                        <div class="lab-card">
                            <b>{branch["name"]}</b><br><br>
                            {branch["description"]}<br><br>
                            <b>Illustrative index:</b>
                            {branch["index"]}/100
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            trajectory = pd.DataFrame({
                "Branch A": [
                    base,
                    branch_a,
                    max(0, branch_a - 5)
                ],
                "Branch B": [
                    base,
                    new_index,
                    branch_b
                ],
                "Branch C": [
                    base,
                    branch_c + 10,
                    branch_c
                ]
            }, index=[
                "Original",
                "Intervention",
                "Hypothetical Continuation"
            ])

            st.subheader("Illustrative Trajectories")
            st.line_chart(trajectory)

            st.warning(
                "The branching model creates hypothetical rule-based "
                "scenarios. It does not predict human behaviour, "
                "character intention or authorial decisions."
            )


# =============================================================================
# 18. MODULE 9: THEORETICAL MARKER INDEX
# =============================================================================

elif selected_module == "⚛️ Dynamic Theoretical Marker Index":

    st.title("⚛️ Dynamic Theoretical Marker Index")

    corpus = get_corpus_input(
        "Enter text for theoretical marker analysis:",
        "theory_corpus"
    )

    if st.button("⚡ Calculate Theoretical Markers", key="theory"):

        words = tokenize(corpus)

        if not words:
            st.warning("Enter text before analysis.")

        else:
            definitions = {
                "Sartrean Bad Faith": (
                    "BAD_FAITH",
                    "Lexical proxies associated with denial, "
                    "justification and responsibility."
                ),
                "Lacanian Lack / Void": (
                    "LACK",
                    "Lexical proxies associated with absence, "
                    "desire and incompleteness."
                ),
                "Foucauldian Surveillance": (
                    "SURVEILLANCE",
                    "Lexical proxies associated with observation, "
                    "authority and control."
                )
            }

            results = []

            for theory, (category, explanation) in definitions.items():

                matches = matched_words(corpus, category)

                frequency = sum(
                    words.count(word)
                    for word in matches
                )

                density = (
                    frequency / len(words) * 100
                    if words else 0
                )

                results.append({
                    "Theoretical Framework": theory,
                    "Matched Terms": ", ".join(matches) or "None",
                    "Marker Frequency": frequency,
                    "Marker Density (%)": round(density, 2),
                    "Explanation": explanation
                })

            df = pd.DataFrame(results)

            st.subheader("Theoretical Marker Index")

            st.dataframe(
                df,
                use_container_width=True
            )

            st.subheader("Marker Density")

            st.bar_chart(
                df.set_index("Theoretical Framework")[
                    ["Marker Density (%)"]
                ]
            )

            strongest = max(
                results,
                key=lambda x: x["Marker Density (%)"]
            )

            st.markdown(
                f"""
                <div class="context-box">
                    <b>Highest lexical marker density:</b>
                    {strongest["Theoretical Framework"]}<br>
                    <b>Density:</b>
                    {strongest["Marker Density (%)"]}%<br>
                    <b>Evidence:</b>
                    {strongest["Matched Terms"]}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.warning(
                "These indicators are lexical operationalizations, "
                "not direct measurements of Sartrean, Lacanian or "
                "Foucauldian theoretical constructs."
            )


# =============================================================================
# 19. MODULE 10: VALIDATION PROTOCOL
# =============================================================================

elif selected_module == "📊 Validation Protocol":

    st.title("📊 Validation Protocol & Empirical Design")

    corpus = get_corpus_input(
        "Enter corpus for validation:",
        "validation_corpus"
    )

    if st.button("⚡ Generate Validation Dataset", key="validation"):

        results = analyze_corpus(corpus)

        if not results:
            st.warning("Enter a corpus first.")

        else:
            validation_df = pd.DataFrame([
                {
                    "Beat": r["beat"],
                    "Speaker": r["speaker"],
                    "Text": r["text"],
                    "Engine Primary Classification": r["category"],
                    "Engine Multi-label Classification": "; ".join(
                        r["categories"]
                    ),
                    "Tension Index": r["tension_index"]
                }
                for r in results
            ])

            st.session_state["validation_data"] = validation_df
            st.session_state["validation_results"] = results

            st.subheader("Generated Annotation Dataset")

            st.dataframe(
                validation_df,
                use_container_width=True
            )

            labels = list(CLASS_COLORS.keys())

            st.subheader("Human Annotation")

            st.caption(
                "For this validation workspace, annotators assign "
                "one primary label per beat. This evaluates primary-label "
                "agreement, not the complete multi-label output."
            )

            annotation_rows = []

            for i, r in enumerate(results):

                st.markdown(
                    f"**Beat {r['beat']} — {safe_html(r['text'])}**"
                )

                c1, c2 = st.columns(2)

                with c1:
                    ann_a = st.selectbox(
                        f"Annotator A — Beat {r['beat']}",
                        labels,
                        index=None,
                        key=f"ann_a_{i}"
                    )

                with c2:
                    ann_b = st.selectbox(
                        f"Annotator B — Beat {r['beat']}",
                        labels,
                        index=None,
                        key=f"ann_b_{i}"
                    )

                annotation_rows.append({
                    "Beat": r["beat"],
                    "Annotator A": ann_a,
                    "Annotator B": ann_b,
                    "Engine": r["category"]
                })

            complete = [
                x for x in annotation_rows
                if x["Annotator A"] is not None
                and x["Annotator B"] is not None
            ]

            if complete:

                labels_a = [
                    x["Annotator A"] for x in complete
                ]

                labels_b = [
                    x["Annotator B"] for x in complete
                ]

                observed_agreement = sum(
                    a == b
                    for a, b in zip(labels_a, labels_b)
                ) / len(complete)

                kappa = None

                try:
                    kappa = cohen_kappa_score(
                        labels_a,
                        labels_b,
                        labels=labels
                    )
                except (ValueError, ZeroDivisionError):
                    kappa = None

                st.divider()
                st.subheader("Inter-Annotator Reliability")

                st.metric(
                    "Observed Agreement",
                    f"{observed_agreement * 100:.1f}%"
                )

                if kappa is not None and not math.isnan(kappa):
                    st.metric(
                        "Cohen's Kappa",
                        round(float(kappa), 3)
                    )
                else:
                    st.info(
                        "Cohen's Kappa could not be reliably estimated "
                        "from the current annotations."
                    )

                st.metric(
                    "Completed Double-Annotated Beats",
                    len(complete)
                )

                st.caption(
                    "Cohen's Kappa adjusts observed agreement for "
                    "chance agreement. Its interpretation depends on "
                    "sample size, label prevalence and annotation design."
                )

                engine_labels = [
                    x["Engine"] for x in complete
                ]

                engine_agreement = sum(
                    e == a
                    for e, a in zip(engine_labels, labels_a)
                ) / len(complete)

                st.metric(
                    "Engine–Annotator A Agreement",
                    f"{engine_agreement * 100:.1f}%"
                )

                st.metric(
                    "Engine–Annotator B Agreement",
                    f"{
                        sum(e == b for e, b in zip(engine_labels, labels_b))
                        / len(complete) * 100
                    :.1f}%"
                )

                annotation_df = pd.DataFrame(annotation_rows)

                st.download_button(
                    "⬇️ Download Annotation Dataset",
                    data=annotation_df.to_csv(
                        index=False
                    ).encode("utf-8-sig"),
                    file_name="human_annotation_dataset.csv",
                    mime="text/csv"
                )

            else:
                st.info(
                    "Complete both annotators' labels for at least "
                    "one beat to calculate agreement."
                )

            st.subheader("Recommended Research Validation")

            st.markdown("""
            1. Develop a written annotation codebook.
            2. Recruit independent annotators who do not know the engine output.
            3. Use a representative corpus with multiple genres and speakers.
            4. Calculate inter-annotator reliability before evaluating the engine.
            5. Compare the engine against human consensus labels.
            6. Report precision, recall, F1-score and confusion matrices.
            7. Use a held-out test set rather than evaluating only on the development corpus.
            8. Conduct error analysis for negation, irony, metaphor and ambiguous language.
            """)


# =============================================================================
# 20. MODULE 11: CORE ARTIFACT & LIMITATIONS
# =============================================================================

elif selected_module == "📜 Core Artifact & Limitations":

    st.title("📜 Core Artifact & Methodological Limitations")

    corpus = get_corpus_input(
        "Enter text to generate a methodological report:",
        "artifact_corpus"
    )

    if st.button("⚡ Generate Corpus Report", key="artifact"):

        results = analyze_corpus(corpus)

        if not results:
            st.warning("No corpus available.")

        else:
            metrics = corpus_metrics(results)
            categories = category_distribution(results)

            corpus_hash = hashlib.sha256(
                corpus.encode("utf-8")
            ).hexdigest()

            report = {
                "Application Version": APP_VERSION,
                "Generation Date": datetime.datetime.now().isoformat(
                    timespec="seconds"
                ),
                "Corpus SHA-256": corpus_hash,
                "Total Beats": metrics["turns"],
                "Total Words": metrics["words"],
                "Unique Words": metrics["unique_words"],
                "Lexical Diversity": metrics["lexical_diversity"],
                "Number of Speakers": metrics["speakers"],
                "Mean Heuristic Tension Index": (
                    metrics["average_tension_index"]
                ),
                "Maximum Heuristic Tension Index": (
                    metrics["maximum_tension_index"]
                ),
                "Minimum Heuristic Tension Index": (
                    metrics["minimum_tension_index"]
                ),
                "Detected Questions": metrics["questions"],
                "Dominant Primary Classification": (
                    Counter(
                        r["category"] for r in results
                    ).most_common(1)[0][0]
                )
            }

            st.subheader("Corpus Integrity Report")

            st.dataframe(
                pd.DataFrame(
                    report.items(),
                    columns=["Parameter", "Computed Result"]
                ),
                use_container_width=True
            )

            st.subheader("Multi-label Classification Frequencies")

            if categories:
                st.bar_chart(
                    pd.DataFrame.from_dict(
                        categories,
                        orient="index",
                        columns=["Frequency"]
                    )
                )

            st.subheader("Methodological Limitations")

            limitations = [
                "Lexical matching cannot reliably establish psychological intention.",
                "Negation handling is approximate and does not perform full syntactic parsing.",
                "Polysemy, irony, metaphor, sarcasm and cultural context may produce classification errors.",
                "The system is rule-based and does not contain a trained contextual language model.",
                "TF-IDF similarity measures lexical overlap, not semantic understanding.",
                "The heuristic tension index is not a validated psychological scale.",
                "Theoretical markers are simplified lexical proxies.",
                "Speaker participation does not necessarily equal social power or dominance.",
                "Question-response similarity does not prove that a question was answered.",
                "Branching scenarios are illustrative, not predictive.",
                "Academic validity requires independent annotation and external evaluation."
            ]

            for limitation in limitations:
                st.markdown(f"- {limitation}")

            st.subheader("Export Research Report")

            report_df = pd.DataFrame(
                report.items(),
                columns=["Parameter", "Result"]
            )

            st.download_button(
                "⬇️ Download Corpus Report (CSV)",
                data=report_df.to_csv(
                    index=False
                ).encode("utf-8-sig"),
                file_name="ontological_silence_report.csv",
                mime="text/csv"
            )

            beat_csv = results_dataframe(results).to_csv(
                index=False
            ).encode("utf-8-sig")

            st.download_button(
                "⬇️ Download Beat-Level Analysis (CSV)",
                data=beat_csv,
                file_name="beat_level_analysis.csv",
                mime="text/csv"
            )

            st.download_button(
                "⬇️ Download Full Report (JSON)",
                data=pd.Series(report).to_json(
                    indent=4,
                    force_ascii=False
                ),
                file_name="ontological_silence_report.json",
                mime="application/json"
            )


# =============================================================================
# 21. GLOBAL FOOTER
# =============================================================================

st.divider()

st.markdown(
    f"""
    <p style="text-align:center; color:#8b949e; font-size:11px;">
    ONTOLOGICAL SILENCE & PARANOIA ENGINE |
    VERSION {APP_VERSION} |
    COMPUTATIONAL DRAMATURGY RESEARCH PROTOTYPE |
    AGIL CHIRAGLI
    </p>
    """,
    unsafe_allow_html=True
)
