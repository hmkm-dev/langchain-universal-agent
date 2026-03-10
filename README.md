# LangChain Universal Agent

This is a simple LangChain-based AI agent that can take a task, perform a web search, and generate an answer using a Hugging Face model.

## Setup

1. Create a Hugging Face API token.
2. Add it to GitHub repository secrets as `HF_TOKEN`.
3. Run the GitHub Action workflow and provide a task input.

## Files

- main.py : Main AI agent logic
- requirements.txt : Python dependencies
- .github/workflows/run.yml : GitHub Actions automation
