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

# Tools
def search_as_text(query):
    results = search_web(query)
    return "\n".join([f"- {r}" for r in results])

TOOLS = {
    "search": search_as_text,
    "summarize": lambda text: model.generate_content(f"Summarize this:\n\n{text}").text,
    "pdf": save_summary_to_pdf,
    "memory": print_memory,
}

def plan_tools(topic):
    prompt = f"""
You are an intelligent AI agent with access to these tools:
- search: to get web data
- summarize: to condense text
- pdf: to save output
- memory: to view past topics

User asked: "{topic}"

Decide which tools to use in order. Output only a Python list like:
['search', 'summarize', 'pdf']
"""
    result = model.generate_content(prompt)
    try:
        tool_plan = eval(result.text.strip())
        if isinstance(tool_plan, list):
            return tool_plan
    except:
        pass
    return ["search", "summarize", "pdf"]

# Streamlit App
st.title("🧠 Feedback Loop Agent")
st.markdown("Let the AI plan and execute a workflow using tools: `search`, `summarize`, `pdf`, `memory`.")

topic = st.text_input("Enter a topic:", placeholder="e.g. Future of Renewable Energy")

if st.button("Start Agent"):
    if not topic:
        st.warning("Please enter a topic first.")
    else:
        st.markdown(f"### 🎯 Topic: **{topic}**")
        steps = []
        current_data = topic
        done = False
        log = ""

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
                st.success("✅ Task completed.")
                done = True
                break

            if plan not in TOOLS:
                st.error(f"⚠️ Invalid Tool: `{plan}`")
                break

            st.write(f"🧠 **Thought:** Use `{plan}`")
            st.write(f"🔧 **Action:** Running `{plan}`...")

            tool = TOOLS[plan]
            if plan == "pdf":
                tool(current_data, topic)
                observation = f"✅ PDF saved for topic: {topic}"
            elif plan == "memory":
                observation = tool("")
            else:
                current_data = tool(current_data)
                observation = current_data[:500] + "..." if isinstance(current_data, str) else "[⚠️] Non-text output"

            steps.append(f"Tool used: {plan}\nObservation: {observation}")
            with st.expander(f"📈 Step {len(steps)}: `{plan}`"):
                st.write(observation)

        if "summarize" in [s.lower() for s in steps[-2:]]:
            save_to_memory(topic, current_data)
            st.info("🧠 Summary saved to memory.")
