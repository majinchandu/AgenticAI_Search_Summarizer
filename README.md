Agentic AI Assistant
Overview
Agentic AI Assistant is a Python-based application designed to perform in-depth research on user-specified topics. It leverages an intelligent AI agent powered by Google's Gemini model to orchestrate a workflow using tools for web searching, text summarization, PDF generation, and memory management. The project offers two interfaces: a command-line interface (CLI) via main.py and a web-based interface built with Streamlit via app.py.
The AI agent dynamically decides which tools to use based on the task's progress, ensuring a feedback loop that refines the output until the task is complete. The system saves summaries to memory and generates PDF reports for easy sharing.
Features

Web Search: Fetches relevant information from the web using the SerpAPI.
Text Summarization: Condenses information into concise summaries using the Gemini 1.5 Flash model.
PDF Generation: Saves summaries as formatted PDF reports.
Memory Management: Stores topic summaries with timestamps for historical reference.
Dynamic Tool Planning: The AI agent decides the next steps using a feedback loop.
Dual Interfaces:
CLI for terminal-based interaction (main.py).
Streamlit UI for a user-friendly web experience (app.py).



Project Structure
├── app.py                # Streamlit web interface
├── main.py               # Command-line interface
├── memory_manager.py     # Handles memory storage and retrieval
├── pdf_writer.py         # Generates PDF reports
├── search_tool.py        # Performs web searches using SerpAPI
├── memory.json           # Stores historical summaries (generated at runtime)
├── .env                  # Environment variables (not included in repo)
└── README.md             # Project documentation

Installation
Prerequisites

Python 3.8 or higher
A Google Gemini API key (for summarization)
A SerpAPI key (for web search)

Steps

Clone the Repository
git clone https://github.com/majinchandu/AgenticAI_Search_Summarizer
cd agentic-ai-assistant


Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies
pip install streamlit google-generativeai python-dotenv reportlab requests


Configure Environment Variables
Create a .env file in the project root and add your API keys:
GEMINI_API_KEY=your_gemini_api_key
SERPAPI_API_KEY=your_serpapi_api_key


Run the Application

For the CLI:
python main.py


For the Streamlit UI:
streamlit run app.py





Usage
Command-Line Interface (main.py)

Run python main.py.
Enter a topic when prompted (e.g., "Machine Learning Trends").
The agent will:
Plan the workflow (e.g., search, summarize, save to PDF).
Execute tools and display observations.
Save the final summary to memory.json and generate a PDF if applicable.



Streamlit Interface (app.py)

Run streamlit run app.py.
Open the provided URL in your browser (typically http://localhost:8501).
Enter a topic in the text input field (e.g., "Quantum Computing").
Click "Run Agent" to start the process.
View real-time updates, including tool actions, observations, and the final summary.
A PDF report is saved, and the summary is stored in memory.json.

Tools

Search: Queries the web using SerpAPI and returns formatted results.
Summarize: Uses the Gemini model to generate concise summaries.
PDF: Saves summaries as PDF reports using ReportLab.
Memory: Displays or saves topic summaries with timestamps.

Example Workflow
For the topic "Artificial Intelligence Ethics":

The agent runs a web search to gather data.
It summarizes the search results into a concise text.
The summary is saved as a PDF (gemini_summary.pdf).
The summary is stored in memory.json with a timestamp.

Memory Management
Summaries are saved in memory.json with the format:
[
  {
    "topic": "Artificial Intelligence Ethics",
    "summary": "Summary text here...",
    "timestamp": "2025-06-24 12:03:00"
  }
]

Use the memory tool to view past topics and their summaries.
PDF Reports

Generated PDFs include a title (e.g., "Summary Report: Artificial Intelligence Ethics") and the summary text.
Files are saved as gemini_summary.pdf in the project root.

Limitations

Requires stable internet for web searches and API calls.
API keys must be valid and have sufficient quota.
PDF generation is basic and may not handle complex formatting.
Memory is stored locally in memory.json without persistence across environments.

Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Powered by Google Gemini for summarization.
Uses SerpAPI for web search.
Built with Streamlit for the web interface.
PDF generation by ReportLab.

Contact
For issues or questions, please open an issue on the GitHub repository or contact the maintainer at your-email@example.com.