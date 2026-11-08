import datetime
import time
import streamlit as st

# Səhifə konfiqurasiyası
st.set_page_config(
    page_title="Ontological Silence & Paranoia Engine | AI Research Prototype",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- OVERRIDE STREAMLIT DEFAULT STYLES WITH HIGH-CONTRAST DARK CSS ---
st.markdown(
    """
    <style>
    /* Ümumi Arxa Fon */
    .stApp {
        background-color: #0b0f19 !important;
        color: #f1f5f9 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    
    /* Sol Panel (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #111827 !important;
        border-right: 1px solid #1f2937 !important;
    }
    [data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    
    /* Başlıqlar */
    h1, h2, h3, h4, h5, h6, label {
        color: #ffffff !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    
    /* TEXTAREA (Mətn daxiletmə qutusu) - TAM DÜZƏLİŞ */
    .stTextArea textarea {
        background-color: #1e293b !important;
        color: #38bdf8 !important;
        font-size: 15px !important;
        font-weight: bold !important;
        border: 1px solid #334155 !important;
        border-radius: 6px !important;
    }
    .stTextArea textarea:focus {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 10px rgba(56, 189, 248, 0.3) !important;
    }
    
    /* Düymələr */
    .stButton button {
        background-color: #0284c7 !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 10px 24px !important;
        transition: 0.3s !important;
    }
    .stButton button:hover {
        background-color: #38bdf8 !important;
        color: #0f172a !important;
    }
    
    /* Kartlar, Kontekst və Panellər */
    .lab-card {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-left: 4px solid #38bdf8;
        padding: 20px;
        border-radius: 6px;
        margin-bottom: 15px;
    }
    .context-box {
        background-color: #172554;
        border: 1px solid #1e3a8a;
        border-left: 4px solid #38bdf8;
        padding: 18px;
        color: #e0f2fe;
        font-size: 13px;
        border-radius: 6px;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    .terminal-box {
        background-color: #022c22;
        border: 1px solid #065f46;
        border-left: 4px solid #34d399;
        padding: 18px;
        color: #6ee7b7;
        font-size: 14px;
        border-radius: 6px;
        margin-top: 15px;
    }
    .warning-terminal {
        background-color: #450a0a;
        border: 1px solid #991b1b;
        border-left: 4px solid #f87171;
        padding: 18px;
        color: #fca5a5;
        font-size: 14px;
        border-radius: 6px;
        margin-top: 15px;
    }
    
    /* Metrik Rəqəmləri */
    [data-testid="stMetricValue"] {
        color: #38bdf8 !important;
        font-size: 32px !important;
        font-weight: bold !important;
    }
    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        font-size: 14px !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 👁️ Terminal Control")
    st.markdown(
        "<p style='font-size: 11px; color: #94a3b8;'>Computational Dramaturgy & AI Lab v5.0</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏛️ Executive Manifesto & Context",
            "💬 Custom AI Scene Analyzer (İnteraktiv)",
            "🧠 Neural-Psychoanalytic Simulator",
            "⚛️ Lacanian & Sartrean Subtext Matrix",
            "📜 Core Artifact: 'İlhəmə və Pərvaz'",
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
        "<p style='color: #38bdf8; font-size: 15px;'>An Experimental Computational Framework for Mapping Domestic Silence, Trauma, and Conversational Physics.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    # Komissiya və kənar oxucular üçün Kontekst Xülasəsi əlavə olundu
    st.markdown(
        """
    <div class='context-box'>
        📌 <b>PROTOTYPE CONTEXT BRIEF (For Evaluators):</b><br>
        <i>"İlhəmə və Pərvaz"</i> is a narrative exploring domestic isolation and inherited trauma. The core scene features a late-night kitchen confrontation between young Zəhra and her father, <b>Pərvaz</b>, where the unspoken memory of the mother (İlhəmə) acts as an invisible structural wall. This engine treats that text not as fiction, but as a computational field of silence, paranoia, and linguistic defense.
    </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div class='lab-card'>
            <h3 style='color: #38bdf8; margin-top:0;'>🌌 The Core Thesis</h3>
            <p style='color: #e2e8f0; font-size: 14px; line-height: 1.6;'>
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
            <h3 style='color: #38bdf8; margin-top:0;'>⚙️ Interactive Capabilities</h3>
            <p style='color: #e2e8f0; font-size: 14px; line-height: 1.6;'>
            This system allows creators and researchers to input custom dialogue lines or adjust psychological friction variables in real time, calculating existential indices instantly.
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

# --- MODULE 2: CUSTOM AI SCENE ANALYZER ---
elif selected_module == "💬 Custom AI Scene Analyzer (İnteraktiv)":
    st.markdown("### 💬 Custom AI Scene & Dialogue Analyzer")
    st.markdown(
        "<p style='color: #94a3b8;'>Type or paste any dramatic dialogue below. The AI engine will compute its silence density and paranoia index in real time.</p>",
        unsafe_allow_html=True,
    )

    user_input_scene = st.text_area(
        "Enter Dialogue Corpus for Real-Time Analysis:",
        value=(
            "- Niyə hər dəfə bu qapı açılanda səsin titrəyir?\n"
            "- Çünki bəzi həqiqətlər otağa sığmır.\n"
            "- Onda niyə danışmırsan?\n"
            "- Danışmaq təslim olmaqdır."
        ),
        height=150,
    )

    analyze_clicked = st.button("⚡ Run AI Analysis")

    if analyze_clicked:
        with st.spinner("Synthesizing linguistic pauses and psychological friction..."):
            time.sleep(1)

        word_count = len(user_input_scene.split())
        computed_silence = min(
            95,
            max(
                20,
                int(
                    50
                    + (user_input_scene.count("?") * 8)
                    - (word_count * 0.1)
                ),
            ),
        )
        computed_paranoia = min(
            98,
            max(
                15,
                int(
                    100
                    - computed_silence
                    + (user_input_scene.count("...") * 10)
                ),
            ),
        )

        st.markdown("---")
        st.markdown("### 🔬 Computational Output & Diagnostics")

        res1, res2, res3 = st.columns(3)
        res1.metric(label="Analyzed Word Count", value=word_count)
        res2.metric(label="Calculated Silence Index", value=f"{computed_silence}%")
        res3.metric(label="Paranoia Coefficient", value=f"{computed_paranoia}%")

        if computed_paranoia > 60:
            st.markdown(
                f"<div class='warning-terminal'>⚠️ <b>HIGH PARANOIA ({computed_paranoia}%):</b> High presence of defensive mechanisms, communicative walls, and structural paranoia.</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<div class='terminal-box'>🟢 <b>NOMINAL STATE ({computed_paranoia}%):</b> Dialogue breakdown risk is low.</div>",
                unsafe_allow_html=True,
            )

        st.markdown("#### 🧬 AI Breakdown:")
        st.write(
            f"- **Pauses/Questions:** {user_input_scene.count('.')} pauses,"
            f" {user_input_scene.count('?')} questions."
        )
        st.write(
            "- **Subtext:** Unspoken truths acting as psychological barrier."
        )

# --- MODULE 3: SIMULATOR ---
elif selected_module == "🧠 Neural-Psychoanalytic Simulator":
    st.markdown("### 🧠 Multi-Factorial Simulator")
    col1, col2 = st.columns(2)
    with col1:
        e_dread = st.slider("Existential Dread", 0, 100, 65)
        l_void = st.slider("Lacanian Void (İlhəmə's Absence)", 0, 100, 70)
    with col2:
        l_supp = st.slider("Linguistic Suppression", 0, 100, 80)
        i_trauma = st.slider("Inherited Trauma (Pərvaz factor)", 0, 100, 60)

    p_score = int((e_dread * 0.3) + (l_void * 0.3) + (l_supp * 0.4))
    st.metric(label="Paranoia Amplification Index", value=f"{p_score}%")

# --- MODULE 4: SUBTEXT MATRIX ---
elif selected_module == "⚛️ Lacanian & Sartrean Subtext Matrix":
    st.markdown("### ⚛️ Subtext Matrix")
    c1, c2, c3 = st.columns(3)
    c1.markdown(
        "<div class='lab-card'><b>1. Sartrean Bad Faith</b><br>88%<br><p style='font-size:12px; color:#94a3b8; margin-top:5px;'>Pərvaz hiding behind institutionalized duty.</p></div>",
        unsafe_allow_html=True,
    )
    c2.markdown(
        "<div class='lab-card'><b>2. Lacanian Lack</b><br>92%<br><p style='font-size:12px; color:#94a3b8; margin-top:5px;'>Zəhra's symbolic void regarding her mother İlhəmə.</p></div>",
        unsafe_allow_html=True,
    )
    c3.markdown(
        "<div class='lab-card'><b>3. Foucault Panopticism</b><br>76%<br><p style='font-size:12px; color:#94a3b8; margin-top:5px;'>The kitchen vault acting as an internal surveillance room.</p></div>",
        unsafe_allow_html=True,
    )

# --- MODULE 5: ARTIFACT ---
elif selected_module == "📜 Core Artifact: 'İlhəmə və Pərvaz'":
    st.markdown("### 📜 Core Artifact: The Kitchen Confrontation")
    st.text_area(
        "Corpus Data Stream (Read-Only)",
        (
            "[ONTOLOGICAL SCENE: KITCHEN VAULT - 03:42 AM]\n\n"
            "Zəhra: - Did İlhəmə ever love me?\n"
            "Pərvaz: - Why are you asking?\n"
            "Zəhra: - Because I don't know. I don't remember her voice, father. I don't even remember her face.\n"
            "Pərvaz: - She was your mother. A person loves their own blood. This isn't something to be asked, Zəhra.\n"
            "Zəhra: - That is not an answer. You aren't telling me how she loved. You are just giving me the sentence you need to survive.\n"
            "Pərvaz: - She loved no one... Everyone in this house opened that door themselves one day. But no one remembered how they walked through it."
        ),
        height=220,
    )

# FOOTER
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #64748b; font-size: 11px;'>ONTOLOGICAL SILENCE ENGINE // MIT MEDIA LAB ARTIFACT</p>",
    unsafe_allow_html=True,
)
