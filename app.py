
import re
import math
import html
import datetime
from collections import Counter, defaultdict

import pandas as pd
import streamlit as st


# =============================================================================
# 1. CONFIGURATION
# =============================================================================

st.set_page_config(
    page_title="Ontological Silence & Paranoia Engine",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# 2. DYNAMIC LEXICON
# =============================================================================

LEXICON = {
    "AGGRESSIVE": {
        "attack", "kill", "destroy", "threat", "force", "obey",
        "punish", "fight", "hate", "angry", "furious", "violent",
        "brutal", "cruel", "murder", "weapon", "enemy", "war",
        "shut", "order", "demand", "strike", "break", "revenge",
        "idiot", "stupid", "damn", "bomb", "gun", "knife"
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
        "heartbroken", "wounded"
    },

    "DEFENSE": {
        "truth", "reality", "reason", "logic", "because",
        "understand", "explain", "philosophy", "theory",
        "maybe", "perhaps", "could", "would", "might",
        "should", "pretend", "mask", "defend", "excuse",
        "justify", "rationalize", "deny", "avoid", "deflect",
        "distract", "divert", "escape", "everyone", "nobody",
        "always", "never", "analyze", "consider", "evaluate"
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
        "guard", "inspect", "inspection", "obey", "institution"
    },

    "LACK": {
        "empty", "nothing", "absence", "missing", "desire",
        "want", "need", "lost", "void", "alone", "lack",
        "silence", "incomplete", "unfulfilled", "absence"
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
    "being", "who", "what", "when", "where", "which",
    "will", "would", "could", "should", "does", "did"
}

CLASS_COLORS = {
    "Silence / Void": "#f85149",
    "Aggression": "#ff7b72",
    "Emotional Withdrawal": "#bc8cff",
    "Defensive Rationalization": "#f0883e",
    "Direct Inquiry": "#58a6ff",
    "Dynamic Interaction": "#3fb950"
}

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
.terminal-box {
    background: #032f20;
    border: 1px solid #116329;
    padding: 16px;
    border-radius: 6px;
    margin-bottom: 12px;
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
</style>
""", unsafe_allow_html=True)


# =============================================================================
# 4. TEXT PROCESSING ENGINE
# =============================================================================

def tokenize(text):
    return re.findall(r"[a-zA-Z']+", text.lower())


def get_text_vector(text):
    return Counter(
        word for word in tokenize(text)
        if len(word) > 2 and word not in STOP_WORDS
    )


def cosine_similarity_native(v1, v2):
    intersection = set(v1) & set(v2)

    numerator = sum(v1[w] * v2[w] for w in intersection)

    denominator = (
        math.sqrt(sum(v ** 2 for v in v1.values())) *
        math.sqrt(sum(v ** 2 for v in v2.values()))
    )

    return numerator / denominator if denominator else 0.0


def matched_words(text, category):
    words = tokenize(text)
    return sorted(set(words) & LEXICON[category])


def parse_corpus(text):
    parsed = []

    for index, raw_line in enumerate(text.splitlines()):
        line = raw_line.strip()

        if not line:
            continue

        if ":" in line:
            speaker, dialogue = line.split(":", 1)
            speaker = speaker.strip() or f"Actor {index + 1}"
            dialogue = dialogue.strip().lstrip("-").strip()
        else:
            speaker = f"Actor {index + 1}"
            dialogue = line.lstrip("-").strip()

        parsed.append({
            "beat": len(parsed) + 1,
            "speaker": speaker,
            "text": dialogue,
            "original": line
        })

    return parsed


def classify_text(text):
    lower = text.lower()

    silence = matched_words(text, "SILENCE")
    aggressive = matched_words(text, "AGGRESSIVE")
    withdrawal = matched_words(text, "WITHDRAWAL")
    defense = matched_words(text, "DEFENSE")

    if re.search(r"\(silence\)|\[silence\]|\(pause\)|\[pause\]", lower):
        category = "Silence / Void"
    elif silence:
        category = "Silence / Void"
    elif aggressive:
        category = "Aggression"
    elif withdrawal:
        category = "Emotional Withdrawal"
    elif defense:
        category = "Defensive Rationalization"
    elif "?" in text:
        category = "Direct Inquiry"
    else:
        category = "Dynamic Interaction"

    return {
        "category": category,
        "silence": silence,
        "aggressive": aggressive,
        "withdrawal": withdrawal,
        "defense": defense,
        "color": CLASS_COLORS[category]
    }


def analyze_corpus(corpus, w_evasion=35, w_compression=20):
    beats = parse_corpus(corpus)

    if not beats:
        return []

    previous_words = {}
    results = []

    for i, beat in enumerate(beats):
        text = beat["text"]
        speaker = beat["speaker"]

        words = tokenize(text)
        word_count = len(words)

        previous_count = previous_words.get(speaker)

        compression = (
            max(0, (previous_count - word_count) / previous_count)
            if previous_count else 0
        )

        previous_words[speaker] = word_count

        if i > 0:
            similarity = cosine_similarity_native(
                get_text_vector(beats[i - 1]["text"]),
                get_text_vector(text)
            )
            evasion = 1 - similarity
        else:
            similarity = 0
            evasion = 0

        classification = classify_text(text)

        base_scores = {
            "Silence / Void": 85,
            "Aggression": 80,
            "Emotional Withdrawal": 75,
            "Defensive Rationalization": 65,
            "Direct Inquiry": 45,
            "Dynamic Interaction": 30
        }

        tension = base_scores[classification["category"]]

        tension += evasion * w_evasion * 0.2
        tension += compression * w_compression * 0.2

        if "?" in text:
            tension += 3

        tension = round(max(0, min(100, tension)), 1)

        results.append({
            **beat,
            **classification,
            "words": word_count,
            "questions": text.count("?"),
            "similarity": round(similarity, 3),
            "evasion": round(evasion, 3),
            "compression": round(compression, 3),
            "tension": tension
        })

    return results


def corpus_metrics(results):
    if not results:
        return {}

    total_words = sum(r["words"] for r in results)
    total_turns = len(results)

    tensions = [r["tension"] for r in results]

    return {
        "turns": total_turns,
        "words": total_words,
        "average_words": round(total_words / total_turns, 2),
        "average_tension": round(sum(tensions) / len(tensions), 2),
        "maximum_tension": max(tensions),
        "minimum_tension": min(tensions),
        "questions": sum(r["questions"] for r in results),
        "speakers": len(set(r["speaker"] for r in results)),
        "unique_words": len(set(
            word for r in results for word in tokenize(r["text"])
        ))
    }


def safe_html(value):
    return html.escape(str(value))


def show_analysis_cards(results):
    for r in results:
        st.markdown(
            f"""
            <div class="lab-card" style="border-left-color:{r['color']}">
                <b>Beat {r['beat']} | {safe_html(r['speaker'])}</b><br><br>
                <i style="color:#58a6ff">
                    "{safe_html(r['text'])}"
                </i><br><br>
                <b>Classification:</b> {r['category']}<br>
                <b>Tension:</b> {r['tension']}%<br>
                <b>Evasion:</b> {r['evasion']}<br>
                <b>Compression:</b> {r['compression']}<br>
                <b>Word Count:</b> {r['words']}
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


# =============================================================================
# 5. SIDEBAR AND HYPERPARAMETERS
# =============================================================================

with st.sidebar:
    st.markdown("### 👁️ Terminal Control")
    st.caption("Computational Dramaturgy Lab | Dynamic Research Engine")

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

    st.markdown("### ⚙️ Hyperparameters")

    w_evasion = st.slider(
        "Semantic Divergence Weight",
        0.0, 50.0, 35.0, 5.0
    )

    w_compression = st.slider(
        "Intra-Speaker Compression Weight",
        0.0, 40.0, 20.0, 5.0
    )

    st.divider()

    st.markdown("**Framework Architect:** Agil Chiragli")
    st.markdown("**Research Prototype:** Independent")
    st.caption(datetime.date.today().isoformat())


# =============================================================================
# 6. MODULE 1: FRAMEWORK
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
    This platform applies transparent, rule-based computational
    methods to dramatic dialogue and narrative text.

    All analytical outputs are generated from user-provided text.
    The engine identifies lexical patterns, discourse structures,
    conversational asymmetries and potential narrative turning points.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Research Objectives")

    objectives = [
        ("Quantifying Subtext",
         "Identifying lexical indicators of silence, withdrawal and evasion."),
        ("Conversational Power",
         "Measuring speaker participation and linguistic dominance."),
        ("Narrative Dynamics",
         "Detecting changes in tension and potential structural turning points."),
        ("Explainable Analysis",
         "Showing the lexical evidence behind each heuristic classification."),
        ("Theoretical Mapping",
         "Operationalizing selected concepts from Sartre, Lacan and Foucault.")
    ]

    for title, description in objectives:
        st.markdown(
            f"<div class='lab-card'><b>{title}</b><br>{description}</div>",
            unsafe_allow_html=True
        )

    st.warning(
        "The engine produces heuristic indicators, not validated "
        "psychological diagnoses or proof of a character's intentions."
    )


# =============================================================================
# 7. MODULE 2: UNIVERSAL NLP X-RAY
# =============================================================================

elif selected_module == "💬 Universal NLP Scene Analyzer":

    st.title("💬 Universal NLP Scene Analyzer")

    corpus = get_corpus_input(
        "Enter dialogue, scene or narrative text:",
        "xray_corpus"
    )

    if st.button("⚡ Execute Universal X-Ray", key="xray"):
        results = analyze_corpus(corpus, w_evasion, w_compression)

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
            c3.metric("Mean Tension", f'{metrics["average_tension"]}%')
            c4.metric("Speakers", metrics["speakers"])

            st.subheader("Beat-by-Beat Analysis")
            show_analysis_cards(results)

            st.subheader("Tension Distribution")

            tension_df = pd.DataFrame({
                "Beat": [f"Beat {r['beat']}" for r in results],
                "Tension": [r["tension"] for r in results]
            })

            st.line_chart(tension_df.set_index("Beat"))

            st.subheader("Emotional Classification Distribution")

            distribution = Counter(r["category"] for r in results)

            st.bar_chart(
                pd.DataFrame.from_dict(
                    distribution,
                    orient="index",
                    columns=["Frequency"]
                )
            )

            st.subheader("Corpus Statistics")
            st.dataframe(
                pd.DataFrame([metrics]),
                use_container_width=True
            )


# =============================================================================
# 8. MODULE 3: CHARACTER RELATIONSHIP & POWER MAP
# =============================================================================

elif selected_module == "🕸️ Character Relationship & Power Map":

    st.title("🕸️ Character Relationship & Power Map")

    corpus = get_corpus_input(
        "Enter character dialogue:",
        "power_corpus"
    )

    if st.button("⚡ Generate Dynamic Power Map", key="power"):

        results = analyze_corpus(corpus, w_evasion, w_compression)

        if not results:
            st.warning("No dialogue detected.")
        else:
            stats = defaultdict(lambda: {
                "turns": 0,
                "words": 0,
                "questions": 0,
                "tension": [],
                "defense": 0,
                "aggression": 0
            })

            for r in results:
                s = stats[r["speaker"]]

                s["turns"] += 1
                s["words"] += r["words"]
                s["questions"] += r["questions"]
                s["tension"].append(r["tension"])

                s["defense"] += len(r["defense"])
                s["aggression"] += len(r["aggressive"])

            total_turns = len(results)
            total_words = sum(r["words"] for r in results)

            rows = []

            for speaker, s in stats.items():

                turn_share = s["turns"] / total_turns * 100
                word_share = (
                    s["words"] / total_words * 100
                    if total_words else 0
                )

                dominance = (turn_share + word_share) / 2

                rows.append({
                    "Speaker": speaker,
                    "Turns": s["turns"],
                    "Words": s["words"],
                    "Turn Share (%)": round(turn_share, 1),
                    "Word Share (%)": round(word_share, 1),
                    "Dominance Index (%)": round(dominance, 1),
                    "Questions": s["questions"],
                    "Defensive Markers": s["defense"],
                    "Aggressive Markers": s["aggression"],
                    "Average Tension": round(
                        sum(s["tension"]) / len(s["tension"]), 1
                    )
                })

            df = pd.DataFrame(rows).sort_values(
                "Dominance Index (%)",
                ascending=False
            )

            st.subheader("Speaker Dominance Matrix")
            st.dataframe(df, use_container_width=True)

            st.subheader("Conversational Participation")
            st.bar_chart(
                df.set_index("Speaker")[
                    ["Turn Share (%)", "Word Share (%)"]
                ]
            )

            st.subheader("Dominance Distribution")
            st.bar_chart(
                df.set_index("Speaker")[["Dominance Index (%)"]]
            )

            dominant = df.iloc[0]

            st.markdown(
                f"""
                <div class="context-box">
                <b>Highest Linguistic Participation:</b>
                {safe_html(dominant["Speaker"])}<br>
                <b>Dominance Index:</b>
                {dominant["Dominance Index (%)"]}%<br>
                <b>Interpretation:</b>
                This character has the highest combined share of
                conversational turns and lexical volume.
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption(
                "Dominance measures linguistic participation, "
                "not necessarily social or psychological authority."
            )


# =============================================================================
# 9. MODULE 4: UNANSWERED QUESTION TRACKER
# =============================================================================

elif selected_module == "❓ Unanswered Question Tracker":

    st.title("❓ Unanswered Question & Deflection Tracker")

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

                for next_beat in beats[i + 1:]:
                    if next_beat["speaker"] != beat["speaker"]:
                        response = next_beat
                        break

                if response is None:
                    status = "No subsequent response found"
                    score = 100
                    evidence = []
                else:
                    response_class = classify_text(response["text"])

                    evidence = (
                        response_class["defense"] +
                        response_class["silence"] +
                        response_class["withdrawal"]
                    )

                    direct_words = {
                        "yes", "no", "because", "when", "where",
                        "after", "before", "during", "did", "was"
                    }

                    response_tokens = set(tokenize(response["text"]))

                    if response_class["category"] == "Silence / Void":
                        score = 95
                        status = "Possible silence / non-response"
                    elif response_class["defense"]:
                        score = 75
                        status = "Possible defensive deflection"
                    elif response_class["withdrawal"]:
                        score = 65
                        status = "Possible emotional withdrawal"
                    elif response_tokens & direct_words:
                        score = 20
                        status = "Potentially direct response"
                    else:
                        score = 45
                        status = "Response requires contextual review"

                audit.append({
                    "Question Speaker": beat["speaker"],
                    "Question": beat["text"],
                    "Response Speaker": (
                        response["speaker"] if response else "None"
                    ),
                    "Response": (
                        response["text"] if response else "No response"
                    ),
                    "Deflection Indicator (%)": score,
                    "Status": status,
                    "Lexical Evidence": ", ".join(evidence)
                })

            if not audit:
                st.info("No question marks were detected in the corpus.")
            else:
                df = pd.DataFrame(audit)

                st.subheader("Question-Response Audit")
                st.dataframe(df, use_container_width=True)

                st.subheader("Potential Deflection Indicators")

                st.bar_chart(
                    df.set_index("Question Speaker")[
                        ["Deflection Indicator (%)"]
                    ]
                )

                unresolved = sum(
                    x["Deflection Indicator (%)"] >= 65 for x in audit
                )

                st.metric(
                    "Questions Requiring Contextual Review",
                    unresolved
                )

                st.caption(
                    "Deflection indicators are heuristic flags. "
                    "They do not establish that a response is intentionally evasive."
                )


# =============================================================================
# 10. MODULE 5: TURNING POINT DETECTOR
# =============================================================================

elif selected_module == "📈 Narrative Turning Point Detector":

    st.title("📈 Narrative Turning Point Detector")

    corpus = get_corpus_input(
        "Enter a narrative or dramatic scene:",
        "turning_corpus"
    )

    if st.button("⚡ Detect Turning Points", key="turning"):

        results = analyze_corpus(corpus, w_evasion, w_compression)

        if len(results) < 2:
            st.warning("At least two dialogue beats are required.")
        else:
            tensions = [r["tension"] for r in results]

            mean_tension = sum(tensions) / len(tensions)

            points = []

            for i, r in enumerate(results):

                previous = tensions[i - 1] if i > 0 else tensions[i]
                following = (
                    tensions[i + 1]
                    if i < len(tensions) - 1
                    else tensions[i]
                )

                change = r["tension"] - previous

                if r["tension"] >= mean_tension + 15:
                    label = "High-Tension Beat"
                    significance = "Elevated tension relative to the corpus."
                elif change >= 15:
                    label = "Escalation Point"
                    significance = "A notable increase in heuristic tension."
                elif change <= -15:
                    label = "De-escalation Point"
                    significance = "A notable decrease in heuristic tension."
                elif (
                    r["tension"] >= previous and
                    r["tension"] >= following
                ):
                    label = "Potential Local Apex"
                    significance = "A local maximum in the tension sequence."
                else:
                    label = "Structural Continuation"
                    significance = "No major local tension shift detected."

                if i > 0:
                    previous_speaker = results[i - 1]["speaker"]
                    speaker_change = previous_speaker != r["speaker"]
                else:
                    speaker_change = False

                points.append({
                    "Beat": r["beat"],
                    "Speaker": r["speaker"],
                    "Text": r["text"],
                    "Tension": r["tension"],
                    "Change": round(change, 1),
                    "Structural Label": label,
                    "Speaker Shift": speaker_change,
                    "Interpretation": significance
                })

            st.subheader("Narrative Tension Trajectory")

            chart_df = pd.DataFrame({
                "Tension": tensions
            }, index=[f"Beat {i+1}" for i in range(len(tensions))])

            st.line_chart(chart_df)

            st.subheader("Detected Structural Points")

            point_df = pd.DataFrame(points)
            st.dataframe(point_df, use_container_width=True)

            for p in points:
                if p["Structural Label"] != "Structural Continuation":
                    st.markdown(
                        f"""
                        <div class="lab-card">
                        <b>{p["Structural Label"]} | Beat {p["Beat"]}</b><br>
                        <i>{safe_html(p["Text"])}</i><br><br>
                        <b>Tension:</b> {p["Tension"]}%<br>
                        <b>Change:</b> {p["Change"]}%<br>
                        <b>Interpretation:</b> {p["Interpretation"]}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


# =============================================================================
# 11. MODULE 6: EXPLAINABLE ANALYSIS
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
            words = [
                w for w in tokenize(target)
                if len(w) > 3 and w not in STOP_WORDS
            ]

            frequencies = Counter(words)

            attribution = []

            weights = {
                "AGGRESSIVE": 1.8,
                "SILENCE": 2.0,
                "WITHDRAWAL": 1.6,
                "DEFENSE": 1.5,
                "INQUIRY": 1.3,
                "SURVEILLANCE": 1.7,
                "LACK": 1.8,
                "BAD_FAITH": 1.5
            }

            for word, frequency in frequencies.most_common(30):

                categories = [
                    category
                    for category in LEXICON
                    if word in LEXICON[category]
                ]

                base_weight = len(word) * frequency * 2.5

                if categories:
                    multiplier = max(weights[c] for c in categories)
                else:
                    multiplier = 1.0

                weight = base_weight * multiplier

                attribution.append({
                    "Token": word,
                    "Frequency": frequency,
                    "Detected Categories": (
                        ", ".join(categories) if categories
                        else "General lexical token"
                    ),
                    "Attribution Weight": round(weight, 2)
                })

            total = sum(x["Attribution Weight"] for x in attribution)

            for item in attribution:
                item["Contribution (%)"] = round(
                    item["Attribution Weight"] / total * 100, 2
                ) if total else 0

            classification = classify_text(target)

            st.subheader("Classification Result")

            st.metric(
                "Detected Classification",
                classification["category"]
            )

            st.markdown(
                f"""
                <div class="context-box">
                <b>Input:</b> {safe_html(target)}<br>
                <b>Classification:</b> {classification["category"]}<br>
                <b>Evidence:</b>
                {", ".join(
                    classification["silence"] +
                    classification["aggressive"] +
                    classification["withdrawal"] +
                    classification["defense"]
                ) or "No category-specific lexical evidence detected"}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.subheader("Feature Attribution")

            if attribution:
                attribution_df = pd.DataFrame(attribution)
                st.dataframe(attribution_df, use_container_width=True)

                st.bar_chart(
                    attribution_df.set_index("Token")[
                        ["Contribution (%)"]
                    ]
                )
            else:
                st.info("No analyzable tokens detected.")

            st.subheader("Decision Rule Trace")

            detected = {
                "Silence": classification["silence"],
                "Aggression": classification["aggressive"],
                "Withdrawal": classification["withdrawal"],
                "Defense": classification["defense"]
            }

            for category, evidence in detected.items():
                st.write(
                    f"**{category}:**",
                    ", ".join(evidence) if evidence else "No match"
                )

            st.caption(
                "Attribution weights describe this rule-based system's "
                "lexical weighting, not causal feature importance."
            )


# =============================================================================
# 12. MODULE 7: COMPARATIVE ANALYZER
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

        a = analyze_corpus(corpus_a, w_evasion, w_compression)
        b = analyze_corpus(corpus_b, w_evasion, w_compression)

        if not a or not b:
            st.warning("Both corpora must contain text.")
        else:
            ma = corpus_metrics(a)
            mb = corpus_metrics(b)

            rows = []

            for metric in [
                "turns",
                "words",
                "average_words",
                "average_tension",
                "maximum_tension",
                "questions",
                "speakers",
                "unique_words"
            ]:
                rows.append({
                    "Metric": metric.replace("_", " ").title(),
                    "Corpus A": ma[metric],
                    "Corpus B": mb[metric],
                    "Difference (B - A)": round(
                        mb[metric] - ma[metric], 2
                    )
                })

            comparison = pd.DataFrame(rows)

            st.subheader("Statistical Comparison")
            st.dataframe(comparison, use_container_width=True)

            c1, c2 = st.columns(2)

            with c1:
                st.metric(
                    "Corpus A Mean Tension",
                    f'{ma["average_tension"]}%'
                )

            with c2:
                st.metric(
                    "Corpus B Mean Tension",
                    f'{mb["average_tension"]}%'
                )

            st.subheader("Category Distribution")

            all_categories = set(
                [r["category"] for r in a + b]
            )

            category_data = pd.DataFrame({
                "Corpus A": [
                    sum(r["category"] == c for r in a)
                    for c in all_categories
                ],
                "Corpus B": [
                    sum(r["category"] == c for r in b)
                    for c in all_categories
                ]
            }, index=list(all_categories))

            st.bar_chart(category_data)

            st.subheader("Comparative Interpretation")

            tension_difference = (
                ma["average_tension"] - mb["average_tension"]
            )

            if tension_difference > 0:
                conclusion = "Corpus A has the higher average heuristic tension."
            elif tension_difference < 0:
                conclusion = "Corpus B has the higher average heuristic tension."
            else:
                conclusion = "Both corpora have equal average heuristic tension."

            st.markdown(
                f"""
                <div class="context-box">
                <b>Computed Observation:</b><br>
                {conclusion}<br>
                <b>Absolute Difference:</b>
                {abs(tension_difference):.2f} percentage points.<br>
                <b>Higher lexical diversity:</b>
                {
                    "Corpus A" if ma["unique_words"] > mb["unique_words"]
                    else "Corpus B" if mb["unique_words"] > ma["unique_words"]
                    else "Equal"
                }
                </div>
                """,
                unsafe_allow_html=True
            )


# =============================================================================
# 13. MODULE 8: DYNAMIC BRANCHING DEMONSTRATOR
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

        original = analyze_corpus(corpus, w_evasion, w_compression)

        if not original or not intervention.strip():
            st.warning("Provide both an original dialogue and an intervention.")
        else:
            base = original[-1]["tension"]

            intervention_class = classify_text(intervention)

            intervention_analysis = analyze_corpus(
                corpus + "\nNew Character: " + intervention,
                w_evasion,
                w_compression
            )

            new_tension = intervention_analysis[-1]["tension"]

            aggressive = bool(intervention_class["aggressive"])
            defensive = bool(intervention_class["defense"])
            withdrawal = bool(intervention_class["withdrawal"])
            silence = bool(intervention_class["silence"])

            branch_a = max(0, min(100, base - 15))
            branch_b = max(0, min(100, new_tension + 15))
            branch_c = max(0, min(100, base - 25))

            branches = [
                {
                    "name": "A: Evasion / Closure",
                    "tension": branch_a,
                    "description": (
                        "The response avoids further engagement, "
                        "potentially reducing conversational exposure."
                    ),
                    "status": "Reinforced boundary"
                },
                {
                    "name": "B: Confrontation / Escalation",
                    "tension": branch_b,
                    "description": (
                        "The intervention increases conflict and "
                        "creates a potential confrontation."
                    ),
                    "status": "Increased tension"
                },
                {
                    "name": "C: Softening / Resolution",
                    "tension": branch_c,
                    "description": (
                        "The interaction moves towards reduced "
                        "tension and possible emotional disclosure."
                    ),
                    "status": "Reduced tension"
                }
            ]

            st.subheader("Input Diagnostic")

            st.write("Intervention classification:", intervention_class["category"])
            st.write("Original final tension:", base)
            st.write("Intervention tension:", new_tension)

            st.subheader("Alternative Trajectories")

            cols = st.columns(3)

            for i, branch in enumerate(branches):
                with cols[i]:
                    st.markdown(
                        f"""
                        <div class="lab-card">
                        <b>{branch["name"]}</b><br><br>
                        {branch["description"]}<br><br>
                        <b>Projected tension:</b>
                        {branch["tension"]}%<br>
                        <b>Structural status:</b>
                        {branch["status"]}
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
                    new_tension,
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
                "Projected Resolution"
            ])

            st.subheader("Projected Tension Trajectories")
            st.line_chart(trajectory)

            st.warning(
                "These are rule-based hypothetical trajectories, "
                "not predictions of actual human behavior or authorial intent."
            )


# =============================================================================
# 14. MODULE 9: THEORETICAL MARKER INDEX
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
                    "Lexical indicators of denial, justification "
                    "and responsibility avoidance."
                ),
                "Lacanian Lack / Void": (
                    "LACK",
                    "Lexical indicators of absence, desire and incompleteness."
                ),
                "Foucauldian Surveillance": (
                    "SURVEILLANCE",
                    "Lexical indicators of observation, authority and control."
                )
            }

            results = []

            for theory, (category, explanation) in definitions.items():

                matches = matched_words(corpus, category)

                frequency = sum(
                    words.count(word) for word in matches
                )

                score = (
                    frequency / len(words) * 100
                    if words else 0
                )

                results.append({
                    "Theoretical Framework": theory,
                    "Matched Terms": ", ".join(matches) or "None",
                    "Marker Frequency": frequency,
                    "Marker Density (%)": round(score, 2),
                    "Explanation": explanation
                })

            df = pd.DataFrame(results)

            st.subheader("Dynamic Theoretical Index")
            st.dataframe(df, use_container_width=True)

            st.subheader("Theoretical Marker Density")

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

            st.caption(
                "These are operationalized lexical proxies for theoretical "
                "concepts, not direct measurements of philosophical constructs."
            )


# =============================================================================
# 15. MODULE 10: VALIDATION PROTOCOL
# =============================================================================

elif selected_module == "📊 Validation Protocol":

    st.title("📊 Validation Protocol & Empirical Design")

    corpus = get_corpus_input(
        "Enter corpus for validation:",
        "validation_corpus"
    )

    if st.button("⚡ Generate Validation Dataset", key="validation"):

        results = analyze_corpus(corpus, w_evasion, w_compression)

        if not results:
            st.warning("Enter a corpus first.")
        else:
            validation_df = pd.DataFrame([
                {
                    "Beat": r["beat"],
                    "Speaker": r["speaker"],
                    "Text": r["text"],
                    "Engine Classification": r["category"],
                    "Tension": r["tension"]
                }
                for r in results
            ])

            st.session_state["validation_data"] = validation_df

            st.subheader("Generated Annotation Dataset")
            st.dataframe(validation_df, use_container_width=True)

            labels = list(CLASS_COLORS.keys())

            st.subheader("Human Annotation")

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

                observed_disagreement = sum(
                    x["Annotator A"] != x["Annotator B"]
                    for x in complete
                ) / len(complete)

                pooled = [
                    x["Annotator A"] for x in complete
                ] + [
                    x["Annotator B"] for x in complete
                ]

                frequencies = Counter(pooled)
                n = len(pooled)

                expected_disagreement = (
                    1 - sum(
                        (count / n) ** 2
                        for count in frequencies.values()
                    )
                ) if n else 0

                alpha = (
                    1 - observed_disagreement / expected_disagreement
                    if expected_disagreement > 0 else None
                )

                st.divider()
                st.subheader("Inter-Annotator Reliability")

                st.metric(
                    "Observed Agreement",
                    f"{(1-observed_disagreement)*100:.1f}%"
                )

                if alpha is not None:
                    st.metric(
                        "Krippendorff's Alpha (Nominal)",
                        round(alpha, 3)
                    )
                else:
                    st.info(
                        "Alpha cannot be estimated when expected "
                        "disagreement is zero."
                    )

                st.caption(
                    "This is a two-annotator nominal disagreement estimate "
                    "using the standard pooled-category formulation. "
                    "It should be interpreted cautiously with small samples."
                )

            else:
                st.info(
                    "Complete both annotators' labels for at least one beat "
                    "to calculate agreement."
                )


# =============================================================================
# 16. MODULE 11: CORE ARTIFACT & LIMITATIONS
# =============================================================================

elif selected_module == "📜 Core Artifact & Limitations":

    st.title("📜 Core Artifact & Methodological Limitations")

    corpus = get_corpus_input(
        "Enter text to generate a methodological report:",
        "artifact_corpus"
    )

    if st.button("⚡ Generate Corpus Report", key="artifact"):

        results = analyze_corpus(corpus, w_evasion, w_compression)

        if not results:
            st.warning("No corpus available.")
        else:
            metrics = corpus_metrics(results)

            categories = Counter(
                r["category"] for r in results
            )

            report = {
                "Generation Date": datetime.datetime.now().isoformat(
                    timespec="seconds"
                ),
                "Total Beats": metrics["turns"],
                "Total Words": metrics["words"],
                "Unique Words": metrics["unique_words"],
                "Number of Speakers": metrics["speakers"],
                "Mean Tension": metrics["average_tension"],
                "Maximum Tension": metrics["maximum_tension"],
                "Minimum Tension": metrics["minimum_tension"],
                "Detected Questions": metrics["questions"],
                "Dominant Classification": (
                    categories.most_common(1)[0][0]
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

            st.subheader("Classification Frequencies")

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
                "Polysemy and context can produce false positive classifications.",
                "Irony, metaphor, sarcasm and cultural nuances may be missed.",
                "The current engine uses rule-based heuristics rather than a trained NLP model.",
                "Tension values are relative computational indicators, not validated psychological measurements.",
                "Theoretical markers are simplified operational proxies.",
                "Speaker dominance does not necessarily equal actual social power.",
                "Reliable academic validation requires independent human annotators and a representative corpus."
            ]

            for limitation in limitations:
                st.markdown(f"- {limitation}")

            st.subheader("Export Research Report")

            report_df = pd.DataFrame(
                report.items(),
                columns=["Parameter", "Result"]
            )

            csv = report_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "⬇️ Download Corpus Report (CSV)",
                data=csv,
                file_name="ontological_silence_report.csv",
                mime="text/csv"
            )

            beat_csv = pd.DataFrame(results).to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                "⬇️ Download Beat-Level Analysis (CSV)",
                data=beat_csv,
                file_name="beat_level_analysis.csv",
                mime="text/csv"
            )


# =============================================================================
# 17. GLOBAL FOOTER
# =============================================================================

st.divider()

st.markdown(
    """
    <p style="text-align:center; color:#8b949e; font-size:11px;">
    ONTOLOGICAL SILENCE & PARANOIA ENGINE |
    DYNAMIC COMPUTATIONAL DRAMATURGY RESEARCH PROTOTYPE |
    AGIL CHIRAGLI
    </p>
    """,
    unsafe_allow_html=True
)
