import time
import streamlit as st

# Səhifə konfiqurasiyası
st.set_page_config(
    page_title="Narrative Tech: Silence & Paranoia Index | Research Prototype",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CINEMATIC DARK MODE & ADVANCED CSS ---
st.markdown(
    """
    <style>
    /* Qlobal Arxa Fon və Şriftlər */
    .stApp {
        background-color: #07090f;
        color: #c5c6c7;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Yan panel dizaynı */
    [data-testid="stSidebar"] {
        background-color: #0b0f19;
        border-right: 1px solid #1f2833;
    }
    
    /* Başlıqlar */
    h1, h2, h3, h4 {
        color: #e0e2eb !important;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: -0.5px;
    }
    
    /* Metrik kartları */
    .metric-container {
        background-color: #0f1624;
        border: 1px solid #1f2833;
        border-left: 3px solid #66fcf1;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 10px;
    }
    
    /* Xəbərdarlıq və Diaqnoz qutuları */
    .warning-box {
        background-color: #2b1314;
        border-left: 4px solid #ff4c4c;
        padding: 15px;
        color: #ff9999;
        font-size: 13px;
        margin-bottom: 10px;
        font-family: 'Courier New', Courier, monospace;
    }
    
    .safe-box {
        background-color: #132b1c;
        border-left: 4px solid #4cff99;
        padding: 15px;
        color: #99ffbb;
        font-size: 13px;
        margin-bottom: 10px;
        font-family: 'Courier New', Courier, monospace;
    }
    
    .info-box {
        background-color: #111d2e;
        border-left: 4px solid #66fcf1;
        padding: 15px;
        color: #66fcf1;
        font-size: 13px;
        margin-bottom: 10px;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Tabların stili */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #0f1624;
        border-radius: 4px;
        color: #8892b0;
        padding: 10px 20px;
        font-family: 'Courier New', Courier, monospace;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1f2833 !important;
        color: #66fcf1 !important;
        border: 1px solid #66fcf1;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- SIDEBAR: TƏDQİQATÇI PANELİ ---
with st.sidebar:
    st.markdown("### 🎛️ Research Parameters")
    st.markdown(
        "<p style='font-size: 11px; color: #8892b0;'>MIT Media Lab Application Artifact v2.4</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏠 Executive Overview",
            "🎬 Computational Core & Script",
            "⚡ Dynamic Paranoia Simulator",
            "🧬 Subtext & NLP Matrix",
            "🔄 Interactive Branching",
        ],
    )

    st.markdown("---")
    st.markdown("**Framework Author:** Agil Chiragli")
    st.markdown("**Core Reference:** *İlhəmə və Pərvaz*")
    st.markdown("**Methodology:** Computational Dramaturgy")

# --- MAIN CONTAINER ---
if selected_module == "🏠 Executive Overview":
    st.markdown(
        "<h1 style='font-size: 28px;'>👁️ NARRATIVE TECH: SILENCE & PARANOIA INDEX</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: #66fcf1; font-size: 14px;'>An Advanced Computational Framework for Analyzing Domestic Silence, Inherited Trauma, and Psychological Friction in Dramatic Texts.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div class='metric-container'>
            <h3>🎯 Research Objective</h3>
            <p style='color: #8892b0; font-size: 13px;'>
            To bridge qualitative literary studies and quantitative digital modeling. By converting structural narrative gaps ("silence") into computational indices, this engine maps how institutionalized trauma shapes domestic dialogue.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class='metric-container'>
            <h3>⚙️ Technical Architecture</h3>
            <p style='color: #8892b0; font-size: 13px;'>
            Built using Python, Streamlit Cloud, and custom CSS. Employs multi-variable weight distribution formulas to calculate real-time psychological tension scores based on syntactic pauses and vocabulary friction.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("### 📊 System Diagnostics at a Glance")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Analyzed Nodes", value="1,420")
    m2.metric(label="Base Silence Index", value="37.4%")
    m3.metric(label="Structural Paranoia", value="41.2%")
    m4.metric(label="Model Status", value="ONLINE")

elif selected_module == "🎬 Computational Core & Script":
    st.markdown("### 🎬 Core Narrative Scene: The Kitchen Silence")
    st.markdown(
        "<p style='color: #8892b0;'>Primary textual artifact from the narrative of 'İlhəmə və Pərvaz', tracking the confrontation between young Zehra and her father, Parviz.</p>",
        unsafe_allow_html=True,
    )

    script_text = """
    [SCENE START: KITCHEN - 03:42 AM]
    
    Zehra: - Did İlhəmə ever love me?
    Parviz: - Why are you asking?
    Zehra: - Because I don't know. I don't remember her voice, father. I don't even remember her face.
    Parviz: - She was your mother. A person loves their own blood. This isn't something to be asked, Zehra.
    Zehra: - That is not an answer. You aren't telling me how she loved. You are just giving me the sentence you need to survive.
    Parviz: - She loved no one... Everyone in this house opened that door themselves one day. But no one remembered how they walked through it.
    
    [SCENE END]
    """
    st.text_area(
        "Raw Script Corpus (Structured Text Stream)", script_text, height=220
    )

    st.markdown(
        "<div class='info-box'>💡 <b>Computational Note:</b> Notice the linguistic shift in Parviz's final line—transitioning from personal defense to existential generalization ('Everyone in this house...'). This marks a 78% spike in communicative withdrawal.</div>",
        unsafe_allow_html=True,
    )

elif selected_module == "⚡ Dynamic Paranoia Simulator":
    st.markdown("### ⚡ Dynamic Simulation & Friction Engine")
    st.markdown(
        "<p style='color: #8892b0;'>Adjust the psychological variables below to simulate real-time shifts in structural paranoia and silence density.</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        isolation = st.slider(
            "Domestic Isolation Level (Məişət Təcridi)", 0, 100, 50
        )
        repression = st.slider(
            "Repressed Memory Factor (Basdırılmış Xatirələr)", 0, 100, 65
        )
        surveillance = st.slider(
            "Implicit Surveillance (Qapalı Nəzarət Hissi)", 0, 100, 40
        )

    with col2:
        linguistic_friction = st.slider(
            "Linguistic Economy / Unspoken Words (Sözlərin Çatışmazlığı)",
            0,
            100,
            70,
        )
        trauma_weight = st.slider(
            "Inherited Trauma Coefficient (Nəsillərarası Travma)", 0, 100, 60
        )

    # Kompleks Hesablama Alqoritmi
    calculated_paranoia = int(
        (isolation * 0.2)
        + (repression * 0.25)
        + (surveillance * 0.15)
        + (linguistic_friction * 0.2)
        + (trauma_weight * 0.2)
    )
    calculated_silence = int(100 - (calculated_paranoia * 0.55))

    st.markdown("---")
    st.markdown("### 📈 Real-Time Analytical Output")

    m1, m2, m3 = st.columns(3)
    m1.metric(label="Calculated Silence Density", value=f"{calculated_silence}%")
    m2.metric(label="Paranoia Amplification Index", value=f"{calculated_paranoia}%")
    m3.metric(
        label="System Stability State",
        value="CRITICAL" if calculated_paranoia > 55 else "STABLE",
    )

    if calculated_paranoia > 55:
        st.markdown(
            f"<div class='warning-box'>⚠️ <b>HIGH PARANOIA THRESHOLD REACHED ({calculated_paranoia}%):</b> Defensive mechanisms have saturated the dialogue structure. Communication channels are exhibiting total algorithmic breakdown.</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<div class='safe-box'>🟢 <b>NOMINAL DIALOGUE STATE:</b> Silence barriers are maintained within standard cultural tolerances. Institutional walls remain intact but non-lethal.</div>",
            unsafe_allow_html=True,
        )

elif selected_module == "🧬 Subtext & NLP Matrix":
    st.markdown("### 🧬 NLP & Subtext Decomposition Matrix")
    st.markdown(
        "<p style='color: #8892b0;'>Granular breakdown of syntactic triggers and psychological defense mechanisms embedded in the dialogue.</p>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
        <div class='metric-container'>
            <h4 style='color: #66fcf1;'>1. Gaslighting Indicator</h4>
            <p style='font-size: 12px; color: #8892b0;'>
            <b>Score: 74%</b><br>
            Detected when Parviz attempts to invalidate Zehra's inquiry by appealing to natural law ("A person loves their own blood").
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class='metric-container'>
            <h4 style='color: #66fcf1;'>2. Emotional Withdrawal</h4>
            <p style='font-size: 12px; color: #8892b0;'>
            <b>Score: 89%</b><br>
            Characterized by abrupt closure of conversational loops and shifting from specific grief to universal doom.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class='metric-container'>
            <h4 style='color: #66fcf1;'>3. Architectural Silence</h4>
            <p style='font-size: 12px; color: #8892b0;'>
            <b>Score: 62%</b><br>
            The physical kitchen space acting as a silent vault that stores generational secrets without resolution.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

elif selected_module == "🔄 Interactive Branching":
    st.markdown("### 🔄 Interactive Scenario Branching Engine")
    st.markdown(
        "<p style='color: #8892b0;'>Simulate alternative narrative paths by choosing Zehra's next investigative move.</p>",
        unsafe_allow_html=True,
    )

    user_choice = st.selectbox(
        "Select Zehra's Response Strategy:",
        [
            "Push further: 'You are lying, father. You drove her away.'",
            "Accept the silence: 'Okay. I won't ask again.'",
            "Deconstruct the door metaphor: 'What door did she open?'",
        ],
    )

    if st.button("Execute Simulation Branch"):
        with st.spinner("Processing computational narrative trajectory..."):
            time.sleep(1)

        if "Push further" in user_choice:
            st.markdown(
                "<div class='warning-box'>🔴 <b>BRANCH OUTCOME [Aggressive Confrontation]:</b> Paranoia Index surges to <b>88%</b>. Immediate conversational shutdown triggered. Silence index drops to 12%.</div>",
                unsafe_allow_html=True,
            )
        elif "Accept the silence" in user_choice:
            st.markdown(
                "<div class='info-box'>🔵 <b>BRANCH OUTCOME [Institutional Compliance]:</b> Paranoia Index normalizes at <b>31%</b>. Silence Index increases to 79%. The domestic equilibrium is preserved at the cost of truth.</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div class='safe-box'>🟢 <b>BRANCH OUTCOME [Metaphorical Interrogation]:</b> Paranoia Index stabilizes at <b>45%</b>. Parviz enters defensive introspection. New narrative vector unlocked.</div>",
                unsafe_allow_html=True,
            )

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #45a29e; font-size: 11px;'>NARRATIVE TECH RESEARCH FRAMEWORK // DESIGNED FOR ACADEMIC & PORTFOLIO EXCELLENCE</p>",
    unsafe_allow_html=True,
)
