# import google.generativeai as genai
# from dotenv import load_dotenv
# import os
# from search_tool import search_web
# from pdf_writer import save_summary_to_pdf
# from memory_manager import save_to_memory , print_memory


# # Load API keys
# load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# genai.configure(api_key=GEMINI_API_KEY)

# # Use Gemini model
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Take input
# topic = input("🧠 Topic batao jiska deep summary chahiye: ")

# # Step 1: Web Search
# print("\n🌐 Searching web for relevant info...")
# search_results = search_web(topic)

# # Step 2: Combine into one text
# combined = "\n".join(search_results)

# # Step 3: Gemini Summary
# prompt = f"""
# You are a research assistant. Summarize the following web results into a deep, structured report:

# Topic: {topic}

# Web results:
# {combined}
# """
# response = model.generate_content(prompt)

# # Final output
# print("\n📘 Gemini Summary Based on Web:\n")
# print(response.text)
# # Step 4: Save to PDF
# save_summary_to_pdf(response.text, topic)
# # Save to memory
# save_to_memory(topic, response.text)
# # Print memory
# print_memory()


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

# 🧠 Fix: Format list results from search into clean string
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

def feedback_loop_agent(topic):
    print(f"\n🧠 [Agent Goal] \"{topic}\"\n")

    current_data = topic
    steps = []
    done = False

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
            print("✅ [Agent Finished] Task completed.")
            done = True
            continue

        if plan not in TOOLS:
            print(f"⚠️ [Invalid Tool]: {plan}")
            break

        print(f"🧠 [Thought] I should now use the `{plan}` tool.")
        print(f"🔧 [Action] Running `{plan}`...")

        tool = TOOLS[plan]
        if plan == "pdf":
            tool(current_data, topic)
            observation = f"PDF saved for topic: {topic}"
        elif plan == "memory":
            observation = tool("")
        else:
            current_data = tool(current_data)
            observation = current_data[:500] + "..." if isinstance(current_data, str) else "[⚠️] Non-text output"

        steps.append(f"Tool used: {plan}\nObservation: {observation}")
        print(f"📈 [Observation] {observation}")
        print("-" * 60)

    # Save to memory if a summary was generated
    if "summarize" in [s.lower() for s in steps[-2:]]:
        save_to_memory(topic, current_data)
        print("🧠 [Memory] Saved summary.")

if __name__ == "__main__":
    topic = input("🧠 Topic batao jiska deep kaam chahiye: ")
    feedback_loop_agent(topic)
