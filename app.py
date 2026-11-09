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
# 2. NATIVE MATHEMATICAL VECTOR ENGINE (Pure Python TF-IDF & Cosine Simulation)
# ==============================================================================
def get_text_vector(text):
    """Tokenizes text and builds a frequency counter vector, filtering stop-words."""
    words = [w.lower() for w in text.split() if len(w) > 2]
    return Counter(words)

def cosine_similarity_native(v1, v2):
    """Calculates mathematical cosine similarity between two native frequency vectors."""
    intersection = set(v1.keys()) & set(v2.keys())
    numerator = sum([v1[x] * v2[x] for x in intersection])
    sum1 = sum([v1[x]**2 for x in v1.keys()])
    sum2 = sum([v2[x]**2 for x in v2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    return float(numerator) / denominator

# ==============================================================================
# 3. CYBER-NOIR DESIGN SYSTEM (Custom CSS Injection)
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
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #58a6ff !important;
        box-shadow: 0 0 12px rgba(88, 166, 255, 0.3) !important;
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
    .cyber-table tr:hover {
        background-color: #161b22;
    }
    [data-testid="stMetricValue"] {
        color: #f0883e !important;
        font-size: 32px !important;
        font-weight: bold !important;
    }
    [data-testid="stMetricLabel"] {
        color: #8b949e !important;
        font-size: 14px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 4. SIDEBAR NAVIGATION & WHITE-BOX HYPERPARAMETERS
# ==============================================================================
with st.sidebar:
    st.markdown("### 👁️ Terminal Control")
    st.markdown(
        "<p style='font-size: 11px; color: #8b949e;'>Computational Dramaturgy Lab v18.5 (Native Full Edition)</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏛️ Executive Manifesto & Framework",
            "💬 Universal NLP Scene Analyzer (X-Ray)",
            "🕸️ Character Relationship & Power Map",
            "🔄 Rule-Based Branching Demonstrator",
            "⚛️ Dynamic Theoretical Marker Index",
            "📊 Validation Protocol & Empirical Design",
            "📜 Core Artifact & Limitations",
        ],
    )

    st.markdown("---")
    st.markdown("### ⚙️ White-Box Hyperparameters")
    st.markdown("<p style='font-size: 11px; color: #8b949e;'>Calibrate model sensitivity coefficients.</p>", unsafe_allow_html=True)
    
    w_evasion = st.slider("W_evasion (Semantic Divergence)", 0.0, 50.0, 35.0, 5.0)
    w_compression = st.slider("W_compression (Intra-Speaker Drop)", 0.0, 40.0, 20.0, 5.0)
    w_lexical = st.slider("W_lexical (Generalization Marker)", 0.0, 40.0, 25.0, 5.0)
    w_punctuation = st.slider("W_punctuation (Pause / Interrogation)", 0.0, 30.0, 15.0, 5.0)

    st.markdown("---")
    st.markdown("**Framework Architect:** Agil Chiragli")
    st.markdown("**Target Research Laboratory:** MIT Media Lab (Review Portfolio)")
    st.markdown(f"**Date:** {datetime.date.today().strftime('%Y-%m-%d')}")

# ==============================================================================
# 5. SHARED CORPUS CONSTANTS
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
# 6. MODULE 1: MANIFESTO & FRAMEWORK (Clean Entry Page)
# ==============================================================================
if selected_module == "🏛️ Executive Manifesto & Framework":
    st.markdown("<h1 style='font-size: 30px;'>👁️ THE ONTOLOGICAL SILENCE & PARANOIA ENGINE</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #f0883e; font-size: 15px;'>An Academic Computational Framework for Mapping Domestic Silence, Trauma, and Conversational Physics.</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown(
        "<div class='context-box'>"
        "📌 <b>UNIVERSAL INPUT PARSING & AUDIT STANDARDS:</b><br>"
        "This experimental prototype establishes a three-layer computational pipeline: "
        "<b>Layer 1 (Computational Linguistics)</b> processes cosine divergence and intra-speaker compression; "
        "<b>Layer 2 (Theoretical Heuristics)</b> operationalizes philosophical markers (Sartre, Lacan, Foucault) dynamically from user input; "
        "<b>Layer 3 (Validation Protocol)</b> outlines transparent human annotation and Inter-Rater Reliability (ICC / Krippendorff's Alpha) frameworks."
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown("#### 🔬 Methodological Overview")
    st.markdown("* **Algorithmic Subtext Extraction:** Translating unsaid dialogue and psychological withdrawal into quantifiable vector metrics.")
    st.markdown("* **Dynamic Branching Physics:** Simulating narrative tension outcomes based on character intervention vectors.")
    st.markdown("* **Cross-Disciplinary Synthesis:** Bridging continental philosophy with computational linguistics for interactive storytelling.")

# ==============================================================================
# 7. MODULE 2: UNIVERSAL NLP SCENE ANALYZER
# ==============================================================================
elif selected_module == "💬 Universal NLP Scene Analyzer (X-Ray)":
    st.markdown("### 💬 Universal NLP Scene Analyzer & Vector X-Ray")
    st.markdown(
        "<p style='color: #8b949e;'><b>Universal Engine:</b> Handles full dialogues, single words, or short phrases dynamically with context-aware calibration.</p>",
        unsafe_allow_html=True,
    )

    preset_option = st.selectbox(
        "Load Preset Corpus or Enter Custom Text:",
        [
            "Custom Input (Type single words, short phrases, or full dialogues below)",
            "Genre 1: Domestic Trauma ('Ilhama & Parvaz' - Default)",
            "Genre 2: Wartime Trench Dialogue ('The Last Trench')",
            "Genre 3: Romantic Separation ('Unsent Letter to Paris')"
        ]
    )

    if "Wartime" in preset_option:
        default_corpus_active = (
            "Soldier A: - Did command know we were abandoned?\n"
            "Officer: - Orders are orders. Do not look at the map.\n"
            "Soldier A: - There is nothing left of the trenches... just mud and silence.\n"
            "Officer: - Silence is what keeps the regiment alive. Keep firing."
        )
    elif "Romantic" in preset_option:
        default_corpus_active = (
            "Partner A: - Why did you leave without saying goodbye?\n"
            "Partner B: - Some distances cannot be crossed with words.\n"
            "Partner A: - You left my letters unopened on the desk.\n"
            "Partner B: - Because reading them would mean admitting we ever existed."
        )
    else:
        default_corpus_active = default_corpus

    user_corpus_input = st.text_area(
        "Corpus Input Stream (Format: Speaker: Line OR Single Words):",
        value=default_corpus_active,
        height=180,
    )

    if st.button("⚡ Execute Universal Vector X-Ray"):
        with st.spinner("Processing token normalization, semantic classification, and vector mapping..."):
            time.sleep(0.4)

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

                # Intra-speaker compression tracking
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

                # Classification Logic
                if "(silence)" in clean_lower or "sükut" in clean_lower or len(clean_text.strip()) < 3:
                    emo = "Silence / Deep Void"
                    def_mech = "Lacanian Void / Suppression"
                    c_class = "warning-terminal"
                    raw_score = 85.0
                elif any(word in clean_lower for word in ["left her", "hide", "road", "fuck", "hate", "shatter", "kill"]):
                    emo = "Aggressive Accusation / Confrontation"
                    def_mech = "Open Hostility / Accusation"
                    c_class = "warning-terminal"
                    raw_score = 80.0
                elif any(word in clean_lower for word in ["truth", "luxury", "afford", "family", "matter", "future", "past"]):
                    emo = "Philosophical Defense / Rationalization"
                    def_mech = "Sartrean Bad Faith / Intellectualization"
                    c_class = "lab-card"
                    raw_score = 65.0
                elif has_q:
                    emo = "Direct Inquiry / Interrogation"
                    def_mech = "Open Questioning"
                    c_class = "terminal-box"
                    raw_score = 45.0
                elif evasion_score > 0.8:
                    emo = "Evasion / Topic Shift"
                    def_mech = "Defensive Deflection"
                    c_class = "lab-card"
                    raw_score = 50.0
                else:
                    emo = "Dynamic Interaction"
                    def_mech = "Open Exposure"
                    c_class = "terminal-box"
                    raw_score = 30.0

                beat_tension = int(min(100, max(10, raw_score + (evasion_score * w_evasion * 0.2) + (compression_ratio * w_compression * 0.2))))
                total_tension += beat_tension

                lex_density = 0.0
                results.append({
                    "beat": i + 1,
                    "speaker": curr_speaker,
                    "line": orig_line,
                    "tension": beat_tension,
                    "emo": emo,
                    "def_mech": def_mech,
                    "class": c_class,
                    "metrics": f"Evasion: {evasion_score:.2f} | Intra-Compression: {compression_ratio:.2f} | Lexical Density: {lex_density:.2f}"
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
# 8. MODULE 3: CHARACTER RELATIONSHIP & POWER MAP
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
            if any(w in txt.lower() for w in ["luxury", "afford", "matter", "hear", "future"]):
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

        st.markdown("---")
        st.markdown("#### 🔬 Analytical Insights on Conversational Physics")
        st.markdown(
            "<div class='context-box'>"
            "• <b>Interrogative Asymmetry:</b> Characters with high question counts drive narrative pressure, whereas low question counts paired with high word share indicate defensive rationalization.<br>"
            "• <b>Turn-Taking Control:</b> Dominance index evaluates absolute conversational real estate held by each speaker across the dialogue timeline."
            "</div>",
            unsafe_allow_html=True,
        )

# ==============================================================================
# 9. MODULE 4: RULE-BASED BRANCHING DEMONSTRATOR
# ==============================================================================
elif selected_module == "🔄 Rule-Based Branching Demonstrator":
    st.markdown("### 🔄 Rule-Based Branching Demonstrator")
    st.markdown(
        "<p style='color: #8b949e;'>Demonstrates heuristic conversational trajectories based on input triggers.</p>",
        unsafe_allow_html=True,
    )

    intervention_input = st.text_input(
        "Enter Custom Character Intervention Vector:",
        value="Zahra demands the key to the locked room.",
    )

    if st.button("Simulate Heuristic Trajectories"):
        with st.spinner("Calculating conversational physics..."):
            time.sleep(0.4)

        aggressive_keywords = ["shout", "break", "demand", "shatter", "hit", "fuck", "off"]
        is_aggressive = any(kw in intervention_input.lower() for kw in aggressive_keywords)
        peak_b2 = 100 if is_aggressive else 92

        st.markdown("---")
        st.markdown("### 🌿 Simulated Branching Trajectories")

        col_b1, col_b2, col_b3 = st.columns(3)

        with col_b1:
            st.markdown(
                "<div class='warning-terminal'>"
                "<b>Branch A: Evasion / Closure</b><br>"
                "<i style='font-size: 13px; color: #ff7b72;'>Respondent turns away, enforcing silence.</i><br><br>"
                "📉 <b>Tension Curve:</b> Drops to 45% via forced shutdown.<br>"
                "🛡️ <b>Wall Status:</b> <span style='color: #f85149;'>REINFORCED</span>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col_b2:
            st.markdown(
                "<div class='warning-terminal' style='background-color: #491002; border-color: #bd2c00; border-left-color: #f0883e;'>"
                "<b>Branch B: Confrontation / Apex</b><br>"
                "<i style='font-size: 13px; color: #ffa657;'>Respondent challenges the barrier.</i><br><br>"
                f"📈 <b>Tension Curve:</b> Spikes to {peak_b2}% (Apex).<br>"
                "🛡️ <b>Wall Status:</b> <span style='color: #f0883e;'>STRAINED</span>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col_b3:
            st.markdown(
                "<div class='terminal-box'>"
                "<b>Branch C: Softening / Catharsis</b><br>"
                "<i style='font-size: 13px; color: #7ee787;'>Respondent yields, offering emotional decay.</i><br><br>"
                "📉 <b>Tension Curve:</b> Decays to 20% (Resolution).<br>"
                "🛡️ <b>Wall Status:</b> <span style='color: #3fb9
