# LangChain Learning Project

A hands-on learning project covering LangChain fundamentals from LLMs to structured output, with Streamlit UIs.

## Project Structure

| Folder | What it covers |
|---|---|
| `1.LLMs/` | Basic LLM invocation with Google Gemini |
| `2.chatModels/` | Chat models via Gemini and HuggingFace (API & local) |
| `3.embeddings/` | Text embeddings, document embedding, similarity search |
| `4.prompt/` | Prompt templates, saving/loading, Streamlit UI |
| `messages/` | Message types, chat history, placeholders |
| `outputParse/` | Output parsers and chaining with StrOutputParser |
| `projectFolder/` | Full chatbot and UI projects |
| `structureOutput/` | Structured output using Pydantic |

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file with your API keys:
```
GOOGLE_API_KEY=<your_google_api_key>
HUGGINGFACEHUB_API_TOKEN=<your_hf_token>
GROQ_API_KEY=<your_groq_api_key>
```

## Tech Stack
- **LangChain** — core framework
- **Google Gemini** — LLM and embeddings
- **HuggingFace** — open-source models (API + local)
- **Groq** — fast inference API
- **Pydantic** — data validation and structured output
- **Streamlit** — web UI
- **scikit-learn / numpy** — cosine similarity for embeddings
