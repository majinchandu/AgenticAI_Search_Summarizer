# Knowledge Ranger – Web Agentic Summarizer

A Streamlit-powered AI research assistant that searches the web, summarizes topics using Google Gemini, and saves structured reports as PDFs. The app also maintains a searchable memory of past summaries.

## Features

- 🔍 Web search using SerpAPI
- 🧠 Summarization with Google Gemini (Generative AI)
- 📄 PDF report generation
- 🗂️ Persistent memory/history of topics and summaries
- Simple Streamlit web UI and CLI agent mode

## Project Structure

```
.
├── app.py                # Streamlit web app
├── main.py               # CLI agent with tool planning
├── search_tool.py        # Web search utility (SerpAPI)
├── pdf_writer.py         # PDF generation utility
├── memory_manager.py     # Persistent memory management
├── memory.json           # Stores past summaries
├── gemini_summary.pdf    # Latest generated PDF
├── .env                  # API keys (should NOT be committed)
├── .gitignore            # Ignores venv, .env, __pycache__, etc.
└── __pycache__/          # Python bytecode cache
```

## Setup

1. **Clone the repository**

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up API keys**

   Create a `.env` file (see below) with your [Google Gemini API key](https://ai.google.dev/) and [SerpAPI key](https://serpapi.com/):

   ```
   GEMINI_API_KEY=your_gemini_api_key
   SERPAPI_API_KEY=your_serpapi_key
   ```

4. **Run the Streamlit app**
   ```sh
   streamlit run app.py
   ```

5. **Or use the CLI agent**
   ```sh
   python main.py
   ```

## Usage

- **Web UI:** Enter a topic, click "Generate Summary", download the PDF, and view past summaries.
- **CLI:** Enter a topic when prompted; the agent will search, summarize, save PDF, and update memory.

## Security

- **Do NOT commit your `.env` or `venv/` directory.**  
  If you have, remove them from git history and rotate your API keys.

## License

MIT License