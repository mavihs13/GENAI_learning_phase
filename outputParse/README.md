# Output Parsers

## What
Covers parsing LLM responses and chaining multiple prompts together using LangChain's LCEL (LangChain Expression Language) pipe syntax.

## Tech
- `langchain-core` — `PromptTemplate`, `StrOutputParser`
- `langchain-groq` — Groq LLM
- `python-dotenv` — API key management

## Files

### `simpleOutput.py`
- **What**: Chains two prompts manually — generates a report, then summarizes it.
- **How**: Calls `model.invoke()` twice; passes `response1.text` directly into the second template.
- **When**: Use to understand the manual (non-LCEL) approach to chaining prompts.

### `strOutputParse.py`
- **What**: Same two-step chain but built using LCEL pipe (`|`) syntax with `StrOutputParser`.
- **How**: `chain = template1 | model | parse | template2 | model | parse` — a single pipeline invoked with `.invoke()`.
- **When**: Use to understand LCEL chaining — the modern, composable way to build LangChain pipelines.

## Key Concepts
- `StrOutputParser` — extracts the plain string text from a model response object
- LCEL `|` pipe operator — composes runnables into a sequential chain
- Without `StrOutputParser`, the model output is an `AIMessage` object, not a plain string — the parser bridges the gap between steps
