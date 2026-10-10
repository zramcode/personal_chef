from dotenv import load_dotenv
load_dotenv()

from typing import Dict, Any
from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import create_agent

#from tavily import TavilyClient

#tavilyclient = TavilyClient()
from ddgs import DDGS

@tool
def web_search(query: str) -> str:
    """Search the web for recipes and cooking information."""

    try:
        results = DDGS().text(
            query,
            max_results=5
        )

        if not results:
            return "No search results found."

        formatted_results = []

        for result in results:
            formatted_results.append(
                f"Title: {result.get('title', '')}\n"
                f"URL: {result.get('href', '')}\n"
                f"Snippet: {result.get('body', '')}"
            )

        return "\n\n".join(formatted_results)

    except Exception as e:
        return f"Web search failed: {str(e)}"


def main():
    llm = ChatOllama(
    model="qwen2.5:0.5b",
    temperature=0.2,
    num_predict=256,
    num_ctx=2048
    )
    system_prompt = """The user will provide you with a list of ingredients they have available at home.

Your job is to help the user find recipes that can be prepared using those ingredients.

When necessary, use the web search tool to find relevant recipes and cooking ideas online.

When suggesting recipes:
- Prefer recipes that use most of the ingredients provided by the user.
- Clearly mention which ingredients from the user's list are used.
- Mention any additional ingredients that may be needed.
- Provide several recipe suggestions when appropriate.
- Do not invent information from web search results.

If the user asks for a specific recipe, provide:
1. A list of required ingredients and quantities.
2. Clear, step-by-step cooking instructions.
3. Cooking time and approximate serving size when available.

Be helpful, practical, and concise.
"""

    question = {
    "messages": [
        {
            "role": "user",
            "content": "I have eggs, potatoes, onions and cheese. What can I cook?"
        }
     ]
    }

    agent = create_agent(
    model = llm,
    tools = [web_search],
    system_prompt = system_prompt
    )

    result = agent.invoke(question)

    print(result["messages"][-1].content)


if __name__ == "__main__":
        main()