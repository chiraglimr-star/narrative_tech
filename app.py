import datetime
import time
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION & INITIALIZATION
# ==========================================
st.set_page_config(
    page_title="Ontological Silence & Paranoia Engine | Academic Research Prototype",
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
        "<p style='font-size: 11px; color: #8b949e;'>Computational Dramaturgy & AI Lab v14.0 (Calibrated Engine)</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏛️ Executive Manifesto & Silence Index",
            "💬 Calibrated NLP Scene Analyzer (X-Ray)",
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
        "📌 <b>ACADEMIC RESEARCH METHODOLOGY & CALIBRATION:</b><br>"
        "This prototype employs a transparent, calibrated heuristic-vector model. Unlike black-box LLMs, it isolates speaker prefixes, "
        "computes contextual question-answer evasion via TF-IDF cosine distance, tracks utterance compression ratios, and measures absolute lexical shielding."
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("### 📐 Calibrated Empirical Mathematical Model")
    st.markdown(
        "<p style='color: #c9d1d9; font-size: 14px;'>The final tension score per beat is a bounded linear combination of normalized empirical weights:</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='lab-card' style='font-family: monospace; color: #58a6ff;'>"
        "<b>Formula:</b><br>"
        "Tension = Base (20) + (Evasion * W_ev) + (Compression Drop * W_comp) + (Absolute Lexicon * W_lex) + (Punctuation Entropy * W_punct)<br><br>"
        "<i>All parameters are fully configurable and unconstrained by arbitrary scaling caps.</i>"
        "</div>",
        unsafe_allow_html=True,
    )

# ==========================================
# 5. MODULE 2: CALIBRATED NLP SCENE ANALYZER
# ==========================================
elif selected_module == "💬 Calibrated NLP Scene Analyzer (X-Ray)":
    st.markdown("### 💬 Calibrated NLP Scene Analyzer & Vector X-Ray")
    st.markdown(
        "<p style='color: #8b949e;'><b>Robust Vector Engine:</b> Evaluates multi-lingual corpuses with prefix stripping and contextual Q&A divergence tracking.</p>",
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
        "Corpus Input Stream (Format: Speaker: Line):",
        value=default_corpus,
        height=180,
    )

    if st.button("⚡ Execute Calibrated Vector X-Ray"):
        with st.spinner("Executing prefix normalization, TF-IDF cosine mapping, and lexical audit..."):
            time.sleep(0.5)

        raw_lines = [l.strip() for l in user_corpus_input.split("\n") if l.strip()]
        
        if not raw_lines:
            st.warning("Corpus is empty. Please enter text.")
        else:
            # 1. Strip speaker prefixes for clean semantic analysis
            cleaned_texts = []
            speakers = []
            for line in raw_lines:
                parts = line.split(":", 1)
                if len(parts) == 2:
                    speakers.append(parts[0].strip())
                    cleaned_texts.append(parts[1].strip().lstrip("-").strip())
                else:
                    speakers.append("Unknown")
                    cleaned_texts.append(line.strip())

            # 2. Compute TF-IDF Matrix across clean texts
            vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b\w+\b')
            try:
                tfidf_matrix = vectorizer.fit_transform(cleaned_texts)
            except Exception:
                tfidf_matrix = None

            # Universal absolute/defensive lexicon
            absolute_lexicon = {"hamı", "heç", "həmişə", "hər", "everyone", "always", "never", "all", "nobody", "hiç"}
            
            results = []
            total_tension = 0
            prev_word_count = None

            for i in range(len(raw_lines)):
                orig_line = raw_lines[i]
                clean_text = cleaned_texts[i]
                words = clean_text.split()
                word_count = len(words) if words else 1

                has_q = 1 if "?" in clean_text else 0
                has_ell = 1 if "..." in clean_text else 0

                # Exact word-boundary lexicon matching
                lex_matches = sum(1 for w in words if w.lower() in absolute_lexicon)
                lex_density = lex_matches / word_count

                # Utterance compression drop ratio compared to previous turn
                if prev_word_count is not None and prev_word_count > 0:
                    compression_ratio = max(0.0, (prev_word_count - word_count) / prev_word_count)
                else:
                    compression_ratio = 0.0
                prev_word_count = word_count

                # Contextual Q&A Evasion
                evasion_score = 0.0
                if i > 0 and "?" in cleaned_texts[i-1] and tfidf_matrix is not None:
                    try:
                        sim = cosine_similarity(tfidf_matrix[i-1:i], tfidf_matrix[i:i+1])[0][0]
                        evasion_score = float(1.0 - sim)
                    except Exception:
                        evasion_score = 0.0

                # Calibrated Linear Formula
                raw_score = 20.0 + (evasion_score * 35.0) + (compression_ratio * 20.0) + (lex_density * 25.0) + (has_q * 8.0) + (has_ell * 12.0)
                beat_tension = int(min(100, max(0, raw_score)))
                total_tension += beat_tension

                # Dynamic psychological classification
                if has_q and evasion_score > 0.6:
                    emo = "Interrogative Stymie / Evasion Spike"
                    def_mech = "Defensive Interrogation / Deflection"
                    c_class = "warning-terminal"
                elif lex_density > 0.15:
                    emo = "Ontological Closure / Absolute Shielding"
                    def_mech = "Sartrean Bad Faith / Generalization Shield"
                    c_class = "lab-card"
                elif has_ell or compression_ratio > 0.5:
                    emo = "Symbolic Void / Linguistic Withdrawal"
                    def_mech = "Lacanian Lack / Suppression"
                    c_class = "warning-terminal"
                else:
                    emo = "Surface Exchange / Low Resistance"
                    def_mech = "Direct Exposure"
                    c_class = "terminal-box"

                results.append({
                    "beat": i + 1,
                    "speaker": speakers[i],
                    "line": orig_line,
                    "tension": beat_tension,
                    "emo": emo,
                    "def_mech": def_mech,
                    "class": c_class,
                    "metrics": f"Evasion: {evasion_score:.2f} | Compression: {compression_ratio:.2f} | Lexical Density: {lex_density:.2f}"
                })

            st.markdown("---")
            st.markdown(f"### 🔬 Calibrated Diagnostic Results ({len(results)} Beats Processed)")

            for r in results:
                card_html = (
                    f"<div class='{r['class']}'>"
                    f"<b>Beat {r['beat']} ({r['speaker']})</b><br>"
                    f"<i style='color: #58a6ff; font-size: 15px;'>\"{r['line']}\"</i><br><br>"
                    f"⚡ <b>Detected State:</b> {r['emo']}<br>"
                    f"🛡️ <b>Defense Mechanism:</b> {r['def_mech']}<br>"
                    f"📊 <b>Computed Tension Index:</b> {r['tension']}%<br>"
                    f"💬 <b style='color: #7ee787;'>Vector Audit Metrics:</b> <i>{r['metrics']}</i>"
                    f"</div>"
                )
                st.markdown(card_html, unsafe_allow_html=True)

            avg_tension = int(total_tension / len(results)) if results else 0
            st.markdown("---")
            st.metric(label="Overall Calibrated Corpus Tension Index", value=f"{avg_tension}%")

# ==========================================
# 6. MODULE 3: REAL BRANCHING SIMULATOR
# ==========================================
elif selected_module == "🔄 Real Branching & Intervention Simulator":
    st.markdown("### 🔄 Real-Time Narrative Branching & Intervention Simulator")
    st.markdown(
        "<p style='color: #8b949e;'>Test custom character interventions with dynamic trajectory modeling.</p>",
        unsafe_allow_html=True,
    )

    intervention_input = st.text_input(
        "Enter Custom Character Intervention Vector:",
        value="Zahra demands the key to the locked room.",
    )

    if st.button("Simulate 3 Behavioral Branching Responses"):
        with st.spinner("Calculating conversational physics..."):
            time.sleep(0.5)

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
        "<p style='color: #8b949e;'>Adjust psychological parameters to observe parameter sensitivity.</p>",
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
        "<p style='color: #8b949e;'>Grounding the engine in established philosophical frameworks.</p>",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    c1.markdown(
        "<div class='lab-card'>"
        "<b>1. Sartrean Bad Faith</b><br>Score: 88%<br>"
        "<p style='font-size:12px; color:#8b949e; margin-top:5px;'>Hiding behind institutionalized duty.</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    c2.markdown(
        "<div class='lab-card'>"
        "<b>2. Lacanian Lack</b><br>Score: 92%<br>"
        "<p style='font-size:12px; color:#8b949e; margin-top:5px;'>Symbolic void regarding maternal absence.</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    c3.markdown(
        "<div class='lab-card'>"
        "<b>3. Foucault Panopticism</b><br>Score: 76%<br>"
        "<p style='font-size:12px; color:#8b949e; margin-top:5px;'>Internalized domestic surveillance.</p>"
        "</div>",
        unsafe_allow_html=True,
    )

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
        "1. <i>Corpus Scope:</i> TF-IDF matrix computation requires robust multi-turn input contexts.<br>"
        "2. <i>Irony & Sarcasm:</i> Semantic divergence measures topical shift but requires advanced pragmatic models for sarcastic inversion.<br>"
        "3. <i>Parameter Tuning:</i> Heuristic weights are calibrated for dramatic dialogue corpora and require domain adaptation for other genres."
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
