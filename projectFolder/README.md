# Project Folder

## What
Full end-to-end projects combining everything learned — chatbots with memory, Streamlit UIs, prompt templates, and output parsers.

## Tech
- `langchain-groq` — Groq LLM (fast inference)
- `langchain-google-genai` — Gemini chat model
- `langchain-core` — prompts, output parsers, message types
- `streamlit` — web UI
- `python-dotenv` — API key management

## Files

### `chatBot.py`
- **What**: Terminal chatbot with in-memory conversation history using Groq.
- **How**: Appends each user message and AI response to `chatHistory` list; passes the full list to `llm.invoke()` each turn.
- **When**: Use as the simplest multi-turn chatbot — no system prompt, no UI, just a loop.

### `chatBot2.0.py`
- **What**: Improved terminal chatbot using Gemini with proper `SystemMessage`, `HumanMessage`, `AIMessage` types.
- **How**: Starts history with a `SystemMessage`; appends typed message objects instead of raw strings.
- **When**: Use when you want structured, typed message history — the correct LangChain pattern for multi-turn chat.

### `chatPrompt_inputUi.py`
- **What**: Streamlit UI where the user picks a domain and topic; the app explains the topic using a `ChatPromptTemplate`.
- **How**: Form inputs → `template.invoke()` → `ChatGroq.invoke()` → `st.markdown(response.content)`.
- **When**: Use to demonstrate a clean Streamlit form UI with a structured chat prompt template.

### `strOutputParseUI.py`
- **What**: Streamlit UI that generates a detailed report and a 5-line summary using an LCEL chain.
- **How**: User enters a topic → `chain.invoke({topic})` runs `template1 | model | parse | template2 | model | parse` → displays summary.
- **When**: Use to show a multi-step LCEL pipeline exposed through a Streamlit interface.

### `wali_ui.py`
- **What**: Full Streamlit chatbot UI ("WALi AI") with persistent session-based conversation history.
- **How**: Uses `st.session_state.messages` to store history; renders chat bubbles with `st.chat_message`; sends only the latest message to the model.
- **When**: Use as a production-style chatbot UI with a proper chat interface and session memory.

## Running the Streamlit Apps

```bash
streamlit run projectFolder/wali_ui.py
streamlit run projectFolder/chatPrompt_inputUi.py
streamlit run projectFolder/strOutputParseUI.py
```

## Key Concepts
- `st.session_state` — persists data across Streamlit reruns
- `st.chat_message` / `st.chat_input` — Streamlit's native chat UI components
- LCEL chain in a UI — wrapping a `template | model | parser` pipeline inside a Streamlit button click
- Typed message history (`HumanMessage`, `AIMessage`) vs raw string history
