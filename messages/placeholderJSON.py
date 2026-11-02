
import json
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

template = ChatPromptTemplate([
    ("system", "You are a helpful customer support assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

with open("chat_history.json", "r", encoding="utf-8") as f:
    history_data = json.load(f)

chat_history = [
    (message["role"], message["content"])
    for message in history_data
]

prompt = template.invoke({
    "chat_history": chat_history,
    "query": "What about my refund?"
})

print(prompt)
