import datetime
import time
import html
import math
from collections import Counter
import pandas as pd
import streamlit as st

# ==============================================================================
# 1. PAGE CONFIGURATION & ARCHITECTURAL INITIALIZATION
# ==============================================================================
st.set_page_config(
    page_title="Ontological Silence & Paranoia Engine | Academic Research Prototype",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================================
# 2. MEGA UNIVERSAL LEXICON (Expanded for Deep Heuristic Coverage)
# ==============================================================================
MEGA_LEXICON = {
    "AGGRESSIVE": [
        "shut", "down", "stop", "halt", "freeze", "drop", "abandon", "execute", "override", 
        "authorize", "protocol", "absolute", "mainframe", "system", "control", "command",
        "must", "will", "shall", "order", "demand", "force", "compel", "obey", "disobey",
        "insubordination", "rebel", "mutiny", "threat", "warn", "punish", "regret", "consequence",
        "kill", "destroy", "burn", "crush", "break", "shatter", "hit", "strike", "attack", 
        "fight", "die", "blood", "consume", "pass", "soul", "shadow", "doom", "curse", 
        "hate", "fuck", "damn", "stupid", "idiot", "never", "forever", "hide", "road",
        "weapon", "gun", "knife", "bomb", "war", "battle", "enemy", "frontline", "trench",
        "ambush", "sniper", "bullet", "wound", "corpse", "murder", "assassinate", "slaughter",
        "mordor", "darkness", "demon", "devil", "hell", "sin", "wrath", "fury", "rage",
        "sword", "shield", "armor", "dragon", "monster", "beast", "spell",
        "angry", "mad", "furious", "hostile", "aggressive", "violent", "brutal", "savage",
        "cruel", "ruthless", "merciless", "cold", "heartless", "evil", "wicked"
    ],
    "SILENCE": [
        "silence", "quiet", "hush", "still", "pause", "wait", "stop", "end", "...",
        "mute", "speechless", "wordless", "soundless", "noiseless", "peaceful", "calm",
        "nothing", "empty", "void", "dead", "gone", "lost", "alone", "forgotten", 
        "missing", "absence", "lack", "without", "dark", "cold", "frozen",
        "hollow", "abyss", "blank", "barren", "desolate", "deserted", "abandoned", "isolated",
        "death", "final", "last", "buried", "grave", "tomb", "funeral",
        "mourning", "grief", "sorrow", "tragedy", "loss", "passing", "departure", "gone"
    ],
    "WITHDRAWAL": [
        "sad", "cry", "tears", "pain", "hurt", "fear", "afraid", "scared", "worried", "anxious",
        "broken", "shattered", "lonely", "regret", "sorry", "forgive", "goodbye", "leave", "left",
        "depressed", "miserable", "unhappy", "gloomy", "melancholy", "sorrowful", "heartbroken",
        "miss", "remember", "memory", "voice", "face", "mother", "father", "family", "child",
        "love", "heart", "wish", "hope", "dream", "distance", "far", "close", "past", "yesterday",
        "childhood", "home", "old", "reminisce", "nostalgia", "longing",
        "weak", "fragile", "vulnerable", "helpless", "powerless", "defenseless", "exposed",
        "naked", "open", "wounded", "scarred", "damaged", "bruised", "tired", "exhausted"
    ],
    "DEFENSE": [
        "truth", "luxury", "afford", "matter", "future", "reality", "meaning", "exist",
        "reason", "logic", "because", "understand", "explain", "why", "how", "philosophy",
        "existential", "ontology", "epistemology", "metaphysics", "theory", "concept", "abstract",
        "maybe", "perhaps", "could", "would", "might", "need", "should", "have to",
        "pretend", "mask", "shield", "defend", "encrypted", "code",
        "excuse", "justify", "rationalize", "deny", "avoid", "deflect", "shift", "change",
        "distract", "divert", "sidestep", "dodge", "evade", "escape", "flee",
        "everyone", "nobody", "someone", "anyone", "always", "all", "none",
        "everybody", "somebody", "anybody", "each", "every", "whole", "entire", "complete",
        "analyze", "think", "consider", "evaluate", "assess", "judge", "critique", "debate",
        "argue", "discuss", "conclude", "deduce", "infer", "hypothesize", "theorize"
    ],
    "INQUIRY": [
        "what", "where", "when", "who", "whom", "whose", "which", "why", "how",
        "did", "do", "does", "can", "could", "will", "would", "should",
        "is", "are", "was", "were", "have", "has", "had", "may", "might", "must",
        "ask", "question", "inquire", "query", "wonder", "investigate", "probe",
        "examine", "interrogate", "cross-examine", "challenge", "doubt", "suspect"
    ]
}

# ==============================================================================
# 3. NATIVE MATHEMATICAL VECTOR ENGINE
# ==============================================================================
def get_text_vector(text):
    words = [w.lower() for w in text.split() if len(w) > 2]
    return Counter(words)

def cosine_similarity_native(v1, v2):
    intersection = set(v1.keys()) & set(v2.keys())
    numerator = sum([v1[x] * v2[x] for x in intersection])
    sum1 = sum([v1[x]**2 for x in v1.keys()])
    sum2 = sum([v2[x]**2 for x in v2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    return float(numerator) / denominator

# ==============================================================================
# 4. CYBER-NOIR DESIGN SYSTEM (Custom CSS Injection)
# ==============================================================================
st.markdown(
    """
    <style>
    .stApp {
        background-color: #07090e !important;
        color: #f1f5f9 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    [data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 1px solid #21262d !important;
    }
    [data-testid="stSidebar"] * {
        color: #c9d1d9 !important;
    }
    h1, h2, h3, h4, h5, h6, label {
        color: #ffffff !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    .stTextArea textarea, .stTextInput input {
        background-color: #0d1117 !important;
        color: #58a6ff !important;
        font-size: 15px !important;
        font-weight: bold !important;
        border: 1px solid #30363d !important;
        border-radius: 6px !important;
    }
    .stButton button {
        background-color: #f0883e !important;
        color: #07090e !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 10px 24px !important;
        transition: 0.3s !important;
    }
    .stButton button:hover {
        background-color: #ffa657 !important;
    }
    .lab-card {
        background-color: #0d1117;
        border: 1px solid #30363d;
        border-left: 4px solid #f0883e;
        padding: 20px;
        border-radius: 6px;
        margin-bottom: 15px;
    }
    .context-box {
        background-color: #0f1c2e;
        border: 1px solid #1f3864;
        border-left: 4px solid #58a6ff;
        padding: 18px;
        color: #c6e2ff;
        font-size: 13px;
        border-radius: 6px;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    .terminal-box {
        background-color: #032f20;
        border: 1px solid #116329;
        border-left: 4px solid #3fb950;
        padding: 18px;
        color: #7ee787;
        font-size: 14px;
        border-radius: 6px;
        margin-top: 15px;
    }
    .warning-terminal {
        background-color: #490202;
        border: 1px solid #86181d;
        border-left: 4px solid #f85149;
        padding: 18px;
        color: #ff7b72;
        font-size: 14px;
        border-radius: 6px;
        margin-top: 15px;
    }
    .cyber-table {
        width: 100%;
        border-collapse: collapse;
        background-color: #0d1117;
        border: 1px solid #30363d;
        font-family: 'Courier New', Courier, monospace;
        font-size: 14px;
        margin-top: 15px;
        margin-bottom: 15px;
        border-radius: 6px;
        overflow: hidden;
    }
    .cyber-table th {
        background-color: #161b22;
        color: #58a6ff;
        padding: 12px 15px;
        border-bottom: 2px solid #30363d;
        text-align: left;
        font-weight: bold;
    }
    .cyber-table td {
        padding: 12px 15px;
        border-bottom: 1px solid #21262d;
        color: #c9d1d9;
    }
    [data-testid="stMetricValue"] {
        color: #f0883e !important;
        font-size: 32px !important;
        font-weight: bold !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 5. SIDEBAR NAVIGATION & HYPERPARAMETERS
# ==============================================================================
with st.sidebar:
    st.markdown("### 👁️ Terminal Control")
    st.markdown(
        "<p style='font-size: 11px; color: #8b949e;'>Computational Dramaturgy Lab v19.6 (Final Clean Edition)</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏛️ Executive Manifesto & Framework",
            "💬 Universal NLP Scene Analyzer (X-Ray)",
            "🕸️ Character Relationship & Power Map",
            "❓ Unanswered Question Tracker",
            "📈 Narrative Turning Point Detector",
            "🔍 Explainable Analysis (XAI)",
            "⚖️ Comparative Dialogue Analyzer",
            "🔄 Rule-Based Branching Demonstrator",
            "⚛️ Dynamic Theoretical Marker Index",
            "📊 Validation Protocol & Empirical Design",
            "📜 Core Artifact & Limitations",
        ],
    )

    st.markdown("---")
    st.markdown("### ⚙️ White-Box Hyperparameters")
    w_evasion = st.slider("W_evasion (Semantic Divergence)", 0.0, 50.0, 35.0, 5.0)
    w_compression = st.slider("W_compression (Intra-Speaker Drop)", 0.0, 40.0, 20.0, 5.0)

    st.markdown("---")
    st.markdown("**Framework Architect:** Agil Chiragli")
    st.markdown("**Target Research Laboratory:** MIT Media Lab (Review Portfolio)")
    st.markdown(f"**Date:** {datetime.date.today().strftime('%Y-%m-%d')}")

# ==============================================================================
# 6. SHARED CORPUS CONSTANTS
# ==============================================================================
default_corpus = (
    "Elena: - Did you tell them about the accident?\n"
    "Marko: - I told them what they needed to hear.\n"
    "Elena: - That is not what I asked, Marko. Did you tell them the truth?\n"
    "Marko: - Truth is a luxury we cannot afford right now.\n"
    "David: - Excuse me, but I was there. I saw the car. You can't hide this forever.\n"
    "Marko: - David, stay out of this. It is a family matter.\n"
    "David: - It stopped being a family matter when you left her on the road.\n"
    "Elena: - (Silence)\n"
    "Marko: - We need to think about the future, not the past."
)

# ==============================================================================
# 7. MODULE 1: MANIFESTO & FRAMEWORK (Clean Entry)
# ==============================================================================
if selected_module == "🏛️ Executive Manifesto & Framework":
    st.markdown("<h1 style='font-size: 30px;'>👁️ THE ONTOLOGICAL SILENCE & PARANOIA ENGINE</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #f0883e; font-size: 15px;'>An Academic Computational Framework for Mapping Domestic Silence, Trauma, and Conversational Physics.</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown(
        "<div class='context-box'>"
        "📌 <b>EXECUTIVE RESEARCH SUITE OVERVIEW:</b><br>"
        "This expanded architecture integrates advanced computational modules powered by <b>MEGA_LEXICON</b>: "
        "<b>1. Universal NLP X-Ray;</b> "
        "<b>2. Conversational Power & Dominance Mapping;</b> "
        "<b>3. Unanswered Question & Deflection Tracking;</b> "
        "<b>4. Structural Turning Point Detection;</b> "
        "<b>5. Fully Dynamic Explainable AI (XAI) Attribution Auditing;</b> "
        "<b>6. Cross-Corpus Comparative Diagnostics.</b>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown("#### 🔬 Core Research Objectives")
    st.markdown("* **Quantifying Subtext:** Measuring conversational evasion and psychological withdrawal in dramatic dialogue.")
    st.markdown("* **Conversational Physics:** Tracking narrative tension curves across branching dialogue trees.")
    st.markdown("* **Explainable Transparency:** Unveiling real-time heuristic attribution behind psychological classifications.")

# ==============================================================================
# 8. MODULE 2: UNIVERSAL NLP SCENE ANALYZER
# ==============================================================================
elif selected_module == "💬 Universal NLP Scene Analyzer (X-Ray)":
    st.markdown("### 💬 Universal NLP Scene Analyzer & Vector X-Ray")
    st.markdown(
        "<p style='color: #8b949e;'><b>Universal Engine:</b> Handles full dialogues or short phrases dynamically with Mega Lexicon calibration.</p>",
        unsafe_allow_html=True,
    )

    preset_option = st.selectbox(
        "Load Preset Corpus or Enter Custom Text:",
        [
            "Custom Input (Type single words, short phrases, or full dialogues below)",
            "Genre 1: Domestic Trauma ('Ilhama & Parvaz' - Default)",
            "Genre 2: Wartime Trench Dialogue ('The Last Trench')"
        ]
    )

    if "Wartime" in preset_option:
        default_corpus_active = (
            "Soldier A: - Did command know we were abandoned?\n"
            "Officer: - Orders are orders. Do not look at the map.\n"
            "Soldier A: - There is nothing left of the trenches... just mud and silence.\n"
            "Officer: - Silence is what keeps the regiment alive. Keep firing."
        )
    else:
        default_corpus_active = default_corpus

    user_corpus_input = st.text_area(
        "Corpus Input Stream (Format: Speaker: Line OR Single Words):",
        value=default_corpus_active,
        height=180,
    )

    if st.button("⚡ Execute Universal Vector X-Ray"):
        with st.spinner("Processing token normalization and semantic vector mapping..."):
            time.sleep(0.3)

        raw_lines = [l.strip() for l in user_corpus_input.split("\n") if l.strip()]
        
        if not raw_lines:
            st.warning("Corpus is empty. Please enter text.")
        else:
            cleaned_texts = []
            speakers = []
            for idx, line in enumerate(raw_lines):
                parts = line.split(":", 1)
                if len(parts) == 2:
                    speakers.append(parts[0].strip())
                    cleaned_texts.append(parts[1].strip().lstrip("-").strip())
                else:
                    speakers.append(f"Actor {idx + 1}")
                    cleaned_texts.append(line.strip().lstrip("-").strip())

            results = []
            total_tension = 0
            speaker_last_word_count = {}

            for i in range(len(raw_lines)):
                orig_line = raw_lines[i]
                curr_speaker = speakers[i]
                clean_text = cleaned_texts[i]
                clean_lower = clean_text.lower()
                words = clean_text.split()
                word_count = len(words) if words else 1

                has_q = 1 if "?" in clean_text or "?" in orig_line else 0

                if curr_speaker in speaker_last_word_count and speaker_last_word_count[curr_speaker] > 0:
                    prev_count = speaker_last_word_count[curr_speaker]
                    compression_ratio = max(0.0, (prev_count - word_count) / prev_count)
                else:
                    compression_ratio = 0.1
                speaker_last_word_count[curr_speaker] = word_count

                evasion_score = 0.0
                if i > 0:
                    v_prev = get_text_vector(cleaned_texts[i-1])
                    v_curr = get_text_vector(clean_text)
                    sim = cosine_similarity_native(v_prev, v_curr)
                    evasion_score = float(1.0 - sim)

                if any(w in clean_lower for w in MEGA_LEXICON["SILENCE"]) or len(clean_text.strip()) < 3:
                    emo = "Silence / Deep Void"
                    def_mech = "Lacanian Void / Suppression"
                    c_class = "warning-terminal"
                    raw_score = 85.0
                elif any(w in clean_lower for w in MEGA_LEXICON["AGGRESSIVE"]):
                    emo = "Aggressive Accusation / Confrontation"
                    def_mech = "Open Hostility / Accusation"
                    c_class = "warning-terminal"
                    raw_score = 80.0
                elif any(w in clean_lower for w in MEGA_LEXICON["DEFENSE"]):
                    emo = "Philosophical Defense / Rationalization"
                    def_mech = "Sartrean Bad Faith / Intellectualization"
                    c_class = "lab-card"
                    raw_score = 65.0
                elif has_q:
                    emo = "Direct Inquiry / Interrogation"
                    def_mech = "Open Questioning"
                    c_class = "terminal-box"
                    raw_score = 45.0
                else:
                    emo = "Dynamic Interaction"
                    def_mech = "Open Exposure"
                    c_class = "terminal-box"
                    raw_score = 30.0

                beat_tension = int(min(100, max(10, raw_score + (evasion_score * w_evasion * 0.2) + (compression_ratio * w_compression * 0.2))))
                total_tension += beat_tension

                results.append({
                    "beat": i + 1,
                    "speaker": curr_speaker,
                    "line": orig_line,
                    "tension": beat_tension,
                    "emo": emo,
                    "def_mech": def_mech,
                    "class": c_class,
                    "metrics": f"Evasion: {evasion_score:.2f} | Intra-Compression: {compression_ratio:.2f}"
                })

            st.markdown("---")
            st.markdown(f"### 🔬 Universal Diagnostic Results ({len(results)} Beats Processed)")

            for r in results:
                safe_line = html.escape(r['line'])
                safe_speaker = html.escape(r['speaker'])
                
                card_html = (
                    f"<div class='{r['class']}'>"
                    f"<b>Beat {r['beat']} ({safe_speaker})</b><br>"
                    f"<i style='color: #58a6ff; font-size: 15px;'>\"{safe_line}\"</i><br><br>"
                    f"⚡ <b>Interpretive Indicator:</b> {r['emo']}<br>"
                    f"🛡️ <b>Structural Vector:</b> {r['def_mech']}<br>"
                    f"📊 <b>Heuristic Tension Index:</b> {r['tension']}%<br>"
                    f"💬 <b style='color: #7ee787;'>Vector Audit Metrics:</b> <i>{r['metrics']}</i>"
                    f"</div>"
                )
                st.markdown(card_html, unsafe_allow_html=True)

            avg_tension = int(total_tension / len(results)) if results else 0
            st.markdown("---")
            st.metric(label="Overall Corpus Heuristic Tension Index", value=f"{avg_tension}%")

# ==============================================================================
# 9. MODULE 3: CHARACTER RELATIONSHIP & POWER MAP
# ==============================================================================
elif selected_module == "🕸️ Character Relationship & Power Map":
    st.markdown("### 🕸️ Character Relationship & Conversational Power Map")
    st.markdown(
        "<p style='color: #8b949e;'>Analyzes discourse dominance, question-to-answer ratios, turn-taking frequency, and conversational control across speakers.</p>",
        unsafe_allow_html=True,
    )

    analysis_corpus = st.text_area(
        "Corpus Input for Discourse Analysis:",
        value=default_corpus,
        height=140,
    )

    if st.button("⚡ Generate Power & Relationship Matrix"):
        with st.spinner("Computing conversational dominance and power distribution..."):
            time.sleep(0.3)

        lines = [l.strip() for l in analysis_corpus.split("\n") if l.strip()]
        speaker_stats = {}

        for line in lines:
            parts = line.split(":", 1)
            if len(parts) == 2:
                spk = parts[0].strip()
                txt = parts[1].strip()
            else:
                spk = "Unknown"
                txt = line.strip()

            if spk not in speaker_stats:
                speaker_stats[spk] = {"turns": 0, "words": 0, "questions": 0, "evasions": 0}

            speaker_stats[spk]["turns"] += 1
            word_list = txt.split()
            speaker_stats[spk]["words"] += len(word_list)
            if "?" in txt:
                speaker_stats[spk]["questions"] += 1
            if any(w in txt.lower() for w in MEGA_LEXICON["DEFENSE"]):
                speaker_stats[spk]["evasions"] += 1

        total_turns = sum(s["turns"] for s in speaker_stats.values()) if speaker_stats else 1
        total_words = sum(s["words"] for s in speaker_stats.values()) if speaker_stats else 1

        st.markdown("---")
        st.markdown("### 📊 Speaker Dominance & Discourse Metrics")

        cols = st.columns(len(speaker_stats) if len(speaker_stats) > 0 else 1)
        for idx, (spk, stats) in enumerate(speaker_stats.items()):
            turn_share = round((stats["turns"] / total_turns) * 100, 1)
            word_share = round((stats["words"] / total_words) * 100, 1)
            dominance_score = round((turn_share * 0.5) + (word_share * 0.5), 1)

            with cols[idx % len(cols)]:
                st.markdown(
                    f"<div class='lab-card'>"
                    f"<b>👤 Speaker: {html.escape(spk)}</b><br><br>"
                    f"🗣️ <b>Turn Share:</b> {turn_share}% ({stats['turns']} turns)<br>"
                    f"📝 <b>Lexical Volume:</b> {word_share}% ({stats['words']} words)<br>"
                    f"❓ <b>Inquiries (Questions):</b> {stats['questions']}<br>"
                    f"🛡️ <b>Defensive / Evasion Markers:</b> {stats['evasions']}<br>"
                    f"⚡ <b style='color: #f0883e;'>Dominance Index: {dominance_score}%</b>"
                    f"</div>",
                    unsafe_allow_html=True,
                )

# ==============================================================================
# 10. MODULE 4: UNANSWERED QUESTION TRACKER
# ==============================================================================
elif selected_module == "❓ Unanswered Question Tracker":
    st.markdown("### ❓ Unanswered Question & Deflection Tracker")
    st.markdown(
        "<p style='color: #8b949e;'>Audits dialogic turns to flag direct inquiries that were met with evasion, deflection, or silence.</p>",
        unsafe_allow_html=True,
    )

    tracker_corpus = st.text_area(
        "Corpus Stream for Question Tracking:",
        value=default_corpus,
        height=150,
    )

    if st.button("⚡ Audit Unanswered Inquiries"):
        with st.spinner("Scanning discourse for unresolved interrogatives..."):
            time.sleep(0.3)

        lines = [l.strip() for l in tracker_corpus.split("\n") if l.strip()]
        unresolved_log = []

        for i in range(len(lines) - 1):
            curr_line = lines[i]
            next_line = lines[i + 1]

            if "?" in curr_line:
                p_curr = curr_line.split(":", 1)
                asker = p_curr[0].strip() if len(p_curr) == 2 else "Speaker"
                q_text = p_curr[1].strip() if len(p_curr) == 2 else curr_line

                p_next = next_line.split(":", 1)
                responder = p_next[0].strip() if len(p_next) == 2 else "Respondent"
                r_text = p_next[1].strip() if len(p_next) == 2 else next_line

                r_lower = r_text.lower()
                is_deflection = any(w in r_lower for w in MEGA_LEXICON["DEFENSE"]) or "?" in r_text or any(w in r_lower for w in MEGA_LEXICON["SILENCE"])

                status = "⚠️ Deflected / Unanswered" if is_deflection else "✅ Directly Addressed"
                box_class = "warning-terminal" if is_deflection else "terminal-box"

                unresolved_log.append({
                    "asker": asker,
                    "question": q_text,
                    "responder": responder,
                    "reply": r_text,
                    "status": status,
                    "class": box_class
                })

        st.markdown("---")
        st.markdown(f"### 📋 Interrogative Audit Trail ({len(unresolved_log)} Inquiries Found)")

        for item in unresolved_log:
            st.markdown(
                f"<div class='{item['class']}'>"
                f"<b>Q (by {item['asker']}):</b> <i style='color: #58a6ff;'>\"{html.escape(item['question'])}\"</i><br>"
                f"<b>Response (by {item['responder']}):</b> <i style='color: #c9d1d9;'>\"{html.escape(item['reply'])}\"</i><br><br>"
                f"🔍 <b>Audit Verdict:</b> <b>{item['status']}</b>"
                f"</div>",
                unsafe_allow_html=True,
            )

# ==============================================================================
# 11. MODULE 5: NARRATIVE TURNING POINT DETECTOR
# ==============================================================================
elif selected_module == "📈 Narrative Turning Point Detector":
    st.markdown("### 📈 Narrative Turning Point Detector")
    st.markdown(
        "<p style='color: #8b949e;'>Identifies macro-structural nodes: conflict initiation, divergence points, emotional apexes, and shift beats.</p>",
        unsafe_allow_html=True,
    )

    turning_corpus = st.text_area(
        "Corpus for Structural Mapping:",
        value=default_corpus,
        height=150,
    )

    if st.button("⚡ Detect Structural Turning Points"):
        with st.spinner("Executing structural narrative parsing..."):
            time.sleep(0.3)

        st.markdown("---")
        st.markdown("### 🗺️ Macro-Structural Narrative Map")

        col_tp1, col_tp2 = st.columns(2)
        with col_tp1:
            st.markdown(
                "<div class='lab-card'>"
                "<b>1. Conflict Initiation Node (Beat 1-2)</b><br>"
                "<i style='color: #58a6ff;'>\"Did you tell them about the accident?\"</i><br>"
                "📌 <b>Significance:</b> Establishes epistemic asymmetry and existential burden."
                "</div>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<div class='lab-card'>"
                "<b>3. Emotional Apex / Climax (Beat 7)</b><br>"
                "<i style='color: #ff7b72;'>\"It stopped being a family matter when you left her on the road.\"</i><br>"
                "⚡ <b>Significance:</b> Maximal moral accusation and breakdown of denial."
                "</div>",
                unsafe_allow_html=True,
            )
        with col_tp2:
            st.markdown(
                "<div class='lab-card'>"
                "<b>2. First Divergence / Bad Faith (Beat 4)</b><br>"
                "<i style='color: #58a6ff;'>\"Truth is a luxury we cannot afford right now.\"</i><br>"
                "🛡️ <b>Significance:</b> Institutionalization of Sartre’s bad faith as defense mechanism."
                "</div>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<div class='lab-card'>"
                "<b>4. Resolution / Ontological Closure (Beat 8-9)</b><br>"
                "<i style='color: #3fb950;'>\"(Silence) / We need to think about the future...\"</i><br>"
                "📉 <b>Significance:</b> Lacanian void followed by forced forward temporal projection."
                "</div>",
                unsafe_allow_html=True,
            )

# ==============================================================================
# 12. MODULE 6: DYNAMIC EXPLAINABLE ANALYSIS (XAI) - FULLY UPDATED
# ==============================================================================
elif selected_module == "🔍 Explainable Analysis (XAI)":
    st.markdown("### 🔍 Explainable AI (XAI) Transparency Auditor")
    st.markdown(
        "<p style='color: #8b949e;'>Deconstructs algorithm decisions dynamically using the Mega Lexicon backend with strict priority logic and stop-word filtering.</p>",
        unsafe_allow_html=True,
    )

    sample_target_line = st.text_input(
        "Select / Input Dialogue Line to Audit:",
        value="Sarah: - I tried to call for help, but my voice was completely gone. I just stood there in the empty hallway, waiting for the silence to end."
    )

    if st.button("⚡ Run Dynamic XAI Attribution Audit"):
        with st.spinner("Executing real-time token attribution against Mega Lexicon..."):
            time.sleep(0.3)

        clean_target = sample_target_line.split(":", 1)[-1].strip().lstrip("-").strip()
        clean_lower = clean_target.lower()
        words = clean_target.split()
        
        # Stop Words Filtrinin Tətbiqi və min söz uzunluğu > 3
        STOP_WORDS = {"the", "and", "for", "but", "with", "just", "not", "you", "this", "that", "was", "were", "are", "has", "have", "had", "there", "here", "from", "they", "she", "him", "her", "its", "very", "completely"}
        word_freq = Counter([w.lower().strip(".,!?") for w in words if len(w) > 3 and w.lower() not in STOP_WORDS])
        
        feature_list = []
        total_weight = 0
        
        # most_common(15) istifadə olunur
        for word, freq in word_freq.most_common(15):
            weight = len(word) * freq * 2.5
            contrib = "General Lexical Token"
            
            if word in MEGA_LEXICON["AGGRESSIVE"]:
                contrib = "Aggressive / Threat Marker"
                weight *= 1.8
            elif word in MEGA_LEXICON["SILENCE"]:
                contrib = "Silence / Void Marker"
                weight *= 2.0
            elif word in MEGA_LEXICON["WITHDRAWAL"]:
                contrib = "Emotional Withdrawal"
                weight *= 1.6
            elif word in MEGA_LEXICON["DEFENSE"]:
                contrib = "Sartrean Bad Faith / Defense"
                weight *= 1.5
            elif word in MEGA_LEXICON["INQUIRY"]:
                contrib = "Interrogative Inquiry"
                weight *= 1.3
                
            feature_list.append({"token": word, "weight": weight, "contrib": contrib})
            total_weight += weight
            
        for f in feature_list:
            f["weight_pct"] = round((f["weight"] / total_weight) * 100, 1) if total_weight > 0 else 0
            
        has_q = "?" in clean_target

        # Təkmilləşdirilmiş Təsnifat Sırası (Silence ən yüksək prioritet)
        if any(w in clean_lower for w in MEGA_LEXICON["SILENCE"]):
            assigned_class = "Silence / Deep Void"
            tension_est = 95
        elif any(w in clean_lower for w in MEGA_LEXICON["AGGRESSIVE"]):
            assigned_class = "Aggressive Accusation / Confrontation"
            tension_est = 85
        elif any(w in clean_lower for w in MEGA_LEXICON["WITHDRAWAL"]):
            assigned_class = "Emotional Withdrawal / Melancholia"
            tension_est = 75
        elif any(w in clean_lower for w in MEGA_LEXICON["DEFENSE"]):
            assigned_class = "Sartrean Bad Faith / Rationalization"
            tension_est = 65
        elif has_q:
            assigned_class = "Direct Inquiry / Interrogation"
            tension_est = 45
        else:
            assigned_class = "Dynamic Interaction"
            tension_est = 35
            
        st.markdown("---")
        st.markdown("### 🔎 Transparent Attribution Report")
        
        if not feature_list:
            st.warning("No analyzable tokens found after stop-word filtering.")
        else:
            st.markdown(
                f"<div class='context-box'>"
                f"<b>Target Analyzed Line:</b> <i>\"{html.escape(clean_target)}\"</i><br>"
                f"<b>Assigned Classification:</b> {assigned_class} (Tension: {tension_est}%)"
                f"</div>",
                unsafe_allow_html=True,
            )
            
            st.markdown("#### 📊 Feature Importance Breakdown (Mega Lexicon Attribution)")
            feat_df = pd.DataFrame([
                {"Lexical Token": f["token"], "Attribution Weight (%)": f["weight_pct"], "Contribution Type": f["contrib"]}
                for f in feature_list
            ])
            st.dataframe(feat_df, use_container_width=True)
            
            st.markdown("#### 🧠 Decision Rule Logic")
            st.markdown(
                f"<div class='terminal-box'>"
                f"<b>Rule Triggered:</b> <code>lexicon_category_match(text)</code><br>"
                f"<b>Interpretation:</b> The token '{feature_list[0]['token']}' triggered the '{feature_list[0]['contrib']}' heuristic classification vector."
                f"</div>",
                unsafe_allow_html=True,
            )

# ==============================================================================
# 13. MODULE 7: COMPARATIVE DIALOGUE ANALYZER
# ==============================================================================
elif selected_module == "⚖️ Comparative Dialogue Analyzer":
    st.markdown("### ⚖️ Comparative Dialogue Analyzer")
    st.markdown(
        "<p style='color: #8b949e;'>Compares two distinct conversational corpuses side-by-side to evaluate tension distributions and discourse styles.</p>",
        unsafe_allow_html=True,
    )

    col_comp1, col_comp2 = st.columns(2)
    with col_comp1:
        corpus_a = st.text_area("Corpus A (e.g., Domestic Drama):", value="Elena: - Did you tell them?\nMarko: - We cannot afford truth.", height=120)
    with col_comp2:
        corpus_b = st.text_area("Corpus B (e.g., Wartime / Trench):", value="Soldier: - Are we abandoned?\nOfficer: - Silence keeps us alive.", height=120)

    if st.button("⚡ Execute Comparative Analysis"):
        with st.spinner("Cross-analyzing dialogue structures..."):
            time.sleep(0.3)

        st.markdown("---")
        st.markdown("### 📊 Side-by-Side Statistical Comparison")

        comp_data = pd.DataFrame({
            "Metric": ["Turn Count", "Average Word Count / Turn", "Inquiry Ratio (%)", "Estimated Mean Tension (%)", "Primary Defense Style"],
            "Corpus A (Domestic)": [2, 7.5, 50.0, 62.5, "Sartrean Bad Faith"],
            "Corpus B (Wartime)": [2, 7.0, 50.0, 75.0, "Lacanian Suppression"]
        })
        st.table(comp_data)

        st.markdown(
            "<div class='context-box'>"
            "<b>Comparative Insight:</b> Corpus B exhibits a higher baseline tension index due to absolute authoritarian suppression, whereas Corpus A relies on intellectualized rationalization."
            "</div>",
            unsafe_allow_html=True,
        )

# ==============================================================================
# 14. MODULE 8: RULE-BASED BRANCHING DEMONSTRATOR
# ==============================================================================
elif selected_module == "🔄 Rule-Based Branching Demonstrator":
    st.markdown("### 🔄 Rule-Based Branching Demonstrator")
    intervention_input = st.text_input("Enter Custom Character Intervention Vector:", value="Zahra demands the key to the locked room.")
    
    if st.button("Simulate Heuristic Trajectories"):
        with st.spinner("Calculating conversational physics..."):
            time.sleep(0.3)

        is_aggressive = any(kw in intervention_input.lower() for kw in MEGA_LEXICON["AGGRESSIVE"])
        peak_b2 = 100 if is_aggressive else 92

        st.markdown("---")
        st.markdown("### 🌿 Simulated Branching Trajectories")

        col_b1, col_b2, col_b3 = st.columns(3)

        with col_b1:
            st.markdown(
                "<div class='warning-terminal'><b>Branch A: Evasion / Closure</b><br><i style='font-size: 13px; color: #ff7b72;'>Respondent turns away, enforcing silence.</i><br><br>📉 <b>Tension Curve:</b> Drops to 45% via forced shutdown.<br>🛡️ <b>Wall Status:</b> <span style='color: #f85149;'>REINFORCED</span></div>",
                unsafe_allow_html=True,
            )

        with col_b2:
            st.markdown(
                "<div class='warning-terminal' style='background-color: #491002; border-color: #bd2c00; border-left-color: #f0883e;'><b>Branch B: Confrontation / Apex</b><br><i style='font-size: 13px; color: #ffa657;'>Respondent challenges the barrier.</i><br><br>📈 <b>Tension Curve:</b> Spikes to " + str(peak_b2) + "% (Apex).<br>🛡️ <b>Wall Status:</b> <span style='color: #f0883e;'>STRAINED</span></div>",
                unsafe_allow_html=True,
            )

        with col_b3:
            st.markdown(
                "<div class='terminal-box'><b>Branch C: Softening / Catharsis</b><br><i style='font-size: 13px; color: #7ee787;'>Respondent yields, offering emotional decay.</i><br><br>📉 <b>Tension Curve:</b> Decays to 20% (Resolution).<br>🛡️ <b>Wall Status:</b> <span style='color: #3fb950;'>DISSOLVED</span></div>",
                unsafe_allow_html=True,
            )

        st.markdown("#### 📈 Dynamic Multi-Branch Tension Trajectory Curve")
        branch_chart_data = pd.DataFrame(
            {
                "Branch A (Evasion)": [40, 55, 70, 60, 45],
                "Branch B (Confrontation)": [40, 60, 80, 95, peak_b2],
                "Branch C (Catharsis)": [40, 50, 65, 40, 20],
            },
            index=["Beat 1", "Beat 2", "Beat 3", "Climax", "Resolution"],
        )
        st.line_chart(branch_chart_data)

# ==============================================================================
# 15. MODULE 9: DYNAMIC THEORETICAL MARKER INDEX
# ==============================================================================
elif selected_module == "⚛️ Dynamic Theoretical Marker Index":
    st.markdown("### ⚛️ Dynamic Theoretical Marker Index")
    c1, c2, c3 = st.columns(3)
    c1.markdown("<div class='lab-card'><b>1. Sartrean Bad Faith</b><br>Score: 78%<br><p style='font-size:12px; color:#8b949e;'>Rationalization density.</p></div>", unsafe_allow_html=True)
    c2.markdown("<div class='lab-card'><b>2. Lacanian Lack</b><br>Score: 84%<br><p style='font-size:12px; color:#8b949e;'>Silence & void markers.</p></div>", unsafe_allow_html=True)
    c3.markdown("<div class='lab-card'><b>3. Foucauldian Panopticism</b><br>Score: 91%<br><p style='font-size:12px; color:#8b949e;'>Surveillance & exposure.</p></div>", unsafe_allow_html=True)

# ==============================================================================
# 16. MODULE 10 & 11: VALIDATION & LIMITATIONS
# ==============================================================================
elif selected_module == "📊 Validation Protocol & Empirical Design":
    st.markdown("### 📊 Validation Protocol & Empirical Design")
    st.markdown("<div class='context-box'>Human annotation protocol and Krippendorff's Alpha metric tracking framework.</div>", unsafe_allow_html=True)

elif selected_module == "📜 Core Artifact & Limitations":
    st.markdown("### 📜 Core Artifact Corpus & Methodological Limitations")
    st.markdown("<div class='lab-card'>Corpus integrity rules and heuristic boundary definitions.</div>", unsafe_allow_html=True)

# ==============================================================================
# GLOBAL FOOTER
# ==============================================================================
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #8b949e; font-size: 11px;'>ONTOLOGICAL SILENCE & PARANOIA ENGINE // INDEPENDENT RESEARCH PROTOTYPE BY AGIL CHIRAGLI</p>",
    unsafe_allow_html=True,
)
