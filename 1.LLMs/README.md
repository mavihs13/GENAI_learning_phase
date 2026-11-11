# 1. LLMs

## What
Introduction to using Large Language Models (LLMs) directly via LangChain.

## Tech
- `langchain-google-genai` — Google Gemini model wrapper
- `python-dotenv` — loads API keys from `.env`

## Files

### `1.LLMs.Demo.py`
- **What**: Sends a plain text prompt to Gemini and prints the response.
- **How**: Initializes `ChatGoogleGenerativeAI` with `gemini-3.8-flash`, calls `.invoke()` with a string prompt.
- **When to use**: When you want the simplest possible LLM call — no templates, no history, just a question and an answer.

## Key Concepts
- `ChatGoogleGenerativeAI` — LangChain wrapper for Gemini chat models
- `temperature=0` — deterministic output
- `max_tokens` — limits response length
- `llm.invoke(prompt)` — synchronous single-turn call
