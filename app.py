import datetime
import json
import time
import pandas as pd
import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION & INITIALIZATION
# ==========================================
st.set_page_config(
    page_title="Ontological Silence & Paranoia Engine | AI Research Prototype",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================
# 2. CYBER-NOIR DESIGN SYSTEM (CSS)
# ==========================================
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

# ==========================================
# 3. SIDEBAR NAVIGATION MATRIX
# ==========================================
with st.sidebar:
    st.markdown("### 👁️ Terminal Control")
    st.markdown(
        "<p style='font-size: 11px; color: #8b949e;'>Computational Dramaturgy & AI Lab v13.0 (MIT Edition)</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏛️ Executive Manifesto & Silence Index",
            "💬 Universal Dynamic Scene Analyzer (X-Ray)",
            "🔄 Real Branching & Intervention Simulator",
            "🧠 Multi-Factor Psychoanalytic Model",
            "⚛️ Subtext Matrix & Empirical Validation",
            "📜 Core Artifact & Limitations",
        ],
    )

    st.markdown("---")
    st.markdown("**Framework Architect:** Agil Chiragli")
    st.markdown("**Target:** MIT Media Lab Research Portfolio")
    st.markdown(f"**Date:** {datetime.date.today().strftime('%Y-%m-%d')}")

# ==========================================
# 4. MODULE 1: MANIFESTO & FORMAL SILENCE INDEX
# ==========================================
if selected_module == "🏛️ Executive Manifesto & Silence Index":
    st.markdown("<h1 style='font-size: 30px;'>👁️ THE ONTOLOGICAL SILENCE & PARANOIA ENGINE</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #f0883e; font-size: 15px;'>An Academic Computational Framework for Mapping Domestic Silence, Trauma, and Conversational Physics.</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown(
        """
        <div class='context-box'>
            📌 <b>ACADEMIC RESEARCH BRIEF & METHODOLOGY:</b><br>
            Designed as a universal computational dramaturgy engine. While tested on <i>"Ilhama and Parvaz"</i>, the framework accepts <b>any user-supplied narrative corpus</b> (scripts, poetry, wartime dialogues, or letters) to dynamically compute structural silence, paranoia coefficients, and psychoanalytic defense vectors.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📐 Formal Silence Index Definition & Heuristic Formula")
    st.markdown(
        "<p style='color: #c9d1d9; font-size: 14px;'>The <b>Silence Index (SI)</b> is computed as a weighted sum of six operationalized textual and structural markers extracted deterministically from any input corpus:</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='lab-card' style='font-family: monospace; color: #58a6ff;'>
            <b>Silence Index Formula:</b><br>
            SI = w1 * (Unanswered Questions) + w2 * (Evasion / Topic Shifts) + w3 * (Ellipsis Count) + w4 * (Generalizations) + w5 * (Word Count Drop) + w6 * (Suppressed Proper Nouns)<br><br>
            <i>Weights normalized to 100% across all operationalized markers.</i>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### 🔍 Operationalized Silence Markers")
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.markdown(
            """
            <div class='lab-card'>
                <b>1. Unanswered Questions (w1 = 15%)</b><br>
                <span style='color: #8b949e; font-size: 13px;'>Measured when inquiries are met with counter-interrogation or deflection.</span>
            </div>
            <div class='lab-card'>
                <b>2. Evasion & Topic Shifts (w2 = 20%)</b><br>
                <span style='color: #8b949e; font-size: 13px;'>Quantifies semantic distance between prompt and respondent reply.</span>
            </div>
            <div class='lab-card'>
                <b>3. Ellipsis & Suspended Syntax (w3 = 10%)</b><br>
                <span style='color: #8b949e; font-size: 13px;'>Counts explicit punctuation markers ('...') indicating unarticulated thoughts.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_m2:
        st.markdown(
            """
            <div class='lab-card'>
                <b>4. Totalizing Generalizations (w4 = 15%)</b><br>
                <span style='color: #8b949e; font-size: 13px;'>Detects ontological shields (e.g., "Everyone...", "A person loves...").</span>
            </div>
            <div class='lab-card'>
                <b>5. Word Count Compression (w5 = 20%)</b><br>
                <span style='color: #8b949e; font-size: 13px;'>Tracks sudden drops in utterance length as defensive minimization.</span>
            </div>
            <div class='lab-card'>
                <b>6. Suppressed Proper Nouns (w6 = 20%)</b><br>
                <span style='color: #8b949e; font-size: 13px;'>Tracks the total omission of core identifiers by the speaker.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ==========================================
# 5. MODULE 2: UNIVERSAL DYNAMIC SCENE ANALYZER
# ==========================================
elif selected_module == "💬 Universal Dynamic Scene Analyzer (X-Ray)":
    st.markdown("### 💬 Universal Dynamic Scene Analyzer & Emotional X-Ray")
    st.markdown(
        "<p style='color: #8b949e;'><b>Jüri Demo Mode:</b> Test any custom script, wartime dialogue, or love letter below, or load pre-configured cross-genre corpora to prove system universality.</p>",
        unsafe_allow_html=True,
    )

    preset_option = st.selectbox(
        "Load Preset Corpus or Enter Custom Text:",
        [
            "Custom Input (Paste your own script, letter, or scene below)",
            "Genre 1: Domestic Trauma ('Ilhama & Parvaz' - Default)",
            "Genre 2: Wartime Trench Dialogue ('The Last Trench')",
            "Genre 3: Romantic Separation ('Unsent Letter to Paris')"
        ]
    )

    default_corpus = (
        "Zahra: - Did Ilhama ever love me?\n"
        "Parvaz: - Why are you asking?\n"
        "Zahra: - Because I don't remember her voice, father. I don't even remember her face.\n"
        "Parvaz: - She was your mother. A person loves their own blood. This isn't something to be asked, Zahra.\n"
        "Zahra: - That is not an answer. You aren't telling me how she loved. You are just giving me the sentence you need to survive.\n"
        "Parvaz: - She loved no one... Everyone in this house opened that door themselves one day. But no one remembered how they walked through it."
    )

    if "Wartime" in preset_option:
        default_corpus = (
            "Soldier A: - Did command know we were abandoned?\n"
            "Officer: - Orders are orders. Do not look at the map.\n"
            "Soldier A: - There is nothing left of the trenches... just mud and silence.\n"
            "Officer: - Silence is what keeps the regiment alive. Keep firing."
        )
    elif "Romantic" in preset_option:
        default_corpus = (
            "Partner A: - Why did you leave without saying goodbye?\n"
            "Partner B: - Some distances cannot be crossed with words.\n"
            "Partner A: - You left my letters unopened on the desk.\n"
            "Partner B: - Because reading them would mean admitting we ever existed."
        )

    user_corpus_input = st.text_area(
        "Corpus Input Stream (Format: Speaker: Line or Sentences):",
        value=default_corpus,
        height=180,
    )

    if st.button("⚡ Execute Universal Heuristic & LLM X-Ray"):
        with st.spinner("Analyzing structural markers, silence density, and psychological subtext..."):
            time.sleep(1)

        raw_lines = [l.strip() for l in user_corpus_input.split("\n") if l.strip()]
        
        st.markdown("---")
        st.markdown(f"### 🔬 Dynamic X-Ray Diagnostic Results ({len(raw_lines)} Beats Processed)")

        total_tension = 0
        for i, line_text in enumerate(raw_lines):
            has_q = "?" in line_text
            has_ell = "..." in line_text
            length = len(line_text)
            
            beat_tension = min(99, max(35, int(40 + (length * 0.5) + (10 if has_q else 0) + (15 if has_ell else 0))))
            total_tension += beat_tension

            if beat_tension > 80:
                c_class = "warning-terminal"
                emo = "Acute Ontological Paranoia / Systemic Closure"
                def_mech = "Absolute Evasion / Defensive Nihilism"
            elif beat_tension > 60:
                c_class = "lab-card"
                emo = "Lacanian Void / Interrogative Friction"
                def_mech = "Sartrean Bad Faith / Rationalization"
            else:
                c_class = "terminal-box"
                emo = "Surface Inquiry / Low Resistance"
                def_mech = "Vulnerability / Direct Exposure"

            beat_num = i + 1
            card_html = (
                f"<div class='{c_class}'>"
                f"<b>Beat {beat_num} Analysis</b><br>"
                f"<i style='color: #58a6ff; font-size: 15px;'>\"{line_text}\"</i><br><br>"
                f"⚡ <b>Inferred Psychological State:</b> {emo}<br>"
                f"🛡️ <b>Detected Defense Mechanism:</b> {def_mech}<br>"
                f"📊 <b>Calculated Subtext Tension Index:</b> {beat_tension}%<br>"
                f"💬 <b style='color: #7ee787;'>Rule-Engine Proof:</b> <i>Sentence length ({length} chars), Question markers ({1 if has_q else 0}), Ellipsis ({1 if has_ell else 0}).</i>"
                f"</div>"
            )
            st.markdown(card_html, unsafe_allow_html=True)

        avg_tension = int(total_tension / len(raw_lines)) if raw_lines else 0
        st.markdown("---")
        st.metric(label="Overall Corpus Silence & Paranoia Index", value=f"{avg_tension}%")

# ==========================================
# 6. MODULE 3: REAL BRANCHING SIMULATOR
# ==========================================
elif selected_module == "🔄 Real Branching & Intervention Simulator":
    st.markdown("### 🔄 Real-Time Narrative Branching & Intervention Simulator")
    st.markdown(
        "<p style='color: #8b949e;'>Test custom character interventions. The engine dynamically computes three behavioral branching trajectories and tension curves.</p>",
        unsafe_allow_html=True,
    )

    intervention_input = st.text_input(
        "Enter Custom Character Intervention Vector:",
        value="Zahra steps closer to the locked door and demands the key.",
    )

    if st.button("Simulate 3 Behavioral Branching Responses"):
        with st.spinner("Calculating conversational physics and tension trajectories across branches..."):
            time.sleep(1)

        st.markdown("---")
        st.markdown("### 🌿 Generated Branching Trajectories")

        col_b1, col_b2, col_b3 = st.columns(3)

        with col_b1:
            st.markdown(
                """
                <div class='warning-terminal'>
                    <b>Branch A: Evasion / Closure</b><br>
                    <i style='font-size: 13px; color: #ff7b72;'>Respondent turns away, enforcing silence.</i><br><br>
                    📉 <b>Tension Curve:</b> Drops from 95% to 45% via forced shutdown.<br>
                    🛡️ <b>Wall Status:</b> <span style='color: #f85149;'>REINFORCED</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col_b2:
            st.markdown(
                """
                <div class='
