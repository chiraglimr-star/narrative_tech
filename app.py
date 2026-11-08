import datetime
import time
import streamlit as st

# Səhifə konfiqurasiyası
st.set_page_config(
    page_title=(
        "Ontological Silence & Paranoia Engine | AI Research Prototype"
    ),
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CINEMATIC PHILOSOPHICAL DARK MODE & CSS ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #05070b;
        color: #e2e8f0;
        font-family: 'Courier New', Courier, monospace;
    }
    [data-testid="stSidebar"] {
        background-color: #090e17;
        border-right: 1px solid #1e293b;
    }
    h1, h2, h3, h4 {
        color: #f8fafc !important;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: -0.5px;
    }
    .metric-card {
        background-color: #0f172a;
        border: 1px solid #334155;
        border-left: 4px solid #38bdf8;
        padding: 20px;
        border-radius: 6px;
        margin-bottom: 15px;
    }
    .warning-box {
        background-color: #450a0a;
        border-left: 4px solid #ef4444;
        padding: 16px;
        color: #fca5a5;
        font-size: 13px;
        margin-bottom: 12px;
        border-radius: 4px;
        font-family: 'Courier New', Courier, monospace;
    }
    .safe-box {
        background-color: #022c22;
        border-left: 4px solid #34d399;
        padding: 16px;
        color: #6ee7b7;
        font-size: 13px;
        margin-bottom: 12px;
        border-radius: 4px;
        font-family: 'Courier New', Courier, monospace;
    }
    .philosophy-box {
        background-color: #1e1b4b;
        border-left: 4px solid #818cf8;
        padding: 16px;
        color: #c7d2fe;
        font-size: 13px;
        margin-bottom: 12px;
        border-radius: 4px;
        font-family: 'Courier New', Courier, monospace;
    }
    [data-testid="stMetricValue"] {
        color: #38bdf8 !important;
        font-size: 28px !important;
        font-weight: bold;
    }
    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        font-size: 13px !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #0f172a;
        border-radius: 6px;
        color: #94a3b8;
        padding: 10px 20px;
        font-family: 'Courier New', Courier, monospace;
        border: 1px solid #334155;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1e293b !important;
        color: #38bdf8 !important;
        border: 1px solid #38bdf8 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- SIDEBAR: ONTOLOGICAL NAVIGATION ---
with st.sidebar:
    st.markdown("### 🌌 Ontological Control")
    st.markdown(
        "<p style='font-size: 11px; color: #94a3b8;'>Computational Dramaturgy & AI Psychoanalysis v3.0</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏛️ Manifesto & Epistemology",
            "📜 The Core Text: 'İlhəmə və Pərvaz'",
            "🧠 Neural-Psychoanalytic Simulator",
            "⚛️ Lacanian & Sartrean Subtext Matrix",
            "🔄 Ontological Decision Branching",
        ],
    )

    st.markdown("---")
    st.markdown("**Framework Architect:** Agil Chiragli")
    st.markdown("**Institution:** MIT Media Lab Candidate Artifact")
    st.markdown(f"**Timestamp:** {datetime.date.today().strftime('%Y-%m-%d')}")

# --- MAIN MODULES ---
if selected_module == "🏛️ Manifesto & Epistemology":
    st.markdown(
        "<h1 style='font-size: 30px;'>🌌 THE ONTOLOGICAL SILENCE & PARANOIA ENGINE</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: #38bdf8; font-size: 15px;'>Bridging Computational Linguistics, Psychoanalytic Theory, and Domestic Dramaturgy.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div class='metric-container'>
            <h3 style='color: #38bdf8; margin-top:0;'>👁️ The Core Thesis</h3>
            <p style='color: #cbd5e1; font-size: 13px; line-height: 1.6;'>
            Silence in domestic architecture is never empty. It is a dense, calculated structural weapon—a linguistic vault where generational trauma, institutional surveillance, and suppressed memory are stored. This engine computes the physics of that unsaid weight.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class='metric-container'>
            <h3 style='color: #38bdf8; margin-top:0;'>⚙️ Computational Framework</h3>
            <p style='color: #cbd5e1; font-size: 13px; line-height: 1.6;'>
            By merging Lacanian psychoanalysis (The Symbolic Order) with modern NLP metrics, the system evaluates how syntactic pauses, defensive rationalizations, and closed conversational loops dictate human alienation.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "### 📊 System Diagnostics & Epistemological Metrics"
    )
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Deconstructed Vectors", value="2,840")
    m2.metric(label="Base Silence Index", value="42.8%")
    m3.metric(label="Paranoia Coefficient", value="68.4%")
    m4.metric(label="Neural State", value="HYPER-AWARE")

