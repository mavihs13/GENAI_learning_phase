# Messages

## What
Covers LangChain message types, `ChatPromptTemplate`, chat history management, and `MessagesPlaceholder` for dynamic history injection.

## Tech
- `langchain-core` — `ChatPromptTemplate`, `MessagesPlaceholder`, message types
- `langchain-google-genai` — Gemini model
- `langchain-groq` — Groq model
- `python-dotenv` — API key management

## Files

### `1.messages.py`
- **What**: Demonstrates the three core message types: `SystemMessage`, `HumanMessage`, `AIMessage`.
- **How**: Builds a message list manually, invokes the model, appends the AI response back to history.
- **When**: Use to understand how multi-turn conversation history is structured in LangChain.

### `chat_prompt_template.py`
- **What**: Uses `ChatPromptTemplate` with `{domain}` and `{topic}` variables.
- **How**: Defines a system + human message template, fills it with `.invoke({...})`, sends to Gemini.
- **When**: Use when you want a reusable chat prompt with dynamic role-based messages.

### `chatPrompt_byinput.py`
- **What**: Same as `chat_prompt_template.py` but takes `domain` and `topic` from terminal input.
- **How**: `input()` → `template.invoke()` → `llm.invoke()` → print response.
- **When**: Use for interactive CLI demos of chat prompt templates.

### `message_placeholder.py`
- **What**: Injects chat history from a `.txt` file into a prompt using `MessagesPlaceholder`.
- **How**: Reads `chat_history.txt`, passes it as `chat_history` variable to the template.
- **When**: Use to understand how `MessagesPlaceholder` dynamically inserts a variable-length history.

### `placeholderJSON.py`
- **What**: Same as `message_placeholder.py` but reads history from `chat_history.json`.
- **How**: Parses JSON into `(role, content)` tuples, injects via `MessagesPlaceholder`.
- **When**: Use when chat history is stored in structured JSON format (more realistic production pattern).

### `chat_history.txt` / `chat_history.json`
- **What**: Sample chat history files used by the placeholder demos.

## Key Concepts
- `SystemMessage` — sets the AI's persona/behavior
- `HumanMessage` — represents user input
- `AIMessage` — represents model response
- `ChatPromptTemplate` — structured multi-role prompt template
- `MessagesPlaceholder` — inserts a dynamic list of messages at a named position in the template
