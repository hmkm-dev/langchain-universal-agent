import os
import requests
from bs4 import BeautifulSoup
from langchain_community.llms import HuggingFaceHub

token = os.environ["HF_TOKEN"]

llm = HuggingFaceHub(
    repo_id="google/flan-t5-large",
    huggingfacehub_api_token=token,
    model_kwargs={"temperature":0.7,"max_length":300}
)

TASK = os.environ.get("TASK", "Explain artificial intelligence")

def web_search(query):
    url = f"https://duckduckgo.com/html/?q={query}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")

    results = []
    for a in soup.find_all("a",class_="result__a")[:5]:
        results.append(a.text)

    return results

print("TASK:",TASK)

search_results = web_search(TASK)

print("SEARCH RESULTS:")
print(search_results)

prompt = f"""
You are an AI assistant.

User task:
{TASK}

Use this information:

{search_results}

Generate the best possible answer.
"""

response = llm.invoke(prompt)

print("\nFINAL ANSWER\n")
print(response)
