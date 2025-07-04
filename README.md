# BizOps-AI-Agent
This tool processes uploaded business documents (PDF, DOCX, TXT) and extracts key workflows, summaries, checklists, and potential automation steps using a multi-agent LLM system. It is designed to assist business analysts, operations teams, and automation consultants.
Features:
- Upload business process documents in .pdf, .docx, or .txt formats
- Automatically extracts:
  - Key tasks and workflow steps
  - High-level summaries
  - Automation opportunities
  - Operational checklists
- Uses multiple LLM agents for each task
- Simple and clean Streamlit interface

Tech Stack:
- Python
- Streamlit for user interface
- OpenAI API with fallback between GPT-4 and GPT-3.5
- LangChain agents for task decomposition and reasoning
- python-docx, PyMuPDF, and other libraries for file parsing

How to Use:
1. Clone the repository
2. Install required packages:
   pip install -r requirements.txt
3. Add your OpenAI API key in a `.env` file:
   OPENAI_API_KEY=your_api_key_here
4. Run the app:
   streamlit run app/streamlit_app.py

Notes:
- Works best with well-structured business documents
- Requires internet access for OpenAI API
- Tested on both GPT-4 and GPT-3.5 endpoints
