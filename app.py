import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

from search_tool import search_web
from pdf_writer import save_summary_to_pdf
from memory_manager import save_to_memory, load_memory

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# UI Header
st.set_page_config(page_title="Knowledge Ranger", layout="centered")
st.title("🧠 Knowledge Ranger – Web Agentic Summarizer")

# User input
topic = st.text_input("Enter a topic to summarize")

if st.button("Generate Summary"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("🔍 Searching the web..."):
            results = search_web(topic)
            combined = "\n".join(results)

        with st.spinner("🧠 Summarizing using Gemini..."):
            prompt = f"""You are a research assistant. Summarize the following web results into a deep, structured report:\n\nTopic: {topic}\n\nWeb results:\n{combined}"""
            response = model.generate_content(prompt)
            summary = response.text

        st.subheader("📘 Gemini Summary:")
        st.write(summary)

        # Save and display PDF
        save_summary_to_pdf(summary, topic)
        st.success("✅ PDF generated and saved as `gemini_summary.pdf`")

        with open("gemini_summary.pdf", "rb") as f:
            st.download_button("📄 Download PDF", f, file_name="summary_report.pdf")

        # Save to memory
        save_to_memory(topic, summary)

# Memory display
st.divider()
st.subheader("🗂️ Past Summaries")
memory = load_memory()
for entry in reversed(memory[-5:]):  # Show last 5 entries
    st.markdown(f"**{entry['timestamp']}** – {entry['topic']}")
