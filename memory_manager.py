import json
from datetime import datetime
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_to_memory(topic, summary):
    memory = load_memory()
    entry = {
        "topic": topic,
        "summary": summary,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    memory.append(entry)
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def print_memory():
    memory = load_memory()
    print("\n🗂️ Previous Topics Summary History:\n")
    for entry in memory:
        print(f"[{entry['timestamp']}] - {entry['topic']}")

