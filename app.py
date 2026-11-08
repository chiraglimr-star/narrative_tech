import streamlit as st

# Səhifənin tənzimlənməsi
st.set_page_config(
    page_title="Narrative Tech: Silence & Paranoia Index",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- CINEMATIC DARK MODE & CUSTOM CSS ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #c5c6c7;
        font-family: 'Courier New', Courier, monospace;
    }
    h1, h2, h3 {
        color: #e0e2eb !important;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: -1px;
    }
    .warning-box {
        background-color: #2b1314;
        border-left: 4px solid #ff4c4c;
        padding: 15px;
        color: #ff9999;
        font-size: 14px;
        margin-bottom: 10px;
    }
    .safe-box {
        background-color: #132b1c;
        border-left: 4px solid #4cff99;
        padding: 15px;
        color: #99ffbb;
        font-size: 14px;
        margin-bottom: 10px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- HEADER SECTION ---
st.markdown(
    "<h1 style='font-size: 32px;'>👁️ NARRATIVE TECH: SILENCE & PARANOIA INDEX</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='color: #66fcf1; font-size: 14px;'>Computational Dramaturgy & Psychological Analysis Engine | Based on 'İlhəmə və Pərvaz'</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# --- TABLAR ---
tab1, tab2 = st.tabs(
    ["🎬 Core Scene & Script", "⚡ Interactive Paranoia Engine"]
)

with tab1:
    st.markdown("### Core Narrative Scene: The Kitchen Silence")
    st.markdown(
        "<p style='color: #8892b0;'>A critical confrontation between young Zehra and her father, Parviz, highlighting institutionalized silence.</p>",
        unsafe_allow_html=True,
    )

    script_text = """
    - Did İlhəmə ever love me?
    - Why are you asking?
    - Because I don't know. I don't remember her voice, father. I don't even remember her face.
    - She was your mother. A person loves their own blood. This isn't something to be asked, Zehra.
    - That is not an answer. You aren't telling me how she loved. You are just giving me the sentence you need to survive.
    - She loved no one... Everyone in this house opened that door themselves one day. But no one remembered how they walked through it.
    """
    st.text_area("Script Excerpt (Read-Only)", script_text, height=180)
    st.markdown(
        "<div class='safe-box'>💡 <b>Subtext Analysis:</b> This scene reflects invisible domestic walls, inherited trauma, and the heavy burden of unspoken truths.</div>",
        unsafe_allow_html=True,
    )

with tab2:
    st.markdown(
        "### Dynamic Simulation Engine: Adjust Parameters"
    )
    st.markdown(
        "<p style='color: #8892b0;'>Simulate psychological tension by adjusting environmental and emotional friction factors.</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        isolation = st.slider(
            "Domestic Isolation Level (Təcrid dərəcəsi)", 0, 100, 45
        )
        repression = st.slider(
            "Repressed Memory Factor (Basdırılmış xatirələr)", 0, 100, 60
        )

    with col2:
        paranoia_multiplier = st.slider(
            "Paranoia Amplification (Paranoya intensivliyi)", 0, 100, 50
        )

    calculated_paranoia = int(
        (isolation * 0.3) + (repression * 0.4) + (paranoia_multiplier * 0.3)
    )
    calculated_silence = int(100 - (calculated_paranoia * 0.6))

    st.markdown("---")

    m1, m2, m3 = st.columns(3)
    m1.metric(label="Total Word Count", value="94")
    m2.metric(label="Calculated Silence Index", value=f"{calculated_silence}%")
    m3.metric(
        label="Real-Time Paranoia Level", value=f"{calculated_paranoia}%"
    )

    st.markdown("### Psychological Diagnostics")
    if calculated_paranoia > 50:
        st.markdown(
            f"<div class='warning-box'>⚠️ <b>CRITICAL TENSION DETECTED ({calculated_paranoia}%):</b> High presence of defensive mechanisms, communicative walls, and structural paranoia. Dialogue breakdown is imminent.</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<div class='safe-box'>🟢 <b>STABLE DIALOGUE:</b> Silence barriers are maintained at standard levels, though underlying tension persists.</div>",
            unsafe_allow_html=True,
        )
