import streamlit as st
import streamlit.components.v1 as components
from ats_checker import check_ats_compliance
from resume_parser import extract_resume_text
from roadmap_generator import generate_roadmap, evaluate_resume

st.set_page_config(page_title="📄 AI-Resume Analyzer ", layout="centered")
st.title("📄AI-Resume Analyzer using LLM")

st.markdown("Upload your resume file (**PDF** or **DOCX**) and enter your desired job role to get a detailed AI-powered evaluation:")

# Upload resume
uploaded_file = st.file_uploader("📤 Upload Resume", type=["pdf", "docx"])

# Text input for target role (replaces dropdown)
target_role = st.text_input("🎯 Target Job Role", placeholder="e.g. Data Scientist, Backend Engineer")

# Output language selector
language = st.selectbox("🌐 Output Language", ["English", "Hindi", "French"])

# Evaluate button
if st.button("🔍 Evaluate Resume"):
    if uploaded_file is None or not target_role:
        st.error("⚠️ Please upload a resume and enter your target role.")
    else:
        with st.spinner("Analyzing your resume..."):
            # Extract resume text
            resume_text = extract_resume_text(uploaded_file)

            # Evaluate using LLM
            feedback = evaluate_resume(resume_text, tone=target_role, language=language)

            # Clean and display
            lines = feedback.strip().splitlines()
            score_line = next((line for line in lines if "Rating" in line or "Score" in line), None)
            summary = "\n".join(lines).strip()

            # Output block
            st.markdown("### 📋 Evaluation Summary")
            st.markdown(summary)

            ats_feedback = check_ats_compliance(resume_text, target_role)

            st.markdown("### 🤖 ATS Compatibility Check")
            st.markdown(ats_feedback)

            # Copy to clipboard button
            components.html(f"""
                <textarea id="copyText" style="display:none;">{summary}</textarea>
                <button onclick="copyText()" style="
                    background-color:#0072b1;
                    color:white;
                    padding:10px 16px;
                    font-size:14px;
                    border:none;
                    border-radius:8px;
                    cursor:pointer;
                    margin-top:10px;">
                    📋 Copy Evaluation to Clipboard
                </button>
                <script>
                    function copyText() {{
                        var textArea = document.getElementById('copyText');
                        textArea.style.display = 'block';
                        textArea.select();
                        document.execCommand('copy');
                        textArea.style.display = 'none';
                        alert('✅ Evaluation copied to clipboard!');
                    }}
                </script>
            """, height=100)

        st.caption("💡 Tip: Improve your resume based on the above feedback and re-upload for better scoring.")
