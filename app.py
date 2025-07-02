# app.py – PolicyPal AI

import streamlit as st
from PyPDF2 import PdfReader
import ollama
import re

# --- Extract Text from PDF ---
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

# --- Create Prompt for Summarization ---
def create_prompt(policy_text):
    prompt = f"""
You are a smart assistant helping users understand insurance policies. Read the below content and provide:
1. Summary of coverage
2. List of key terms (Sum insured, Waiting period, Critical illness, Exclusions)
3. Warn if any common clauses are missing
4. Output in bullet points + table format if possible

Policy:
{policy_text[:4000]}
"""
    return prompt

# --- Query Ollama Model ---
def query_llm(prompt):
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# --- Streamlit UI ---
st.set_page_config(page_title="PolicyPal AI", layout="wide")
st.title("📘 PolicyPal AI – Insurance Policy Checker")

uploaded_file = st.file_uploader("Upload Insurance Policy (PDF)", type=["pdf"])
if uploaded_file:
    with st.spinner("Extracting policy content..."):
        raw_text = extract_text_from_pdf(uploaded_file)
        st.success("✅ Text extracted successfully.")

    if st.button("🔎 Analyze Policy"):
        with st.spinner("Summarizing with LLM..."):
            prompt = create_prompt(raw_text)
            result = query_llm(prompt)
            st.markdown("### 🧾 AI-Generated Summary")
            st.markdown(result)
else:
    st.info("Please upload a policy document to get started.")
