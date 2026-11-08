import datetime
import json
import time
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Ontological Silence & Paranoia Engine | AI Research Prototype",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CYBER-NOIR & DARK PLOTLY-READY CSS ---
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

# --- SIDEBAR NAVIGATION MATRIX ---
with st.sidebar:
    st.markdown("### 👁️ Terminal Control")
    st.markdown(
        "<p style='font-size: 11px; color: #8b949e;'>Computational Dramaturgy & AI Lab v12.5 (Universal Engine)</p>",
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

# --- MODULE 1: MANIFESTO & FORMAL SILENCE INDEX ---
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
            SI = w₁·(Unanswered Questions) + w₂·(Evasion / Topic Shifts) + w₃·(Ellipsis Count) + w₄·(Generalizations) + w₅·(Word Count Drop) + w₆·(Suppressed Proper Nouns)<br><br>
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
                <b>1. Unanswered Questions (w₁ = 15%)</b><br>
                <span style='color: #8b949e; font-size: 13px;'>Measured when inquiries are met with counter-interrogation or deflection.</span>
            </div>
            <div class='lab-card'>
                <b>2. Evasion & Topic Shifts (w₂ = 20%)</b><br>
                <span style='color: #8b949e; font-size: 13px;'>Quantifies semantic distance between prompt and respondent reply.</span>
            </div>
            <div class='lab-card'>
                <b>3. Ellipsis & Suspended Syntax (w₃ = 10%)</b><br>
                <span style='color: #8b949e; font-size:
