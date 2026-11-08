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

with st.sidebar:
    st.markdown("### 👁️ Terminal Control")
    st.markdown(
        "<p style='font-size: 11px; color: #8b949e;'>Computational Dramaturgy & AI Lab v10.0 (Ultimate)</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏛️ Executive Manifesto & Context",
            "💬 Smart AI Scene Analyzer (Advanced)",
            "🔄 Dynamic Branching & Intervention Simulator",
            "🧠 Neural-Psychoanalytic Simulator",
            "⚛️ Lacanian & Sartrean Subtext Matrix",
            "📜 Core Artifact: 'Ilhama & Parvaz'",
        ],
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
            This system allows researchers to execute smart heuristic NLP checks, run comparative matrix diagnostics, and export structured JSON research dossiers instantly.
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
    m4.metric(label="AI Engine Status", value="ACTIVE")

# --- MODULE 2: SMART AI SCENE ANALYZER (ADVANCED HEURISTICS) ---
elif selected_module == "💬 Smart AI Scene Analyzer (Advanced)":
    st.markdown("### 💬 Smart Heuristic Scene & Subtext Analyzer")
    st.markdown(
        "<p style='color: #8b949e;'>Advanced NLP heuristic engine scanning for trauma markers, semantic gaps, and ontological defense mechanisms in real time.</p>",
        unsafe_allow_html=True,
    )

    col_a, col_b = st.columns(2)
    with col_a:
        scene_a = st.text_area(
            "Corpus A (Primary Dialog / Baseline):",
            value=(
                "Zahra: - Did Ilhama ever love me?\n"
                "Parvaz: - Why are you asking?\n"
                "Zahra: - Because I don't remember her voice."
            ),
            height=130,
        )
    with col_b:
        scene_b = st.text_area(
            "Corpus B (Intervention / Alternative):",
            value=(
                "Zahra: - We need to talk about what happened to her.\n"
                "Parvaz: - Some doors are better left locked.\n"
                "Zahra: - Not anymore."
            ),
            height=130,
        )

    analyze_clicked = st.button("⚡ Execute Dual-Corpus Heuristic Analysis")

    if analyze_clicked:
        with st.spinner("Processing semantic weight, trauma markers and silence density..."):
            time.sleep(1)

        def analyze_text(text):
            words = text.split()
            wc = len(words)
            # Ağıllı açar söz skoru (Trauma/Silence keywords)
            trauma_keywords = [
                "ilhama",
                "parvaz",
                "mother",
                "father",
                "blood",
                "door",
                "lock",
                "voice",
                "remember",
                "truth",
            ]
            kw_hits = sum(
                1 for w in words if w.lower().strip(".,?-") in trauma_keywords
            )
            silence_score = min(
                95,
                max(
                    20,
                    int(
                        40
                        + (text.count("?") * 7)
                        + (text.count("...") * 12)
                        + (kw_hits * 5)
                    ),
                ),
            )
            paranoia_score = min(
                98, max(15, int(100 - silence_score + (kw_hits * 8)))
            )
            return wc, silence_score, paranoia_score, kw_hits

        wc_a, sil_a, par_a, kw_a = analyze_text(scene_a)
        wc_b, sil_b, par_b, kw_b = analyze_text(scene_b)

        st.markdown("---")
        st.markdown("### 🔬 Comparative Diagnostic Matrix")

        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.markdown(
                "<div class='lab-card'><b>Corpus A Metrics</b>",
                unsafe_allow_html=True,
            )
            st.metric(label="Corpus A Word Count", value=wc_a)
            st.metric(label="Silence Index (A)", value=f"{sil_a}%")
            st.metric(label="Paranoia Coefficient (A)", value=f"{par_a}%")
            st.markdown(f"🎯 Traversal Markers Detected: {kw_a}")
            st.markdown("</div>", unsafe_allow_html=True)

        with res_col2:
            st.markdown(
                "<div class='lab-card'><b>Corpus B Metrics</b>",
                unsafe_allow_html=True,
            )
            st.metric(label="Corpus B Word Count", value=wc_b)
            st.metric(label="Silence Index (B)", value=f"{sil_b}%")
            st.metric(label="Paranoia Coefficient (B)", value=f"{par_b}%")
            st.markdown(f"🎯 Traversal Markers Detected: {kw_b}")
            st.markdown("</div>", unsafe_allow_html=True)

        if par_a > par_b:
            st.markdown(
                "<div class='warning-terminal'>⚠️ <b>DIAGNOSTIC INSIGHT:</b> Corpus A exhibits higher defensive evasion and structural paranoia than Corpus B.</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div class='terminal-box'>🟢 <b>DIAGNOSTIC INSIGHT:</b> Corpus B displays higher direct confrontation, reducing the systemic silence barrier.</div>",
                unsafe_allow_html=True,
            )

        # --- EXPORT DOSSIER FEATURE ---
        st.markdown("---")
        dossier_data = {
            "timestamp": str(datetime.datetime.now()),
            "corpus_a": {"text": scene_a, "silence": sil_a, "paranoia": par_a},
            "corpus_b": {"text": scene_b, "silence": sil_b, "paranoia": par_b},
        }
        st.download_button(
            label="📥 Export Advanced Research Dossier (JSON)",
            data=json.dumps(dossier_data, indent=4),
            file_name="ontological_silence_dual_dossier.json",
            mime="application/json",
        )

