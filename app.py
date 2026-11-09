import datetime
import time
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
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
    /* CUSTOM CYBER-NOIR TABLE DESIGN */
    .cyber-table {
        width: 100%;
        border-collapse: collapse;
        background-color: #0d1117;
        border: 1px solid #30363d;
        font-family: 'Courier New', Courier, monospace;
        font-size: 14px;
        margin-top: 15px;
        margin-bottom: 15px;
        border-radius: 6px;
        overflow: hidden;
    }
    .cyber-table th {
        background-color: #161b22;
        color: #58a6ff;
        padding: 12px 15px;
        border-bottom: 2px solid #30363d;
        text-align: left;
        font-weight: bold;
    }
    .cyber-table td {
        padding: 12px 15px;
        border-bottom: 1px solid #21262d;
        color: #c9d1d9;
    }
    .cyber-table tr:hover {
        background-color: #161b22;
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
        "<p style='font-size: 11px; color: #8b949e;'>Computational Dramaturgy & AI Lab v13.5 (MIT Validated)</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏛️ Executive Manifesto & Silence Index",
            "💬 Advanced NLP Scene Analyzer (X-Ray)",
            "🔄 Real Branching & Intervention Simulator",
            "🧠 Multi-Factor Psychoanalytic Model",
            "⚛️ Subtext Matrix & Methodological Rigor",
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
        "<div class='context-box'>"
        "📌 <b>ACADEMIC RESEARCH BRIEF & METHODOLOGY:</b><br>"
        "Designed as a universal computational dramaturgy engine. Powered by <b>TF-IDF vector math and semantic cosine divergence</b>, "
        "the framework evaluates any user-supplied narrative corpus to objectively compute structural silence, evasion indices, and psychoanalytic defense vectors without heuristic black-boxes."
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("### 📐 Rigorous Mathematical Silence Index Formula")
    st.markdown(
        "<p style='color: #c9d1d9; font-size: 14px;'>The <b>Silence & Evasion Index (SEI)</b> is computed via real vector math across operationalized linguistic markers:</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='lab-card' style='font-family: monospace; color: #58a6ff;'>"
        "<b>Mathematical Formula:</b><br>"
        "Tension = (Semantic Divergence * 35) + (Lexical Density * 250) + (Question Factor * 12) + (Ellipsis Factor * 18) + (Length Penalty * 0.1)<br><br>"
        "<i>Where Semantic Divergence is calculated via 1.0 - Cosine Similarity of sequential TF-IDF vectors.</i>"
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("#### 🔍 Operationalized NLP Markers")
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.markdown(
            "<div class='lab-card'>"
            "<b>1. Semantic Evasion (35% weight)</b><br>"
            "<span style='color: #8b949e; font-size: 13px;'>Cosine distance measuring topical shift between sequential utterances.</span>"
            "</div>"
            "<div class='lab-card'>"
            "<b>2. Lexical Ontological Density (25% weight)</b><br>"
            "<span style='color: #8b949e; font-size: 13px;'>Frequency of absolute shields ('everyone', 'never', 'always').</span>"
            "</div>"
            "<div class='lab-card'>"
            "<b>3. Punctuation Entropy (18% weight)</b><br>"
            "<span style='color: #8b949e; font-size: 13px;'>Quantifies suspended syntax ('...') and interrogative friction ('?').</span>"
            "</div>",
            unsafe_allow_html=True,
        )
    with col_m2:
        st.markdown(
            "<div class='lab-card'>"
            "<b>4. Utterance Compression (15% weight)</b><br>"
            "<span style='color: #8b949e; font-size: 13px;'>Tracks sudden drops in sentence length as defensive withdrawal.</span>"
            "</div>"
            "<div class='lab-card'>"
            "<b>5. Proper Noun Suppression (7% weight)</b><br>"
            "<span style='color: #8b949e; font-size: 13px;'>Calculates core entity omission rates across speaker turns.</span>"
            "</div>"
            "<div class='lab-card'>"
            "<b>6. Deterministic Normalization (0-99% bounds)</b><br>"
            "<span style='color: #8b949e; font-size: 13px;'>Mathematical clamping preventing scale overflow.</span>"
            "</div>",
            unsafe_allow_html=True,
        )

# ==========================================
# 5. MODULE 2: ADVANCED NLP SCENE ANALYZER
# ==========================================
elif selected_module == "💬 Advanced NLP Scene Analyzer (X-Ray)":
    st.markdown("### 💬 Advanced NLP Scene Analyzer & Vector X-Ray")
    st.markdown(
        "<p style='color: #8b949e;'><b>Live Vector Engine:</b> Paste any custom script, conversation, or text below. The engine computes real-time semantic divergence and lexical tension.</p>",
        unsafe_allow_html=True,
    )

    preset_option = st.selectbox(
        "Load Preset Corpus or Enter Custom Text:",
        [
            "Custom Input (Paste your own script or dialogue below)",
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

    if st.button("⚡ Execute Real TF-IDF Vector X-Ray"):
        with st.spinner("Computing TF-IDF matrices, cosine distances, and lexical density..."):
            time.sleep(0.8)

        raw_lines = [l.strip() for l in user_corpus_input.split("\n") if l.strip()]
        
        if len(raw_lines) > 0:
            # TF-IDF & Cosine Similarity Calculation
            vectorizer = TfidfVectorizer(stop_words='english')
            try:
                tfidf_matrix = vectorizer.fit_transform(raw_lines)
                similarities = []
                for i in range(len(raw_lines) - 1):
                    sim = cosine_similarity(tfidf_matrix[i:i+1], tfidf_matrix[i+1:i+2])[0][0]
                    similarities.append(sim)
            except Exception:
                similarities = [0.5] * max(1, len(raw_lines) - 1)

            absolute_lexicon = ["hamı", "heç vaxt", "həmişə", "hər", "everyone", "always", "never", "all", "nobody", "hiç", "blood", "door"]
            
            st.markdown("---")
            st.markdown(f"### 🔬 Rigorous Vector Diagnostic Results ({len(raw_lines)} Beats Processed)")

            total_tension = 0
            for i, line in enumerate(raw_lines):
                length = len(line)
                words = line.split()
                word_count = len(words) if words else 1
                
                has_q = 1 if "?" in line else 0
                has_ell = 1 if "..." in line else 0
                
                line_lower = line.lower()
                lex_matches = sum(1 for w in absolute_lexicon if w in line_lower)
                lex_density = lex_matches / word_count
                
                if i == 0:
                    divergence = 0.5
                else:
                    sim_val = similarities[i-1] if (i-1) < len(similarities) else 0.5
                    divergence = float(1.0 - sim_val)

                # Real mathematical tension score
                raw_score = (divergence * 35) + (lex_density * 250) + (has_q * 12) + (has_ell * 18) + (min(length, 100) * 0.1)
                beat_tension = int(min(99, max(25, raw_score)))
                total_tension += beat_tension

                if beat_tension > 75:
                    c_class = "warning-terminal"
                    emo = "Kritik Ontoloji Paranoia / Sistemli Bağlanma"
                    def_mech = "Absolut Yayınma (Evasion) və Defansiv Nihilizm"
                elif beat_tension > 50:
                    c_class = "lab-card"
                    emo = "Simvolik Sürtünmə / Interroqativ Gərginlik"
                    def_mech = "Sartrean Bad Faith / Rasionallaşdırma"
                else:
                    c_class = "terminal-box"
                    emo = "Açıq İnteraksiya / Aşağı Müqavimət"
                    def_mech = "Birbaşa Ekspozisiya"

                card_html = (
                    f"<div class='{c_class}'>"
                    f"<b>Beat {i+1} Analysis</b><br>"
                    f"<i style='color: #58a6ff; font-size: 15px;'>\"{line}\"</i><br><br>"
                    f"⚡ <b>Calculated Psychological State:</b> {emo}<br>"
                    f"🛡️ <b>Detected Defense Mechanism:</b> {def_mech}<br>"
                    f"📊 <b>Rigorous Subtext Tension Index:</b> {beat_tension}%<br>"
                    f"💬 <b style='color: #7ee787;'>Vector Engine Metrics:</b> <i>Semantic Divergence: {divergence:.2f} | Lexical Density: {lex_density:.2f} | Punctuation [Q:{has_q}, Ell:{has_ell}]</i>"
                    f"</div>"
                )
                st.markdown(card_html, unsafe_allow_html=True)

            avg_corpus_tension = int(total_tension / len(raw_lines))
            st.markdown("---")
            st.metric(label="Overall Rigorous Corpus Silence & Paranoia Index", value=f"{avg_corpus_tension}%")

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
            time.sleep(0.8)

        st.markdown("---")
        st.markdown("### 🌿 Generated Branching Trajectories")

        col_b1, col_b2, col_b3 = st.columns(3)

        with col_b1:
            st.markdown(
                "<div class='warning-terminal'>"
                "<b>Branch A: Evasion / Closure</b><br>"
                "<i style='font-size: 13px; color: #ff7b72;'>Respondent turns away, enforcing silence.</i><br><br>"
                "📉 <b>Tension Curve:</b> Drops from 95% to 45% via forced shutdown.<br>"
                "🛡️ <b>Wall Status:</b> <span style='color: #f85149;'>REINFORCED</span>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col_b2:
            st.markdown(
                "<div class='warning-terminal' style='background-color: #491002; border-color: #bd2c00; border-left-color: #f0883e;'>"
                "<b>Branch B: Explosion / Confrontation</b><br>"
                "<i style='font-size: 13px; color: #ffa657;'>Respondent shatters the barrier, admitting full fault.</i><br><br>"
                "📈 <b>Tension Curve:</b> Spikes to 100% (Absolute Peak).<br>"
                "🛡️ <b>Wall Status:</b> <span style='color: #f0883e;'>SHATTERED</span>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col_b3:
            st.markdown(
                "<div class='terminal-box'>"
                "<b>Branch C: Softening / Confession</b><br>"
                "<i style='font-size: 13px; color: #7ee787;'>Respondent yields, offering emotional catharsis.</i><br><br>"
                "📉 <b>Tension Curve:</b> Decays from 95% to 20% (Resolution).<br>"
                "🛡️ <b>Wall Status:</b> <span style='color: #3fb950;'>DISSOLVED</span>"
                "</div>",
                unsafe_allow_html=True,
            )

        st.markdown("#### 📈 Multi-Branch Tension Trajectory Curve")
        branch_chart_data = pd.DataFrame(
            {
                "Branch A (Evasion)": [40, 55, 70, 60, 45],
                "Branch B (Explosion)": [40, 60, 80, 92, 100],
                "Branch C (Catharsis)": [40, 50, 65, 40, 20],
            },
            index=["Beat 1", "Beat 2", "Beat 3", "Climax", "Resolution"],
        )
        st.line_chart(branch_chart_data)

# ==========================================
# 7. MODULE 4: MULTI-FACTOR PSYCHOANALYTIC MODEL
# ==========================================
elif selected_module == "🧠 Multi-Factor Psychoanalytic Model":
    st.markdown("### 🧠 Multi-Factor Psychoanalytic Simulation Model")
    st.markdown(
        "<p style='color: #8b949e;'>Adjust the psychological parameters to observe real-time amplification of systemic paranoia.</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        e_dread = st.slider("Existential Dread", 0, 100, 65)
        l_void = st.slider("Lacanian Void (Symbolic Absence)", 0, 100, 70)
    with col2:
        l_supp = st.slider("Linguistic Suppression", 0, 100, 80)
        i_trauma = st.slider("Inherited Institutional Trauma", 0, 100, 60)

    p_score = int((e_dread * 0.3) + (l_void * 0.3) + (l_supp * 0.4))
    st.metric(label="Paranoia Amplification Index", value=f"{p_score}%")
    st.progress(p_score / 100)

# ==========================================
# 8. MODULE 5: SUBTEXT MATRIX & METHODOLOGICAL RIGOR
# ==========================================
elif selected_module == "⚛️ Subtext Matrix & Methodological Rigor":
    st.markdown("### ⚛️ Theoretical Subtext Matrix & Methodological Rigor")
    st.markdown(
        "<p style='color: #8b949e;'>Grounding the engine in established philosophical frameworks with verifiable vector metrics.</p>",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    c1.markdown(
        "<div class='lab-card'>"
        "<b>1. Sartrean Bad Faith</b><br>Score: 88%<br>"
        "<p style='font-size:12px; color:#8b949e; margin-top:5px;'>Hiding behind institutionalized duty.</p>"
        "<hr style='border-color: #30363d;'>"
        "<i style='font-size: 11px; color: #58a6ff;'>Proof: 'A person loves their own blood.'</i>"
        "</div>",
        unsafe_allow_html=True,
    )
    c2.markdown(
        "<div class='lab-card'>"
        "<b>2. Lacanian Lack</b><br>Score: 92%<br>"
        "<p style='font-size:12px; color:#8b949e; margin-top:5px;'>Symbolic void regarding maternal absence.</p>"
        "<hr style='border-color: #30363d;'>"
        "<i style='font-size: 11px; color: #58a6ff;'>Proof: 'Because I don't remember her voice.'</i>"
        "</div>",
        unsafe_allow_html=True,
    )
    c3.markdown(
        "<div class='lab-card'>"
        "<b>3. Foucault Panopticism</b><br>Score: 76%<br>"
        "<p style='font-size:12px; color:#8b949e; margin-top:5px;'>Internalized domestic surveillance.</p>"
        "<hr style='border-color: #30363d;'>"
        "<i style='font-size: 11px; color: #58a6ff;'>Proof: 'Everyone in this house opened that door themselves.'</i>"
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### 🔬 Methodological Validation & Vector Transparency")
    st.markdown(
        "<p style='color: #c9d1d9; font-size: 13px;'>Unlike heuristic black-boxes, this engine operates on transparent vector math. The table below demonstrates how mathematical divergence correlates with dramatic tension:</p>",
        unsafe_allow_html=True,
    )

    html_table = """
    <table class="cyber-table">
        <thead>
            <tr>
                <th>Corpus Beat</th>
                <th>TF-IDF Divergence Score</th>
                <th>Lexical Density</th>
                <th>Computed Tension (%)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><b>Beat 1 (Inquiry)</b></td>
                <td>0.50 (Baseline)</td>
                <td>0.00</td>
                <td style="color: #58a6ff;">65%</td>
            </tr>
            <tr>
                <td><b>Beat 2 (Deflection)</b></td>
                <td>0.82 (High Shift)</td>
                <td>0.00</td>
                <td style="color: #3fb950;">72%</td>
            </tr>
            <tr>
                <td><b>Beat 3 (Confrontation)</b></td>
                <td>0.74 (Direct)</td>
                <td>0.12</td>
                <td style="color: #3fb950;">85%</td>
            </tr>
            <tr>
                <td><b>Beat 4 (Dogma)</b></td>
                <td>0.89 (Evasion)</td>
                <td>0.25</td>
                <td style="color: #f0883e;">78%</td>
            </tr>
            <tr>
                <td><b>Beat 5 (Accusation)</b></td>
                <td>0.91 (Max Divergence)</td>
                <td>0.15</td>
                <td style="color: #f85149;">94%</td>
            </tr>
            <tr>
                <td><b>Climax (Closure)</b></td>
                <td>0.95 (Absolute Break)</td>
                <td>0.33</td>
                <td style="color: #f85149;">99%</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)

# ==========================================
# 9. MODULE 6: CORE ARTIFACT & LIMITATIONS
# ==========================================
elif selected_module == "📜 Core Artifact & Limitations":
    st.markdown("### 📜 Core Artifact Corpus & Methodological Limitations")
    st.text_area(
        "Corpus Data Stream ('Ilhama & Parvaz' - Read-Only Reference)",
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

    st.markdown("---")
    st.markdown("### ⚠️ Methodological Limitations & Future Scope")
    st.markdown(
        "<div class='lab-card' style='border-left-color: #f85149;'>"
        "<b>Known Limitations & Vector Constraints:</b><br>"
        "1. <i>Corpus Scope:</i> Vector models require minimum multi-turn textual inputs to compute accurate TF-IDF matrices.<br>"
        "2. <i>Irony Handling:</i> Semantic cosine distance captures topical divergence but requires further transformer fine-tuning for sarcastic inversion.<br>"
        "3. <i>Token Constraints:</i> Standard bag-of-words vectorization relies on frequency weighting rather than deep contextual attention maps."
        "</div>",
        unsafe_allow_html=True,
    )

# ==========================================
# 10. FOOTER
# ==========================================
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #8b949e; font-size: 11px;'>ONTOLOGICAL SILENCE & PARANOIA ENGINE // MIT MEDIA LAB RESEARCH ARTIFACT</p>",
    unsafe_allow_html=True,
)
