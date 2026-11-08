import streamlit as st
import re

# Page Configuration (Noir / Dark Minimalist Theme)
st.set_page_config(
    page_title="Narrative Tech | Silence & Paranoia Index",
    page_icon="🎭",
    layout="wide"
)

# Custom CSS Styles
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    .stButton>button {
        background-color: #2b2b36;
        color: #ffffff;
        border-radius: 6px;
        border: 1px solid #4a4a5a;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #3b3b4f;
        border-color: #8888a0;
    }
    </style>
""", unsafe_allow_html=True)

# Title & Academic/Contextual Header
st.title("🎭 Narrative Tech: Silence & Paranoia Index")
st.caption("Computational Dramaturgy & Psychological Analysis Engine | Based on the original drama 'İlhəmə və Pərvaz'")

st.markdown("""
> **Project Context:** This interactive prototype bridges humanities and computational media, analyzing 
> psychological suppression, structural silence, and memory reconstruction from Agil Chiragli’s narrative framework.
""")

st.divider()

# Tabs for Interactive Experience
tab1, tab2 = st.tabs(["📖 Scene Context & Narrative", "📊 Silence & Paranoia Engine"])

# Selected Key Scene translated to English for international presentation
SAMPLE_TEXT = """— Did Ilhame ever love me?
— Why are you asking?
— Because I don't know. I don't remember her voice, father. I don't even remember her face.
— She was your mother. A person loves their own blood. This isn't something to be asked, Zehra.
— That is not an answer. You aren't telling me how she loved. You are just giving me the sentence you need to survive.
— She loved no one... Everyone in this house opened that door themselves one day. But no one remembered how they walked through it."""

with tab1:
    st.subheader("Core Narrative Scene: The Kitchen Silence")
    st.write("A critical confrontation between young Zehra and her father, Parviz, highlighting institutionalized silence.")
    st.text_area("Script Excerpt", SAMPLE_TEXT, height=200, disabled=True)
    
    st.info("💡 This scene reflects invisible domestic walls, inherited trauma, and the heavy burden of unspoken truths.")

with tab2:
    st.subheader("Computational Text Analysis (NLP / Sentiment & Tension Engine)")
    
    input_text = st.text_area("Input dialogue or text for psychological tension analysis:", SAMPLE_TEXT, height=180)
    
    if st.button("Calculate Indices"):
        words = input_text.split()
        word_count = len(words)
        
        # English keywords corresponding to the psychological weight of the story
        silence_keywords = ["silence", "silent", "know", "voice", "remember", "door", "shadow", "cold", "answer"]
        paranoia_keywords = ["love", "loved", "lie", "fear", "anyone", "sin", "truth", "horror", "blood"]
        
        silence_count = sum(1 for w in words if any(k in w.lower() for k in silence_keywords))
        paranoia_count = sum(1 for w in words if any(k in w.lower() for k in paranoia_keywords))
        
        # Algorithmic Index Calculation
        silence_index = min(100, int((silence_count / max(1, word_count)) * 300 + (input_text.count("...") * 15)))
        paranoia_index = min(100, int((paranoia_count / max(1, word_count)) * 400 + (input_text.count("?") * 10)))
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(label="📊 Total Word Count", value=word_count)
        with col2:
            st.metric(label="🤐 Silence Index", value=f"{silence_index}%")
        with col3:
            st.metric(label="⚡ Psychological Tension", value=f"{paranoia_index}%")
            
        st.divider()
        st.subheader("Psychological Diagnostics & Evaluation")
        
        if silence_index > 40:
            st.warning("⚠️ **High Silence Pressure:** The text exhibits dominant emotional withdrawal and unresolved questioning.")
        else:
            st.success("✅ **Open Dialogue Level:** Silence barriers are maintained at standard levels.")
            
        if paranoia_index > 30:
            st.error("🚨 **Critical Tension Detected:** High presence of defensive mechanisms, distrust, and hidden accusations.")
        else:
            st.info("ℹ️ **Stable Emotional Tone:** Tension parameters remain within baseline thresholds.")
