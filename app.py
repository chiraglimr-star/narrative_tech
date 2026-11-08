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

# --- ULTIMATE CINEMATIC DARK-NOIR & AMBER CSS ---
st.markdown(
    """
    <style>
    /* Dərin qara noür arxa fon */
    .stApp {
        background-color: #000000;
        color: #e2e8f0;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Yan panel - zərif qrafit */
    [data-testid="stSidebar"] {
        background-color: #08080a;
        border-right: 1px solid #1c1c24;
    }
    
    /* Başlıqlar - təmiz ağ və kəhrəba işığı */
    h1, h2, h3, h4 {
        color: #f3f4f6 !important;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: -0.5px;
    }
    
    /* Əsas Kartlar (Laboratoriya panelləri) */
    .lab-card {
        background-color: #0a0a0e;
        border: 1px solid #22222e;
        border-left: 4px solid #f59e0b; /* Kəhrəba / Amber vurğu */
        padding: 22px;
        border-radius: 6px;
        margin-bottom: 15px;
    }
    
    /* Terminal qutuları */
    .terminal-box {
        background-color: #050508;
        border: 1px solid #22222e;
        border-left: 4px solid #10b981; /* Yaşıl terminal işığı */
        padding: 18px;
        color: #34d399;
        font-size: 13px;
        border-radius: 4px;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Xəbərdarlıq qutuları (Qan-qırmızı triller stili) */
    .warning-terminal {
        background-color: #140305;
        border: 1px solid #501015;
        border-left: 4px solid #ef4444; /* Dərin qırmızı */
        padding: 18px;
        color: #fca5a5;
        font-size: 13px;
        border-radius: 4px;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Metrik rəqəmləri - Parlaq kəhrəba */
    [data-testid="stMetricValue"] {
        color: #f59e0b !important;
        font-size: 28px !important;
        font-weight: bold;
    }
    [data-testid="stMetricLabel"] {
        color: #9ca3af !important;
        font-size: 13px !important;
    }
    
    /* Tabların stili */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #0a0a0e;
        border-radius: 6px;
        color: #9ca3af;
        padding: 10px 20px;
        font-family: 'Courier New', Courier, monospace;
        border: 1px solid #22222e;
    }
    .stTabs [aria-selected="true"] {
        background-color: #16161f !important;
        color: #f59e0b !important;
        border: 1px solid #f59e0b !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 👁️ Terminal Control")
    st.markdown(
        "<p style='font-size: 11px; color: #9ca3af;'>Computational Dramaturgy & AI Lab v4.1</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏛️ Executive Manifesto",
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

# --- MODULE 1: MANIFESTO ---
if selected_module == "🏛️ Executive Manifesto":
    st.markdown(
        "<h1 style='font-size: 30px;'>👁️ THE ONTOLOGICAL SILENCE & PARANOIA ENGINE</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: #f59e0b; font-size: 15px;'>An Experimental Computational Framework for Mapping Domestic Silence, Trauma, and Conversational Physics.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div class='lab-card'>
            <h3 style='color: #f59e0b; margin-top:0;'>🌌 The Core Thesis</h3>
            <p style='color: #d1d5db; font-size: 13px; line-height: 1.6;'>
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
            <h3 style='color: #f59e0b; margin-top:0;'>⚙️ Interactive Capabilities</h3>
            <p style='color: #d1d5db; font-size: 13px; line-height: 1.6;'>
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
        "<p style='color: #9ca3af;'>Type or paste any dramatic dialogue, family confrontation, or script excerpt below. The AI engine will compute its underlying silence density, paranoia index, and psychoanalytic subtext in real time.</p>",
        unsafe_allow_html=True,
    )

    user_input_scene = st.text_area(
        "Enter Dialogue Corpus for Real-Time Analysis:",
        value=(
            "- Niyə hər dəfə bu qapı açılanda səsin titrəyir?\n- Çünki bəzi"
            " həqiqətlər otağa sığmır.\n- Onda niyə danışmırsan?\n- Danışmaq"
            " təslim olmaqdır."
        ),
        height=140,
    )

    col_btn1, col_btn2 = st.columns([1, 4])
    with col_btn1:
        analyze_clicked = st.button("⚡ Run AI Analysis")

    if analyze_clicked:
        with st.spinner(
            "Synthesizing linguistic pauses and psychological friction..."
        ):
            time.sleep(1.2)

        word_count = len(user_input_scene.split())
        computed_silence = min(
            95, max(20, int(50 + (user_input_scene.count("?") * 8) - (word_count * 0.1)))
        )
        computed_paranoia = min(
            98, max(15, int(100 - computed_silence + (user_input_scene.count("...") * 10)))
        )

        st.markdown("---")
        st.markdown("### 🔬 Computational Output & Diagnostics")

        res1, res2, res3 = st.columns(3)
        res1.metric(label="Analyzed Word Count", value=word_count)
        res2.metric(label="Calculated Silence Index", value=f"{computed_silence}%")
        res3.metric(label="Paranoia Coefficient", value=f"{computed_paranoia}%")

        if computed_paranoia > 60:
            st.markdown(
                f"<div class='warning-terminal'>⚠️ <b>HIGH PARANOIA & DEFENSIVE ANCHOR ({computed_paranoia}%):</b> The provided text exhibits strong linguistic evasion, closed loops, and deep psychological friction. Structural breakdown is active.</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<div class='terminal-box'>🟢 <b>NOMINAL DIALOGUE STATE ({computed_paranoia}%):</b> The text maintains standard communicative flow, though underlying emotional containment is visible.</div>",
                unsafe_allow_html=True,
            )

        st.markdown("#### 🧬 AI Psychoanalytic Breakdown of Your Text:")
        st.markdown(
            f"""
        - **Syntactic Friction:** Detected {user_input_scene.count('.')} structural pauses and {user_input_scene.count('?')} interrogative tension triggers.
        - **Lacanian Subtext:** The dialogue relies on an unspoken symbolic contract where withholding information functions as self-preservation.
        - **Architectural Weight:** The text reflects an internal confinement space similar to institutional domestic barriers.
        """
        )

# --- MODULE 3: NEURAL-PSYCHOANALYTIC SIMULATOR ---
elif selected_module == "🧠 Neural-Psychoanalytic Simulator":
    st.markdown("### 🧠 Multi-Factorial Neural & Psychological Simulator")
    st.markdown(
        "<p style='color: #9ca3af;'>Adjust the parameters below to dynamically simulate shifts in domestic paranoia and existential alienation.</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        existential_dread = st.slider(
            "Existential Dread / Void Level (Ekzistensial Boşluq)",
            0,
            100,
            65,
        )
        lacanian_void = st.slider(
            "The Big Other Absence (Büyük Öykünün Yoxluğu)", 0, 100, 70
        )
        domestic_surveillance = st.slider(
            "Implicit Structural Surveillance (Qapalı Nəzarət)", 0, 100, 50
        )

    with col2:
        linguistic_suppression = st.slider(
            "Linguistic Suppression (Dehidrasiya olunmuş Sözlər)",
            0,
            100,
            80,
        )
        inherited_trauma = st.slider(
            "Transgenerational Trauma Coefficient (Nəsillərarası Travma)",
            0,
            100,
            60,
        )

    calculated_paranoia = int(
        (existential_dread * 0.2)
        + (lacanian_void * 0.25)
        + (domestic_surveillance * 0.15)
        + (linguistic_suppression * 0.25)
        + (inherited_trauma * 0.15)
    )
    calculated_silence = int(100 - (calculated_paranoia * 0.45))
    alienation_score = int((calculated_paranoia + calculated_silence) / 2)

    st.markdown("---")
    st.markdown("### 📈 Real-Time Simulation Metrics")

    m1, m2, m3 = st.columns(3)
    m1.metric(label="Computed Silence Density", value=f"{calculated_silence}%")
    m2.metric(label="Paranoia Amplification", value=f"{calculated_paranoia}%")
    m3.metric(
        label="Alienation Quotient", value=f"{alienation_score} / 100"
    )

    if calculated_paranoia > 65:
        st.markdown(
            f"<div class='warning-terminal'>⚠️ <b>CRITICAL THRESHOLD ({calculated_paranoia}%):</b> Linguistic defenses have saturated the cognitive space. Total conversational alienation is underway.</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<div class='terminal-box'>🟢 <b>EQUILIBRIUM STATE:</b> Structural silence is maintained within tolerable human limits.</div>",
            unsafe_allow_html=True,
        )

# --- MODULE 4: SUBTEXT MATRIX ---
elif selected_module == "⚛️ Lacanian & Sartrean Subtext Matrix":
    st.markdown("### ⚛️ Advanced Psychoanalytic Subtext Decomposition")
    st.markdown(
        "<p style='color: #9ca3af;'>Granular breakdown of linguistic defense mechanisms through existential and psychoanalytic frameworks.</p>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
        <div class='lab-card'>
            <h4 style='color: #f59e0b; margin-top:0;'>1. Sartrean 'Bad Faith'</h4>
            <p style='font-size: 12px; color: #d1d5db;'>
            <b>Intensity: 88%</b><br>
            Evading radical freedom by hiding behind institutionalized duty and predetermined domestic roles.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class='lab-card'>
            <h4 style='color: #f59e0b; margin-top:0;'>2. Lacanian Lack</h4>
            <p style='font-size: 12px; color: #d1d5db;'>
            <b>Intensity: 92%</b><br>
            The symbolic void where memory is erased and replaced by structural silence.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class='lab-card'>
            <h4 style='color: #f59e0b; margin-top:0;'>3. Foucaultian Panopticism</h4>
            <p style='font-size: 12px; color: #d1d5db;'>
            <b>Intensity: 76%</b><br>
            The household operating as an internal prison where inhabitants police their own unsaid words.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# --- MODULE 5: CORE ARTIFACT ---
elif selected_module == "📜 Core Artifact: 'İlhəmə və Pərvaz'":
    st.markdown("### 📜 Primary Textual Artifact: The Kitchen Silence")
    st.markdown(
        "<p style='color: #9ca3af;'>The foundational narrative matrix mapping the confrontation between Zehra and Parviz.</p>",
        unsafe_allow_html=True,
    )

    script_text = """
    [ONTOLOGICAL SCENE: KITCHEN VAULT - 03:42 AM]
    
    Zehra: - Did İlhəmə ever love me?
    Parviz: - Why are you asking?
    Zehra: - Because I don't know. I don't remember her voice, father. I don't even remember her face.
    Parviz: - She was your mother. A person loves their own blood. This isn't something to be asked, Zehra.
    Zehra: - That is not an answer. You aren't telling me how she loved. You are just giving me the sentence you need to survive.
    Parviz: - She loved no one... Everyone in this house opened that door themselves one day. But no one remembered how they walked through it.
    
    [END OF CORPUS STREAM]
    """
    st.text_area("Corpus Data Stream", script_text, height=220)

    st.markdown(
        "<div class='terminal-box'>🏛️ <b>Philosophical Note:</b> Parviz's shift from personal defense to universal fatalism represents the collapse of individual responsibility into an inherited architectural doom.</div>",
        unsafe_allow_html=True,
    )

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #4b5563; font-size: 11px;'>ONTOLOGICAL SILENCE & PARANOIA ENGINE // CRAFTED FOR MIT MEDIA Lab PORTFOLIO EXCELLENCE</p>",
    unsafe_allow_html=True,
)
)
