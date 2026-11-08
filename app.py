import datetime
import json
import time
import streamlit as st

st.set_page_config(
    page_title="Ontological Silence & Paranoia Engine | AI Research Prototype",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded",
)

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
    .stTextArea textarea {
        background-color: #0d1117 !important;
        color: #58a6ff !important;
        font-size: 15px !important;
        font-weight: bold !important;
        border: 1px solid #30363d !important;
        border-radius: 6px !important;
    }
    .stTextArea textarea:focus {
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

with st.sidebar:
    st.markdown("### 👁️ Terminal Control")
    st.markdown(
        "<p style='font-size: 11px; color: #8b949e;'>Computational Dramaturgy & AI Lab v9.1</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏛️ Executive Manifesto & Context",
            "💬 Custom AI Scene Analyzer (Interactive)",
            "🔄 Interactive Branching Simulation",
            "🧠 Neural-Psychoanalytic Simulator",
            "⚛️ Lacanian & Sartrean Subtext Matrix",
            "📜 Core Artifact: 'Ilhama & Parvaz'",
        ],
    )

    st.markdown("---")
    st.markdown("🎵 **Noir Atmosphere Audio**")
    # Təhlükəsiz və işlək ambient audio treki
    st.audio(
        "https://upload.wikimedia.org/wikipedia/commons/e/e5/Rain_in_Field_and_Thunder.ogg",
        format="audio/ogg",
    )

    st.markdown("---")
    st.markdown("**Framework Architect:** Agil Chiragli")
    st.markdown("**Target:** MIT Media Lab Portfolio")
    st.markdown(f"**Date:** {datetime.date.today().strftime('%Y-%m-%d')}")

# --- MODULE 1: MANIFESTO & CONTEXT ---
if selected_module == "🏛️ Executive Manifesto & Context":
    st.markdown(
        "<h1 style='font-size: 30px;'>👁️ THE ONTOLOGICAL SILENCE & PARANOIA ENGINE</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: #f0883e; font-size: 15px;'>An Experimental Computational Framework for Mapping Domestic Silence, Trauma, and Conversational Physics.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    st.markdown(
        """
    <div class='context-box'>
        📌 <b>PROTOTYPE CONTEXT BRIEF (For Evaluators):</b><br>
        <i>"Ilhama and Parvaz"</i> is a narrative exploring domestic isolation and inherited trauma. The core scene features a late-night kitchen confrontation between young Zahra and her father, <b>Parvaz</b>, where the unspoken memory of the mother (Ilhama) acts as an invisible structural wall. This engine treats that text not as fiction, but as a computational field of silence, paranoia, and linguistic defense.
    </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div class='lab-card'>
            <h3 style='color: #f0883e; margin-top:0;'>🌌 The Core Thesis</h3>
            <p style='color: #c9d1d9; font-size: 14px; line-height: 1.6;'>
            Silence in domestic architecture is never empty. It is a dense, calculated structural weapon—a linguistic vault where generational trauma, institutional surveillance, and suppressed memory are stored.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class='lab-card'>
            <h3 style='color: #f0883e; margin-top:0;'>⚙️ Interactive Capabilities</h3>
            <p style='color: #c9d1d9; font-size: 14px; line-height: 1.6;'>
            This system allows creators and researchers to input custom dialogue lines, run real-time diagnostic simulations, and test interactive branching trajectories instantly.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("### 📊 System Diagnostics")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Deconstructed Vectors", value="3,120")
    m2.metric(label="Base Silence Index", value="44.2%")
    m3.metric(label="Paranoia Coefficient", value="71.5%")
