import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
from prompts import get_prompt

load_dotenv()

# API (OpenRouter)
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Page config
st.set_page_config(page_title="Legal AI Assistant", layout="wide")

# 🔥 CUSTOM CSS (UI DESIGN)
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
h1, h2, h3 {
    text-align: center;
}
.stButton>button {
    background: linear-gradient(90deg, #4CAF50, #00c6ff);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
.stTextArea textarea {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# 🎯 HERO SECTION
st.markdown("""
# ⚖️ Legal Document Drafting Assistant
### Generate Professional Legal Documents Instantly

""")

st.markdown("---")

# 🔥 FEATURES CARDS
col1, col2, col3 = st.columns(3)

with col1:
    st.info("⚡ **Fast Generation**\n\nCreate drafts in seconds")

with col2:
    st.info("🌐 **Multi-language**\n\nHindi + English support")

with col3:
    st.info("⚖️ **Legal Format**\n\nProper structured output")

st.markdown("---")

# 🚀 INPUT SECTION
st.subheader("📝 Create Your Document")

col1, col2 = st.columns(2)

with col1:
    doc_type = st.selectbox("📄 Document Type",
                            ["Complaint", "RTI", "Legal Notice"])

    language = st.selectbox("🌐 Language",
                            ["English", "Hindi"])

with col2:
    tone = st.selectbox("⚖️ Tone",
                        ["Formal", "Aggressive", "Neutral"])

details = st.text_area("✍️ Enter Details", height=150)

# 🚀 GENERATE BUTTON
if st.button("🚀 Generate Draft"):
    if details.strip() == "":
        st.warning("Please enter details first")
    else:
        prompt = get_prompt(doc_type, details, language, tone)

        with st.spinner("Generating..."):
            response = client.chat.completions.create(
                model="openrouter/auto",
                messages=[{"role": "user", "content": prompt}]
            )

        st.success("✅ Draft Generated")

        st.text_area("📄 Output", response.choices[0].message.content, height=300)

st.markdown("---")

# 👨‍💻 FOOTER
st.markdown("""
---
### 👨‍💻 Created By  
**Gautam Akshit** 

**Bilaspur, Himachal Pradesh** 
📞 8219717095  
📧 gautamakshit1234@gmail.com  
""")

