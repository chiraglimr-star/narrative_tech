import datetime
import time
import html
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
# 3. SIDEBAR NAVIGATION & WHITE-BOX CONTROLS
# ==========================================
with st.sidebar:
    st.markdown("### 👁️ Terminal Control")
    st.markdown(
        "<p style='font-size: 11px; color: #8b949e;'>Computational Dramaturgy Lab v17.2 (Universal Input Edition)</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    selected_module = st.radio(
        "Navigation Matrix",
        [
            "🏛️ Executive Manifesto & Framework",
            "💬 Universal NLP Scene Analyzer (X-Ray)",
            "🔄 Rule-Based Branching Demonstrator",
            "⚛️ Dynamic Theoretical Marker Index",
            "📊 Validation Protocol & Empirical Design",
            "📜 Core Artifact & Limitations",
        ],
    )

    st.markdown("---")
    st.markdown("### ⚙️ White-Box Hyperparameters")
    st.markdown("<p style='font-size: 11px; color: #8b949e;'>Adjust heuristic weights to test model sensitivity.</p>", unsafe_allow_html=True)
    
    w_evasion = st.slider("W_evasion (Semantic Divergence)", 0.0, 50.0, 35.0, 5.0)
    w_compression = st.slider("W_compression (Intra-Speaker Drop)", 0.0, 40.0, 20.0, 5.0)
    w_lexical = st.slider("W_lexical (Generalization Marker)", 0.0, 40.0, 25.0, 5.0)
    w_punctuation = st.slider("W_punctuation (Pause / Interrogation)", 0.0, 30.0, 15.0, 5.0)

    st.markdown("---")
    st.markdown("**Framework Architect:** Agil Chiragli")
    st.markdown("**Target Research Laboratory:** MIT Media Lab (Review Portfolio)")
    st.markdown(f"**Date:** {datetime.date.today().strftime('%Y-%m-%d')}")

# ==========================================
# 4. MODULE 1: MANIFESTO & FRAMEWORK
# ==========================================
if selected_module == "🏛️ Executive Manifesto & Framework":
    st.markdown("<h1 style='font-size: 30px;'>👁️ THE ONTOLOGICAL SILENCE & PARANOIA ENGINE</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #f0883e; font-size: 15px;'>An Academic Computational Framework for Mapping Domestic Silence, Trauma, and Conversational Physics.</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown(
        "<div class='context-box'>"
        "📌 <b>UNIVERSAL INPUT PARSING & AUDIT STANDARDS:</b><br>"
        "This experimental prototype supports both complex dialogue corpuses and single-word/short-phrase inputs. "
        "It evaluates semantic valence, contextual topic shifts, and lexical markers robustly across any conversational scenario."
        "</div>",
        unsafe_allow_html=True,
    )

