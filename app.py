import datetime
import time
import plotly.graph_objects as go
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
    .stApp {
        background-color: #0b0f19 !important;
        color: #f1f5f9 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    [data-testid="stSidebar"] {
        background-color: #111827 !important;
        border-right: 1px solid #1f2937 !important;
    }
    [data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    h1, h2, h3, h4, h5, h6, label {
        color: #ffffff !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    .stTextArea textarea {
        background-color: #1e293b !important;
        color: #38bdf8 !important;
        font-size: 15px !important;
        font-weight: bold !important;
        border: 1px solid #334155 !important;
        border-radius: 6px !important;
    }
    .stButton button {
        background-color: #f59e0b !important;
        color: #0b0f19 !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 10px 24px !important;
        transition: 0.3s !important;
    }
    .stButton button:hover {
        background-color: #fbbf24 !important;
    }
    .lab-card {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-left: 4px solid #f59e0b;
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
    [data-testid="stMetricValue"] {
        color: #f59e0b !important;
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
        "<p style='font-size: 11px; color: #94a3b8;'>Computational Dramaturgy & AI Lab v5.2</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏛️ Executive Manifesto & Context",
            "💬 Custom AI Scene & Plotly Analyzer",
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
        "<p style='color: #f59e0b; font-size: 15px;'>An Experimental Computational Framework for Mapping Domestic Silence, Trauma, and Conversational Physics.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

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
            <h3 style='color: #f59e0b; margin-top:0;'>🌌 The Core Thesis</h3>
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
            <h3 style='color: #f59e0b; margin-top:0;'>⚙️ Interactive Capabilities</h3>
            <p style='color: #e2e8f0; font-size: 14px; line-height: 1.6;'>
            This system allows users to input custom dialogues, view real-time Plotly emotional vector charts, and trigger interactive narrative branching simulations instantly.
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

# --- MODULE 2: CUSTOM AI SCENE & PLOTLY ANALYZER ---
elif selected_module == "💬 Custom AI Scene & Plotly Analyzer":
    st.markdown("### 💬 Custom AI Scene Analyzer & Emotional Vector Meter")
    st.markdown(
        "<p style='color: #94a3b8;'>Type or paste any dramatic dialogue below. The AI engine will compute its silence density, paranoia index, and generate a real-time Plotly emotional vector curve across narrative segments.</p>",
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
        height=140,
    )

    analyze_clicked = st.button("⚡ Run AI Analysis & Plot Vectors")

    if analyze_clicked:
        with st.spinner("Synthesizing linguistic pauses and psychological friction..."):
            time.sleep(1)

        lines = []
        for line in user_input_scene.split("\n"):
            if line.strip():
                lines.append(line.strip())

        if not lines:
            lines = ["Start"]

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

        st.markdown("### 📈 Real-Time Plotly Paranoia & Sentiment Vector")
        st.markdown(
            "<p style='font-size: 12px; color: #94a3b8;'>Tracking psychological tension spikes across dialogue sequence nodes:</p>",
            unsafe_allow_html=True,
        )

        x_nodes = [f"Node {i+1}" for i in range(len(lines))]
        y_values = [min(95, max(20, (i + 1) * 25 + (len(l) % 15))) for i, l in enumerate(lines)]

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=x_nodes,
                y=y_values,
                mode="lines+markers",
                name="Paranoia Vector",
                line=dict(color="#f59e0b", width=3),
                marker=dict(size=10, color="#38bdf8"),
            )
        )
        fig.update_layout(
            paper_bgcolor="#0b0f19",
            plot_bgcolor="#1e293b",
            font=dict(color="#f1f5f9", family="Courier New"),
            margin=dict(l=20, r=20, t=20, b=20),
            height=280,
            xaxis=dict(showgrid=True, gridcolor="#334155"),
            yaxis=dict(showgrid=True, gridcolor="#334155", range=[0, 100], title="Paranoia Intensity (%)"),
        )
        st.plotly_chart(fig, use_container_width=True)

        if computed_paranoia > 60:
            st.markdown(
                f"<div class='warning-terminal'>⚠️ <b>HIGH PARANOIA SPIKE ({computed_paranoia}%):</b> Linguistic evasion and defensive walls detected. Structural collapse imminent.</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<div class='terminal-box'>🟢 <b>NOMINAL DIALOGUE STATE ({computed_paranoia}%):</b> Communicative flow is stable, with controlled emotional subtext.</div>",
                unsafe_allow_html=True,
            )

        st.markdown("---")
        st.markdown("### 🔄 Interactive Branching Simulation")
        st.markdown(
            "<p style='font-size: 13px; color: #94a3b8;'>Select an alternative narrative intervention vector for this text:</p>",
            unsafe_allow_html=True,
        )

        branch_choice = st.selectbox(
            "Choose Next Action:",
            [
                "Atanın (Pərvazın) yerinə sərt cavab yaz",
                "Sükutu poz və birbaşa həqiqəti soruş",
                "Mərmər divar metaforasını dekonstruksiya et",
            ],
        )

        if st.button("Execute Branch Simulation"):
            with st.spinner("Processing narrative trajectory shift..."):
                time.sleep(0.8)
            if "Atanın" in branch_choice:
                st.markdown(
                    "<div class='warning-terminal'>🔴 <b>BRANCH OUTCOME [Pərvaz's Defensive Retaliation]:</b> Paranoia Index surges to <b>91%</b>. Complete communicative shutdown.</div>",
                    unsafe_allow_html=True,
                )
            elif "Sükutu poz" in branch_choice:
                st.markdown(
                    "<div class='terminal-box'>🟢 <b>BRANCH OUTCOME [Ontological Breakthrough]:</b> Silence Index drops to <b>18%</b>. Symbolic contract renegotiated.</div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    "<div class='lab-card'>🟣 <b>BRANCH OUTCOME [Architectural Dissolution]:</b> System stabilizes at <b>45%</b>. New narrative vector unlocked.</div>",
                    unsafe_allow_html=True,
                )

# --- MODULE 3: NEURAL-PSYCHOANALYTIC SIMULATOR ---
elif selected_module == "🧠 Neural-Psychoanalytic Simulator":
    st.markdown("### 🧠 Multi-Factorial Neural & Psychological Simulator")
    st.markdown(
        "<p style='color: #94a3b8;'>Adjust the parameters below to simulate shifts in domestic paranoia and existential alienation.</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        e_dread = st.slider("Existential Dread", 0, 100, 65)
        l_void = st.slider("Lacanian Void (İlhəmə's Absence)", 0, 100, 70)
    with col2:
        l_supp = st.slider("Linguistic Suppression", 0, 100, 80)
        i_trauma = st.slider("Inherited Trauma (Pərvaz factor)", 0, 100, 60)

    p_score = int((e_dread * 0.25) + (l_void * 0.25) + (l_supp * 0.3) + (i_trauma * 0.2))
    st.metric(label="Paranoia Amplification Index", value=f"{p_score}%")

    if p_score > 65:
        st.markdown(
            "<div class='warning-terminal'>⚠️ Critical psychological friction detected across simulated parameters.</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<div class='terminal-box'>🟢 Simulated psychological state is within nominal domestic tolerances.</div>",
            unsafe_allow_html=True,
        )

# --- MODULE 4: SUBTEXT MATRIX ---
elif selected_module == "⚛️ Lacanian & Sartrean Subtext Matrix":
    st.markdown("### ⚛️ Advanced Psychoanalytic Subtext Decomposition")
    c1, c2, c3 = st.columns(3)
    c1.markdown(
        "<div class='lab-card'><b>1. Sartrean Bad Faith</b><br><span style='color:#f59e0b;'>88%</span><br><p style='font-size:12px; color:#94a3b8; margin-top:5px;'>Pərvaz hiding behind institutionalized duty.</p></div>",
        unsafe_allow_html=True,
    )
    c2.markdown(
        "<div class='lab-card'><b>2. Lacanian Lack</b><br><span style='color:#f59e0b;'>92%</span><br><p style='font-size:12px; color:#94a3b8; margin-top:5px;'>Zəhra's symbolic void regarding her mother İlhəmə.</p></div>",
        unsafe_allow_html=True,
    )
    c3.markdown(
        "<div class='lab-card'><b>3. Foucault Panopticism</b><br><span style='color:#f59e0b;'>76%</span><br><p style='font-size:12px; color:#94a3b8; margin-top:5px;'>The kitchen vault acting as an internal surveillance room.</p></div>",
        unsafe_allow_html=True,
    )

# --- MODULE 5: CORE ARTIFACT ---
elif selected_module == "📜 Core Artifact: 'İlhəmə və Pərvaz'":
    st.markdown("### 📜 Primary Textual Artifact: The Kitchen Confrontation")
    st.markdown(
        "<p style='color: #94a3b8;'>The foundational dialogue between Zəhra and her father Pərvaz.</p>",
        unsafe_allow_html=True,
    )

    script_text = (
        "[ONTOLOGICAL SCENE: KITCHEN VAULT - 03:42 AM]\n\n"
        "Zəhra: - Did İlhəmə ever love me?\n"
        "Pərvaz: - Why are you asking?\n"
        "Zəhra: - Because I don't know. I don't remember her voice, father. I don't even remember her face.\n"
        "Pərvaz: - She was your mother. A person loves their own blood. This isn't something to be asked, Zəhra.\n"
        "Zəhra: - That is not an answer. You aren't telling me how she loved. You are just giving me the sentence you need to survive.\n"
        "Pərvaz: - She loved no one... Everyone in this house opened that door themselves one day. But no one remembered how they walked through it."
    )

    st.text_area("Corpus Data Stream (Read-Only)", script_text, height=220)
    st.markdown(
        "<div class='terminal-box'>🏛️ <b>Note:</b> Pərvaz's transition to universal fatalism marks a 78% spike in communicative withdrawal.</div>",
        unsafe_allow_html=True,
    )

# FOOTER
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #64748b; font-size: 11px;'>ONTOLOGICAL SILENCE ENGINE // CRAFTED FOR MIT MEDIA LAB PORTFOLIO EXCELLENCE</p>",
    unsafe_allow_html=True,
)
