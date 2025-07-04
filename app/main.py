import os
import sys

# Ensure agents and utils directories are on path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from openai import OpenAI
from agents.doc_reader import run as run_doc_reader
from agents.workflow_parser import run as run_workflow_parser
from agents.automation_finder import run as run_automation_finder
from agents.checklist_builder import run as run_checklist_builder
from agents.summary_generator import run as run_summary_generator

st.set_page_config(page_title="BizOps AI Agent", layout="centered")
st.title("BizOps AI Agent  Business Document Intelligence")

uploaded_file = st.file_uploader("Upload your business document (TXT PDF DOC):", type=["txt"])
if uploaded_file is not None:
    input_text = uploaded_file.read().decode("utf-8")

    st.subheader("1. Raw Input")
    st.text_area("Content", input_text, height=200)

    if st.button("Analyze Document"):
        with st.spinner("Running agents..."):
            doc_result = run_doc_reader(input_text)
            workflow = run_workflow_parser(input_text)
            automation = run_automation_finder(input_text)
            checklist = run_checklist_builder(input_text)
            summary = run_summary_generator(input_text)

        st.success("Analysis complete!")

        st.subheader("2. Document Understanding")
        st.write(doc_result)

        st.subheader("3. Workflow Extracted")
        st.write(workflow)

        st.subheader("4. Suggested Automations")
        st.write(automation)

        st.subheader("5. Operational Checklist")
        st.write(checklist)

        st.subheader("6. Summary")
        st.write(summary)