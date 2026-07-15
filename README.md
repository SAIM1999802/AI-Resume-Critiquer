# 📃 AI Resume Critiquer

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-8E75C2?style=flat&logo=google-gemini&logoColor=white)](https://ai.google.dev/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=chainlink&logoColor=white)](https://github.com/langchain-ai/langchain)
[![uv](https://img.shields.io/badge/uv-Package_Manager-DE5C2C?style=flat&logo=astral&logoColor=white)](https://github.com/astral-sh/uv)

An intelligent, Streamlit-based web application designed to perform exhaustive, recruiter-level audits of professional CVs. By parsing PDFs (retaining complex column structures) and text files, this tool leverages **LangChain** to orchestrate seamless prompts and **Google's Gemini 2.5 Flash** to deliver brutal, line-by-line feedback, rewrite weak resume bullets, and highlight ATS keyword gaps. 

The project is fully optimized for speed and modern Python packaging using **Astral's `uv` package manager**.

---

## ⚠️ CRITICAL WARNINGS

> 🔑 **API Key Required:** This application **does not** include a built-in API key. To use this project, you must generate your own personal **Google AI Studio API key** and add it to your environment.
>
> 🤖 **Model Integration:** This project explicitly uses **Google Gemini** via the `langchain-google-genai` package. It will not work with OpenAI, Anthropic, or other API keys without altering the core model initialization code.

---

## 🚀 Key Features

* **Advanced Layout Extraction:** Powered by `pdfplumber` to accurately read complex, multi-column resume layouts without overlapping text lines.
* **LangChain Orchestration:** Utilizes **LangChain Core** and `SystemMessage`/`HumanMessage` paradigms to ensure structured, precise, and robust LLM prompting.
* **Lightning-Fast with `uv`:** Built and optimized using the modern, Rust-powered **`uv` package manager** for instant dependency resolution and environment setup.
* **Brutally Honest AI Recruiter:** Acts as an elite HR Director, analyzing your resume using real-world recruitment standards.
* **Actionable Bullet Rewrites:** Automatically rewrites weak experience and project descriptions using Google's **X-Y-Z formula** (*Accomplished [X] as measured by [Y], by doing [Z]*).
* **ATS Keyword Matcher:** Highlights exactly which target keywords and technology stacks are missing for your desired job role.

---

## 🛠️ Tech Stack

* **Frontend UI:** [Streamlit](https://streamlit.io/)
* **PDF Engine:** [pdfplumber](https://github.com/jsvine/pdfplumber)
* **AI Orchestration & LLM Framework:** [LangChain](https://github.com/langchain-ai/langchain)
* **LLM Engine:** [Google Gemini 2.5 Flash](https://ai.google.dev/gemini-api)
* **Package Manager & Virtual Env:** [uv (by Astral)](https://github.com/astral-sh/uv)

---

## 📦 Installation & Local Setup

Get your local development server running in just a few steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/ai-resume-critiquer.git](https://github.com/your-username/ai-resume-critiquer.git)
cd ai-resume-critiquer