# ==========================================
# 5. MODULE 2: UNIVERSAL NLP SCENE ANALYZER
# ==========================================
elif selected_module == "💬 Universal NLP Scene Analyzer (X-Ray)":
    st.markdown("### 💬 Universal NLP Scene Analyzer & Vector X-Ray")
    st.markdown(
        "<p style='color: #8b949e;'><b>Universal Engine:</b> Handles full dialogues, single words, or short phrases dynamically with context-aware calibration.</p>",
        unsafe_allow_html=True,
    )

    preset_option = st.selectbox(
        "Load Preset Corpus or Enter Custom Text:",
        [
            "Custom Input (Type single words, short phrases, or full dialogues below)",
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
        "Corpus Input Stream (Format: Speaker: Line OR Single Words):",
        value=default_corpus,
        height=180,
    )

    if st.button("⚡ Execute Universal Vector X-Ray"):
        with st.spinner("Processing token normalization, sentiment/lexicon check, and vector mapping..."):
            time.sleep(0.4)

        raw_lines = [l.strip() for l in user_corpus_input.split("\n") if l.strip()]
        
        if not raw_lines:
            st.warning("Corpus is empty. Please enter text.")
        else:
            cleaned_texts = []
            speakers = []
            for idx, line in enumerate(raw_lines):
                parts = line.split(":", 1)
                if len(parts) == 2:
                    speakers.append(parts[0].strip())
                    cleaned_texts.append(parts[1].strip().lstrip("-").strip())
                else:
                    speakers.append(f"Actor {idx + 1}")
                    cleaned_texts.append(line.strip().lstrip("-").strip())

            try:
                vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b\w+\b')
                tfidf_matrix = vectorizer.fit_transform(cleaned_texts)
            except Exception:
                tfidf_matrix = None

            absolute_lexicon = {
                "hamı", "heç", "həmişə", "hər", "everyone", "always", 
                "never", "all", "nobody", "hiç", "because", "heç vaxt", 
                "heç kim", "hiçbir", "Hiç", "nothing", "hiç kimse"
            }

            calm_lexicon = {
                "calm", "sakit", "rahat", "fine", "ok", "okay", "hə", 
                "baş üstə", "peace", "sus", "yes", "bilmirəm", "neyse"
            }
            
            results = []
            total_tension = 0
            speaker_last_word_count = {}

            for i in range(len(raw_lines)):
                orig_line = raw_lines[i]
                curr_speaker = speakers[i]
                clean_text = cleaned_texts[i]
                words = clean_text.split()
                word_count = len(words) if words else 1

                has_q = 1 if "?" in clean_text or "?" in orig_line else 0
                has_ell = 1 if "..." in clean_text or "…" in clean_text else 0

                lex_matches = sum(1 for w in words if w.lower() in absolute_lexicon)
                lex_density = lex_matches / word_count

                is_calm_utterance = any(w.lower() in calm_lexicon for w in words) and word_count <= 3

                if curr_speaker in speaker_last_word_count and speaker_last_word_count[curr_speaker] > 0:
                    prev_count = speaker_last_word_count[curr_speaker]
                    compression_ratio = max(0.0, (prev_count - word_count) / prev_count)
                else:
                    compression_ratio = 0.1
                speaker_last_word_count[curr_speaker] = word_count

                evasion_score = 0.0
                if i > 0 and tfidf_matrix is not None:
                    try:
                        sim = cosine_similarity(tfidf_matrix[i-1:i], tfidf_matrix[i:i+1])[0][0]
                        evasion_score = float(1.0 - sim)
                    except Exception:
                        evasion_score = 0.2

                if is_calm_utterance and i == 0:
                    beat_tension = 12
                    emo = "Neytral / Sakitləndirici İfadə"
                    def_mech = "Emosional Sabitləşmə"
                    c_class = "terminal-box"
                else:
                    raw_score = 15.0 + (evasion_score * w_evasion * 1.2) + (compression_ratio * w_compression) + (lex_density * w_lexical * 15) + (has_q * w_punctuation * 0.8) + (has_ell * w_punctuation * 1.2)
                    beat_tension = int(min(100, max(10, raw_score)))

                    if is_calm_utterance:
                        beat_tension = int(min(beat_tension, 25))
                        emo = "Neytral / Sakitləndirici Mübadilə"
                        def_mech = "Sabitləşmə"
                        c_class = "terminal-box"
                    elif evasion_score > 0.7 or "fuck" in clean_text.lower() or "off" in clean_text.lower():
                        emo = "Aqressiv Reaksiya / Semantik Qırılma"
                        def_mech = "Konfrontativ Yayınma / Müdafiə"
                        c_class = "warning-terminal"
                    elif lex_density > 0.1 or has_ell:
                        emo = "Ontoloji Qapanma / Simvolik Void"
                        def_mech = "Defensiv Çəkilmə / Bad Faith"
                        c_class = "lab-card"
                    else:
                        emo = "Dinamik İnteraksiya / Gərgin Mübadilə"
                        def_mech = "Açıq Ekspozisiya"
                        c_class = "terminal-box"

                total_tension += beat_tension

                results.append({
                    "beat": i + 1,
                    "speaker": curr_speaker,
                    "line": orig_line,
                    "tension": beat_tension,
                    "emo": emo,
                    "def_mech": def_mech,
                    "class": c_class,
                    "metrics": f"Evasion: {evasion_score:.2f} | Intra-Compression: {compression_ratio:.2f} | Lexical Density: {lex_density:.2f}"
                })

            st.markdown("---")
            st.markdown(f"### 🔬 Universal Diagnostic Results ({len(results)} Beats Processed)")

            for r in results:
                safe_line = html.escape(r['line'])
                safe_speaker = html.escape(r['speaker'])
                
                card_html = (
                    f"<div class='{r['class']}'>"
                    f"<b>Beat {r['beat']} ({safe_speaker})</b><br>"
                    f"<i style='color: #58a6ff; font-size: 15px;'>\"{safe_line}\"</i><br><br>"
                    f"⚡ <b>Interpretive Indicator:</b> {r['emo']}<br>"
                    f"🛡️ <b>Structural Vector:</b> {r['def_mech']}<br>"
                    f"📊 <b>Heuristic Tension Index:</b> {r['tension']}%<br>"
                    f"💬 <b style='color: #7ee787;'>Vector Audit Metrics:</b> <i>{r['metrics']}</i>"
                    f"</div>"
                )
                st.markdown(card_html, unsafe_allow_html=True)

            avg_tension = int(total_tension / len(results)) if results else 0
            st.markdown("---")
            st.metric(label="Overall Corpus Heuristic Tension Index", value=f"{avg_tension}%")

# ==========================================
# 6. MODULE 3: RULE-BASED BRANCHING DEMONSTRATOR
# ==========================================
elif selected_module == "🔄 Rule-Based Branching Demonstrator":
    st.markdown("### 🔄 Rule-Based Branching Demonstrator")
    st.markdown(
        "<p style='color: #8b949e;'>Demonstrates heuristic conversational trajectories based on input triggers.</p>",
        unsafe_allow_html=True,
    )

    intervention_input = st.text_input(
        "Enter Custom Character Intervention Vector:",
        value="Zahra demands the key to the locked room.",
    )

    if st.button("Simulate Heuristic Trajectories"):
        with st.spinner("Calculating conversational physics..."):
            time.sleep(0.4)

        aggressive_keywords = ["qışqır", "sındır", "demand", "shatter", "vur", "qırıntı", "fuck", "off"]
        is_aggressive = any(kw in intervention_input.lower() for kw in aggressive_keywords)
        peak_b2 = 100 if is_aggressive else 92

        st.markdown("---")
        st.markdown("### 🌿 Simulated Branching Trajectories")

        col_b1, col_b2, col_b3 = st.columns(3)

        with col_b1:
            st.markdown(
                "<div class='warning-terminal'>"
                "<b>Branch A: Evasion / Closure</b><br>"
                "<i style='font-size: 13px; color: #ff7b72;'>Respondent turns away, enforcing silence.</i><br><br>"
                "📉 <b>Tension Curve:</b> Drops to 45% via forced shutdown.<br>"
                "🛡️ <b>Wall Status:</b> <span style='color: #f85149;'>REINFORCED</span>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col_b2:
            st.markdown(
                "<div class='warning-terminal' style='background-color: #491002; border-color: #bd2c00; border-left-color: #f0883e;'>"
                "<b>Branch B: Confrontation / Apex</b><br>"
                "<i style='font-size: 13px; color: #ffa657;'>Respondent challenges the barrier.</i><br><br>"
                f"📈 <b>Tension Curve:</b> Spikes to {peak_b2}% (Apex).<br>"
                "🛡️ <b>Wall Status:</b> <span style='color: #f0883e;'>STRAINED</span>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col_b3:
            st.markdown(
                "<div class='terminal-box'>"
                "<b>Branch C: Softening / Catharsis</b><br>"
                "<i style='font-size: 13px; color: #7ee787;'>Respondent yields, offering emotional decay.</i><br><br>"
                "📉 <b>Tension Curve:</b> Decays to 20% (Resolution).<br>"
                "🛡️ <b>Wall Status:</b> <span style='color: #3fb950;'>DISSOLVED</span>"
                "</div>",
                unsafe_allow_html=True,
            )

        st.markdown("#### 📈 Dynamic Multi-Branch Tension Trajectory Curve")
        branch_chart_data = pd.DataFrame(
            {
                "Branch A (Evasion)": [40, 55, 70, 60, 45],
                "Branch B (Confrontation)": [40, 60, 80, 95, peak_b2],
                "Branch C (Catharsis)": [40, 50, 65, 40, 20],
            },
            index=["Beat 1", "Beat 2", "Beat 3", "Climax", "Resolution"],
        )
        st.line_chart(branch_chart_data)

# ==========================================
# 7. MODULE 4: DYNAMIC THEORETICAL MARKER INDEX
# ==========================================
elif selected_module == "⚛️ Dynamic Theoretical Marker Index":
    st.markdown("### ⚛️ Dynamic Theoretical Marker Index")
    st.markdown(
        "<p style='color: #8b949e;'>Operationalized philosophical constructs computed dynamically from active corpus text.</p>",
        unsafe_allow_html=True,
    )

    active_text_sample = user_corpus_input.lower() if 'user_corpus_input' in locals() and user_corpus_input else ""
    if not active_text_sample:
        active_text_sample = (
            "zahra: - did ilhama ever love me? why are you asking? "
            "because i don't remember her voice, father. she was your mother. a person loves their own blood. "
            "she loved no one... everyone in this house opened that door themselves."
        ).lower()

    bad_faith_score = min(98, int(30 + (active_text_sample.count("hamı") + active_text_sample.count("everyone") + active_text_sample.count("blood") + active_text_sample.count("because")) * 12))
    lacanian_score = min(98, int(40 + (active_text_sample.count("remember") + active_text_sample.count("voice") + active_text_sample.count("?") + active_text_sample.count("admit")) * 10))
    panopticon_score = min(98, int(35 + (active_text_sample.count("door") + active_text_sample.count("house") + active_text_sample.count("desk")) * 18))

    c1, c2, c3 = st.columns(3)
    c1.markdown(
        f"<div class='lab-card'>"
        f"<b>1. Sartrean Bad Faith (Marker Index)</b><br>Score: {bad_faith_score}%<br>"
        f"<p style='font-size:12px; color:#8b949e; margin-top:5px;'>Operationalized via generalization shielding density.</p>"
        f"</div>",
        unsafe_allow_html=True,
    )
    c2.markdown(
        f"<div class='lab-card'>"
        f"<b>2. Lacanian Lack (Marker Index)</b><br>Score: {lacanian_score}%<br>"
        f"<p style='font-size:12px; color:#8b949e; margin-top:5px;'>Operationalized via interrogative & memory void markers.</p>"
        f"</div>",
        unsafe_allow_html=True,
    )
    c3.markdown(
        f"<div class='lab-card'>"
        f"<b>3. Foucauldian Panopticism (Marker Index)</b><br>Score: {panopticon_score}%<br>"
        f"<p style='font-size:12px; color:#8b949e; margin-top:5px;'>Operationalized via spatial boundary references.</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

# ==========================================
# 8. MODULE 5: VALIDATION PROTOCOL & EMPIRICAL DESIGN
# ==========================================
elif selected_module == "📊 Validation Protocol & Empirical Design":
    st.markdown("### 📊 Validation Protocol & Empirical Design (Results Pending)")
    st.markdown(
        "<p style='color: #8b949e;'>To maintain rigorous academic integrity, speculative numbers have been removed. The framework below outlines the active Human Annotation & Inter-Rater Reliability study design.</p>",
        unsafe_allow_html=True,
    )

    st.markdown("#### 📐 Proposed Human Annotation Study Protocol")
    st.markdown(
        "<div class='context-box'>"
        "<b>Study Design Parameters:</b><br>"
        "• <b>Dataset Scope:</b> 100–200 dialogue corpuses across diverse genres.<br>"
        "• <b>Independent Annotators:</b> 3–5 trained human experts (psychology and dramaturg students).<br>"
        "• <b>Blind Evaluation:</b> Annotators evaluate emotional tension, evasion, and withdrawal on a 1–5 scale without exposure to automated engine outputs.<br>"
        "• <b>Statistical Metrics:</b> Inter-rater agreement measured via <b>Krippendorff's Alpha</b> / <b>Intraclass Correlation Coefficient (ICC)</b>, and model-human agreement evaluated via <b>Spearman Rank Correlation</b> and <b>Mean Absolute Error (MAE)</b>."
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("#### 🧩 Ablation Study Framework (Pending Execution)")
    ablation_table = """
    <table class="cyber-table">
        <thead>
            <tr>
                <th>Configuration</th>
                <th>Active Components</th>
                <th>Status</th>
                <th>Target Metric</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><b>Model A</b></td>
                <td>Evasion Only</td>
                <td style="color: #f0883e;">Pending Empirical Deployment</td>
                <td>Spearman ρ & MAE</td>
            </tr>
            <tr>
                <td><b>Model B</b></td>
                <td>Evasion + Intra-Compression</td>
                <td style="color: #f0883e;">Pending Empirical Deployment</td>
                <td>Spearman ρ & MAE</td>
            </tr>
            <tr>
                <td><b>Model C</b></td>
                <td>Evasion + Compression + Lexical Shielding</td>
                <td style="color: #f0883e;">Pending Empirical Deployment</td>
                <td>Spearman ρ & MAE</td>
            </tr>
            <tr>
                <td><b>Model D (Full)</b></td>
                <td>All Components (Evasion + Compression + Lexical + Punctuation)</td>
                <td style="color: #f0883e;">Pending Empirical Deployment</td>
                <td>Spearman ρ & MAE</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(ablation_table, unsafe_allow_html=True)

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
    st.markdown("### ⚠️ Methodological Limitations & External Validity")
    st.markdown(
        "<div class='lab-card' style='border-left-color: #f85149;'>"
        "<b>Known Constraints & Epistemological Boundaries:</b><br>"
        "1. <i>Corpus Dependency:</i> TF-IDF vector matrix computations require multi-turn discursive inputs.<br>"
        "2. <i>Pragmatic Boundaries:</i> Bag-of-words tokenization maps topical divergence but requires attention-based transformers for sarcastic or ironic inversion.<br>"
        "3. <i>Interpretive Indicative Status:</i> Outputs are heuristic interpretive markers, not definitive psychological diagnoses.<br>"
        "4. <i>Hyper-Parameter Sensitivity:</i> Manual slider weight adjustments alter absolute scoring bounds, necessitating standardized benchmark normalization."
        "</div>",
        unsafe_allow_html=True,
    )

# ==========================================
# 10. FOOTER
# ==========================================
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #8b949e; font-size: 11px;'>ONTOLOGICAL SILENCE & PARANOIA ENGINE // INDEPENDENT RESEARCH PROTOTYPE BY AGIL CHIRAGLI</p>",
    unsafe_allow_html=True,
)
