import streamlit as st
from search_tool import search_web
from pdf_writer import save_summary_to_pdf
from memory_manager import save_to_memory, print_memory
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Format list results from search into clean string
def search_as_text(query):
    results = search_web(query)
    return "\n".join([f"- {r}" for r in results])

# Tool Registry
TOOLS = {
    "search": search_as_text,
    "summarize": lambda text: model.generate_content(f"Summarize this:\n\n{text}").text,
    "pdf": save_summary_to_pdf,
    "memory": print_memory,
}

def feedback_loop_agent_streamlit(topic):
    st.session_state["logs"] = []
    current_data = topic
    steps = []
    done = False

    final_summary = ""

    while not done:
        planning_prompt = f"""
You are an intelligent AI agent. Your current goal is:

"{topic}"

So far, you have these observations:
{steps}

Available tools: search, summarize, pdf, memory, done

Based on current state, what should be the next step?
Respond with only the tool name you want to run next.
If the task is complete, respond with: done
"""
        plan = model.generate_content(planning_prompt).text.strip().lower()
        plan = plan.replace("`", "").replace("'", "").replace('"', '').strip()

        if plan == "done":
            st.success(" Task completed.")
            done = True
            continue

        if plan not in TOOLS:
            st.error(f" Invalid Tool: {plan}")
            break

        st.info(f" Thought: I should now use the `{plan}` tool.")

        tool = TOOLS[plan]
        if plan == "pdf":
            tool(current_data, topic)
            observation = f" PDF saved for topic: {topic}"
        elif plan == "memory":
            observation = tool("")
        else:
            current_data = tool(current_data)
            observation = current_data[:500] + "..." if isinstance(current_data, str) else "[⚠️] Non-text output"
            if plan == "summarize":
                final_summary = current_data

        steps.append(f"Tool used: {plan}\nObservation: {observation}")
        st.code(observation)

    if "summarize" in [s.lower() for s in steps[-2:]]:
        save_to_memory(topic, current_data)
        st.success(" Memory updated with final summary.")

    if final_summary:
        st.subheader(" Final Summary")
        st.write(final_summary)

# Streamlit UI
st.set_page_config(page_title="Agentic AI Assistant", layout="centered")
st.title(" Agentic AI: Knowledge Assistant")

query = st.text_input(" Topic batao jiska deep kaam chahiye:", "")
if st.button(" Run Agent") and query:
    feedback_loop_agent_streamlit(query)
