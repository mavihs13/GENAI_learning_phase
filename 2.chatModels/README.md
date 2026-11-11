# 2. Chat Models

## What
Demonstrates chat model usage across multiple providers: Google Gemini, HuggingFace API, and HuggingFace local pipeline.

## Tech
- `langchain-google-genai` — Gemini chat model
- `langchain-huggingface` — HuggingFace chat wrappers
- `transformers` — local model pipeline
- `python-dotenv` — API key management

## Files

### `chatModel_gemini.py`
- **What**: Invokes Gemini chat model with a plain string prompt.
- **How**: Uses `ChatGoogleGenerativeAI` with `gemini-3.8-flash`.
- **When**: Use when you want a managed cloud-based chat model with no local setup.

### `chatModel_HF_api.py`
- **What**: Calls a HuggingFace-hosted model (`TinyLlama`) via the Inference API.
- **How**: `HuggingFaceEndpoint` connects to the HF API; `ChatHuggingFace` wraps it for chat-style invocation.
- **When**: Use when you want to run an open-source model without downloading it locally.

### `chatModel_HF_local.py`
- **What**: Runs `TinyLlama` fully locally using a HuggingFace pipeline.
- **How**: `HuggingFacePipeline.from_model_id()` downloads and runs the model on your machine; `ChatHuggingFace` wraps it.
- **When**: Use when you need offline inference or want full control over the model.

## Key Concepts
- `ChatHuggingFace` — unified chat interface for HF models
- `HuggingFaceEndpoint` vs `HuggingFacePipeline` — API vs local execution
- `task="text-generation"` — required task type for text models
