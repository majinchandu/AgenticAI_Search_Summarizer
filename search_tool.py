import os
from dotenv import load_dotenv
import requests

load_dotenv()
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

def search_web(query):
    params = {
        "q": query,
        "num": 3,
        "api_key": SERPAPI_API_KEY,
        "engine": "google",
        "gl": "in",
    }

    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()

    if "organic_results" not in data:
        return ["No results found."]

    results = data["organic_results"]
    summaries = [result["snippet"] for result in results if "snippet" in result]
    return summaries