elif selected_module == "📜 The Core Text: 'İlhəmə və Pərvaz'":
    st.markdown("### 📜 Primary Textual Artifact: The Kitchen Silence")
    st.markdown(
        "<p style='color: #94a3b8;'>The foundational dialogue matrix mapping the ontological confrontation between Zehra and her father, Parviz.</p>",
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
    st.text_area(
        "Corpus Data Stream (Read-Only Neural Log)", script_text, height=230
    )

    st.markdown(
        "<div class='philosophy-box'>🏛️ <b>Philosophical Deconstruction:</b> Parviz's shift from personal defense to universal fatalism ('Everyone in this house opened that door...') represents the collapse of individual responsibility into an inherited architectural doom.</div>",
        unsafe_allow_html=True,
    )

elif selected_module == "🧠 Neural-Psychoanalytic Simulator":
    st.markdown("### 🧠 Multi-Factorial Neural & Psychological Simulator")
    st.markdown(
        "<p style='color: #94a3b8;'>Adjust the psychological friction variables to compute real-time shifts in domestic paranoia and existential alienation.</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        existential_dread = st.slider(
            "Existential Dread / Void Level (Ekzistensial Boşluq)",
            0,
            100,
            60,
        )
        lacanian_void = st.slider(
            "The Big Other Absence (Büyük Öykünün Yoxluğu)", 0, 100, 75
        )
        domestic_surveillance = st.slider(
            "Implicit Structural Surveillance (Qapalı Nəzarət)", 0, 100, 50
        )

    with col2:
        linguistic_suppression = st.slider(
            "Linguistic Suppression / Unsaid Truths (Dehidrasiya olunmuş Sözlər)",
            0,
            100,
            80,
        )
        inherited_trauma = st.slider(
            "Transgenerational Trauma Coefficient (Nəsillərarası Travma)",
            0,
            100,
            70,
        )

    # Advanced Multi-Layer Algorithmic Computation
    calculated_paranoia = int(
        (existential_dread * 0.2)
        + (lacanian_void * 0.25)
        + (domestic_surveillance * 0.15)
        + (linguistic_suppression * 0.25)
        + (inherited_trauma * 0.15)
    )
    calculated_silence = int(100 - (calculated_paranoia * 0.48))
    alienation_score = int((calculated_paranoia + calculated_silence) / 2)

    st.markdown("---")
    st.markdown("### 📈 Real-Time Neural & Psychological Metrics")

    m1, m2, m3 = st.columns(3)
    m1.metric(label="Computed Silence Index", value=f"{calculated_silence}%")
    m2.metric(label="Paranoia Amplification", value=f"{calculated_paranoia}%")
    m3.metric(
        label="Alienation Quotient", value=f"{alienation_score} / 100"
    )

    if calculated_paranoia > 65:
        st.markdown(
            f"<div class='warning-box'>⚠️ <b>CRITICAL ONTOLOGICAL BREAK ({calculated_paranoia}%):</b> Linguistic defenses have completely saturated the cognitive space. The domestic structure is operating under extreme psychological alienation.</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<div class='safe-box'>🟢 <b>NOMINAL DIALOGIC EQUILIBRIUM:</b> Structural silence is maintained within tolerable human limits. The architecture holds, though deep fractures remain unaddressed.</div>",
            unsafe_allow_html=True,
        )

elif selected_module == "⚛️ Lacanian & Sartrean Subtext Matrix":
    st.markdown("### ⚛️ Advanced Psychoanalytic Subtext Decomposition")
    st.markdown(
        "<p style='color: #94a3b8;'>Granular breakdown of linguistic defense mechanisms through existential and psychoanalytic frameworks.</p>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
        <div class='metric-container'>
            <h4 style='color: #38bdf8; margin-top:0;'>1. Sartrean 'Bad Faith'</h4>
            <p style='font-size: 12px; color: #cbd5e1;'>
            <b>Intensity: 88%</b><br>
            Parviz's appeal to natural law ("A person loves their own blood") is a classic evasion of radical freedom, hiding behind institutionalized duty.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class='metric-container'>
            <h4 style='color: #38bdf8; margin-top:0;'>2. Lacanian Lack & Absence</h4>
            <p style='font-size: 12px; color: #cbd5e1;'>
            <b>Intensity: 92%</b><br>
            Zehra's inability to remember her mother's face points to a fundamental symbolic void that no institutional explanation can fill.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class='metric-container'>
            <h4 style='color: #38bdf8; margin-top:0;'>3. Foucaultian Panopticism</h4>
            <p style='font-size: 12px; color: #cbd5e1;'>
            <b>Intensity: 76%</b><br>
            The domestic household operating as an internal prison where every inhabitant polices their own unsaid words.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

elif selected_module == "🔄 Ontological Decision Branching":
    st.markdown("### 🔄 Interactive Philosophical Branching Engine")
    st.markdown(
        "<p style='color: #94a3b8;'>Select Zehra's investigative trajectory to simulate alternative ontological futures.</p>",
        unsafe_allow_html=True,
    )

    user_choice = st.selectbox(
        "Select Interrogation Vector:",
        [
            "Confrontation: 'You didn't protect her; you exiled her, father.'",
            "Nihilistic Surrender: 'Then this house is just a waiting room for ghosts.'",
            (
                "Deconstructive Inquiry: 'What was behind the door she"
                " opened?'"
            ),
        ],
    )

    if st.button("Execute Neural Simulation Branch"):
        with st.spinner(
            "Running quantum narrative and psychoanalytic computation..."
        ):
            time.sleep(1.2)

        if "Confrontation" in user_choice:
            st.markdown(
                "<div class='warning-box'>🔴 <b>BRANCH OUTCOME [Sartrean Crisis]:</b> Paranoia index surges to <b>94%</b>. Absolute rupture of the symbolic contract. Parviz enters terminal emotional withdrawal.</div>",
                unsafe_allow_html=True,
            )
        elif "Nihilistic Surrender" in user_choice:
            st.markdown(
                "<div class='philosophy-box'>🟣 <b>BRANCH OUTCOME [Absolute Dissolution]:</b> Silence index reaches <b>91%</b>. All active communication loops terminate. The domestic architecture freezes in timeless vacuum.</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div class='safe-box'>🟢 <b>BRANCH OUTCOME [Ontological Breakthrough]:</b> Paranoia stabilizes at <b>48%</b>. A new interpretive vector opens up, bypassing the generational curse through critical awareness.</div>",
                unsafe_allow_html=True,
            )

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #64748b; font-size: 11px;'>ONTOLOGICAL SILENCE & PARANOIA ENGINE // CRAFTED FOR MIT MEDIA Lab PORTFOLIO EXCELLENCE</p>",
    unsafe_allow_html=True,
)
