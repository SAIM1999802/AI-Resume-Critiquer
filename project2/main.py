import os
import io
import streamlit as st
import pypdf as pdfReader
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
import pdfplumber

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7,
    max_tokens=3000,
)

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")
st.title("AI Resume Critiquer")
st.markdown("Upload your Resume")

up_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you are targeting (Optional)")

analyze = st.button("Analyze Resume")

# def extract_txt_from_pdf(pdf_file): 
    # pdf_reader = pdfReader.PdfReader(pdf_file)
    # text = ""
    # for page in pdf_reader.pages:
        # extracted = page.extract_text()
        # if extracted:
            # text += extracted + "\n"
    # return text

def extract_txt_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text(layout=True) # layout=True preserves columns!
            if extracted:
                text += extracted + "\n"
    return text

def ext_txt_from_file(up_file):
    if up_file.type == "application/pdf":
        return extract_txt_from_pdf(up_file)
    return up_file.getvalue().decode("utf-8")

if analyze and up_file:
    try:
        file_content = ext_txt_from_file(up_file)

        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()

        prompt = f"""You are reviewing the resume of an applicant targeting the following role: {job_role if job_role else 'General Software Engineering / Web Developent Role'}.
        Please conduct an exhaustive, granular review of the following resume data. Do not summarize or give brief overviews. Walk through each section thoroughly.
        Resume content to analyze:
        {file_content}

        Provide your breakdown exactly using the following structural template:
        ## 1. Executive Summary & First Impressions
        - Critique the overall layout structure, tone, and profile summary.
        - Is the career objective or professional summary compelling? How can it be reworded?
        
        ## 2. In-Depth Section-by-Section Breakdown
        - **Contact Info & Links:** Check for professionalism and missing links (GitHub/LinkedIn).
        - **Experience/Projects:** Go line-by-line through their experience or projects. Point out exactly which bullet points are weak and provide rewritten, high-impact versions using the X-Y-Z formula (Accomplished [X] as measured by [Y], by doing [Z]).
        - **Technical Skills:** Are the skills grouped logically? What trending tech stacks for the target role are missing?
        - **Education & Certifications:** Review formatting and relevance.
        
        ## 3. Targeted Optimization for: '{job_role if job_role else "General Application"}'
        - Map the resume against industry standards for this exact role.
        - Identify critical keyword gaps that might cause the resume to fail an ATS (Applicant Tracking System).
        
        ## 4. Red-Pen Corrections (The Action Plan)
        - Provide a bulleted checklist of exact changes the candidate needs to make immediately.
        - Suggest layout or formatting changes to improve structural readability."""   

        messages = [
           SystemMessage(content=(
                "You are an elite, highly critical HR Director and Technical Recruiter with decades of experience. "
                "Your job is to provide brutal, comprehensive, line-by-line resume critiques. "
                "Do not use generic conversational filler or placeholder names like 'Alex'. Address the user's uploaded text content directly. "
                "Be incredibly detailed, exhaustive, and actionable in your feedback."
            )),
            HumanMessage(content=prompt)
        ]

        with st.spinner("Analyzing your resume..."):
            response = llm.invoke(messages)

        st.markdown("### Analysis Results")
        st.markdown(response.content)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
