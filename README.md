# Agentic AI Assistant

## 🧠 Overview

**Agentic AI Assistant** is a Python-based application designed to perform in-depth research on user-specified topics.
It leverages an intelligent AI agent powered by Google's Gemini model to orchestrate a workflow using tools for:

* Web searching
* Text summarization
* PDF generation
* Memory management

The project offers two interfaces:

* A command-line interface (CLI) via `main.py`
* A web-based interface built with Streamlit via `app.py`

The AI agent dynamically decides which tools to use based on task progress, ensuring a **feedback loop** that refines output until the task is complete.

---

## Features

* **Web Search**: Fetches relevant information using [SerpAPI](https://serpapi.com).
* **Text Summarization**: Condenses content via Gemini 1.5 Flash.
* **PDF Generation**: Saves outputs as formatted PDF reports.
* **Memory Management**: Stores topic summaries with timestamps in `memory.json`.
* **Dynamic Tool Planning**: Agent decides next steps based on context.
* **Dual Interfaces**:

  * CLI with `main.py`
  * Streamlit UI with `app.py`

---

## Project Structure

```
🔹 app.py                # Streamlit web interface
🔹 main.py               # Command-line interface
🔹 memory_manager.py     # Handles memory storage and retrieval
🔹 pdf_writer.py         # Generates PDF reports
🔹 search_tool.py        # Performs web searches using SerpAPI
🔹 memory.json           # Stores historical summaries (generated at runtime)
🔹 .env                  # Environment variables (not included in repo)
🔹 README.md             # Project documentation
```

---

## Installation

###  Prerequisites

* Python 3.8 or higher
* A Google Gemini API key
* A SerpAPI key

###  Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/majinchandu/AgenticAI_Search_Summarizer
cd agentic-ai-assistant
```

#### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install streamlit google-generativeai python-dotenv reportlab requests
```

#### 4. Configure Environment Variables

Create a `.env` file in the project root and add your API keys:

```env
GEMINI_API_KEY=your_gemini_api_key
SERPAPI_API_KEY=your_serpapi_api_key
```

---

## Run the Application

### CLI:

```bash
python main.py
```

### Streamlit UI:

```bash
streamlit run app.py
```

---

## Usage

### Command-Line Interface (`main.py`)

* Run `python main.py`
* Enter a topic (e.g., `Machine Learning Trends`)
* The agent will:

  * Plan the workflow
  * Execute tools
  * Display observations
  * Save summary to `memory.json`
  * Generate PDF if applicable

---

### Streamlit Interface (`app.py`)

* Run `streamlit run app.py`
* Open the URL in your browser (`http://localhost:8501`)
* Enter a topic (e.g., `Quantum Computing`)
* Click `Run Agent`
* View real-time logs and final summary
* Output saved to PDF and memory

---

##  Tools

* **Search**: Uses SerpAPI for real-time web data
* **Summarize**: Uses Gemini for intelligent summarization
* **PDF**: Exports summary as `gemini_summary.pdf`
* **Memory**: Tracks history in `memory.json`

---

##  Example Workflow

For topic `Artificial Intelligence Ethics`:

1. Agent performs web search
2. Summarizes key content
3. Saves to `gemini_summary.pdf`
4. Logs to `memory.json`

---

##  Memory Management

Summaries are saved like:

```json
[
  {
    "topic": "Artificial Intelligence Ethics",
    "summary": "Summary text here...",
    "timestamp": "2025-06-24 12:03:00"
  }
]
```

View or reuse past summaries via the memory tool.

---

##  PDF Reports

* Title: `Summary Report: <Topic>`
* Output file: `gemini_summary.pdf`
* Location: Project root

---

##  Limitations

* Requires active internet connection
* Valid API keys and sufficient quota required
* Basic PDF formatting
* Local memory only (no cloud persistence)

---

##  Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

##  License

This project is licensed under the **MIT License**.
See the `LICENSE` file for more information.

---

##  Acknowledgments

* **Google Gemini API** – Summarization engine
* **SerpAPI** – Web search tool
* **Streamlit** – Frontend framework
* **ReportLab** – PDF generation

---

##  Contact

For issues or questions, open a GitHub issue or email:
**[chanderveersinghchauhan08@gmail.com](mailto:chanderveersinghchauhan08@gmail.com)**