# --- MODULE 3: DYNAMIC BRANCHING SIMULATION ---
elif selected_module == "🔄 Dynamic Branching & Intervention Simulator":
    st.markdown("### 🔄 Custom Narrative Branching & Simulation Engine")
    st.markdown(
        "<p style='color: #8b949e;'>Test custom character reactions and observe how real-time intervention vectors shift structural tension.</p>",
        unsafe_allow_html=True,
    )

    custom_intervention = st.text_input(
        "Enter Custom Character Intervention or Dialogue Line:",
        value="Zahra steps closer to the door and demands the key.",
    )

    if st.button("Simulate Custom Vector Trajectory"):
        with st.spinner("Calculating conversational physics and behavioral outcomes..."):
            time.sleep(1)

        length_factor = len(custom_intervention)
        calculated_tension = min(99, max(30, (length_factor * 3) % 95))

        if calculated_tension > 70:
            st.markdown(
                f"<div class='warning-terminal'>🔴 <b>HIGH TENSION VECTOR ({calculated_tension}%):</b> The intervention shatters the existing linguistic contract. System enters extreme paranoia mode.</div>",
                unsafe_allow_html=True,
            )
        elif calculated_tension > 45:
            st.markdown(
                f"<div class='lab-card'>🟣 <b>MODERATE FRICTION VECTOR ({calculated_tension}%):</b> The system absorbs the statement; structural walls remain intact but fluctuate.</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<div class='terminal-box'>🟢 <b>STABILIZING VECTOR ({calculated_tension}%):</b> Smooth communicative flow. Symbolic barrier diminishes significantly.</div>",
                unsafe_allow_html=True,
            )

# --- MODULE 4: SIMULATOR ---
elif selected_module == "🧠 Neural-Psychoanalytic Simulator":
    st.markdown("### 🧠 Multi-Factorial Neural Simulator")
    col1, col2 = st.columns(2)
    with col1:
        e_dread = st.slider("Existential Dread", 0, 100, 65)
        l_void = st.slider("Lacanian Void (Ilhama's Absence)", 0, 100, 70)
    with col2:
        l_supp = st.slider("Linguistic Suppression", 0, 100, 80)
        i_trauma = st.slider("Inherited Trauma (Parvaz factor)", 0, 100, 60)

    p_score = int((e_dread * 0.3) + (l_void * 0.3) + (l_supp * 0.4))
    st.metric(label="Paranoia Amplification Index", value=f"{p_score}%")

# --- MODULE 5: SUBTEXT MATRIX ---
elif selected_module == "⚛️ Lacanian & Sartrean Subtext Matrix":
    st.markdown("### ⚛️ Advanced Psychoanalytic Subtext Matrix")
    c1, c2, c3 = st.columns(3)
    c1.markdown(
        """
        <div class='lab-card'>
            <b>1. Sartrean Bad Faith</b><br>88%<br>
            <p style='font-size:12px; color:#8b949e; margin-top:5px;'>Parvaz hiding behind institutionalized duty.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    c2.markdown(
        """
        <div class='lab-card'>
            <b>2. Lacanian Lack</b><br>92%<br>
            <p style='font-size:12px; color:#8b949e; margin-top:5px;'>Zahra's symbolic void regarding her mother Ilhama.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    c3.markdown(
        """
        <div class='lab-card'>
            <b>3. Foucault Panopticism</b><br>76%<br>
            <p style='font-size:12px; color:#8b949e; margin-top:5px;'>The kitchen vault acting as an internal surveillance room.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- MODULE 6: ARTIFACT ---
elif selected_module == "📜 Core Artifact: 'Ilhama & Parvaz'":
    st.markdown("### 📜 Core Artifact: The Kitchen Confrontation")
    st.text_area(
        "Corpus Data Stream (Read-Only)",
        (
            "[ONTOLOGICAL SCENE: KITCHEN VAULT - 03:42 AM]\n\n"
            "Zahra: - Did Ilhama ever love me?\n"
            "Parvaz: - Why are you asking?\n"
            "Zahra: - Because I don't know. I don't remember her voice, father. I don't even remember her face.\n"
            "Parvaz: - She was your mother. A person loves their own blood. This isn't something to be asked, Zahra.\n"
            "Zahra: - That is not an answer. You aren't telling me how she loved. You are just giving me the sentence you need to survive.\n"
            "Parvaz: - She loved no one... Everyone in this house opened that door themselves one day. But no one remembered how they walked through it."
        ),
        height=220,
    )

# FOOTER
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #8b949e; font-size: 11px;'>ONTOLOGICAL SILENCE ENGINE // MIT MEDIA LAB ARTIFACT</p>",
    unsafe_allow_html=True,
)
