# JU3-PolicyPal-AI
GEN AI

📘 PolicyPal AI – Insurance Policy Summarizer and Checker
🧠 Idea Summary
An AI assistant that takes insurance policy documents (health/life/car) and:

🔍 Summarizes the policy (coverage, conditions, exclusions)

✅ Checks for missing clauses (based on standard benchmarks)

📊 Highlights risky or unclear terms

🗂️ Outputs a structured summary table + editable doc

⚙️ Key Features
Upload PDF/Word file

Auto-extract content using AI

Detect key policy sections:

Sum insured

Waiting period

Pre-existing disease coverage

Exclusions

Show:

Summary (natural language)

Tabular extracted facts

Warnings (e.g., “No coverage for pre-existing diseases”)

🔧 Stack
Component	Tool
UI	Streamlit
File Parsing	PyMuPDF / PyPDF2 / python-docx
LLM (local)	Ollama (TinyLLaMA / LLaMA 3)
Optional cloud	Azure OpenAI / Claude / GPT-4
Output	JSON + .docx summary

📦 Output
sql
Copy
Edit
PolicyPal Summary:
--------------------
✅ Covered: Hospitalization, Day-care
❌ Not Covered: Pre-existing diseases, Dental
📄 Summary Table:
| Feature              | Value                    |
|----------------------|--------------------------|
| Sum Insured          | ₹5,00,000                |
| Waiting Period       | 2 Years                  |
| Critical Illness     | Not Mentioned            |
| Exclusions Mentioned | Yes                      |

# 📘 PolicyPal AI – Insurance Policy Summarizer and Checker

PolicyPal AI helps users understand their insurance policies by summarizing uploaded PDFs and extracting key clauses like sum insured, waiting period, exclusions, etc.

## 🚀 Features

- Upload policy documents in PDF
- AI summarizes coverage, exclusions, conditions
- Warns about missing clauses
- Outputs structured summary with highlights

## 🛠️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yourusername/policypal-ai.git
cd policypal-ai
Install dependencies:

pip install -r requirements.txt
Pull the LLaMA model using Ollama:

ollama pull llama3
Run the Streamlit app:

streamlit run app.py
