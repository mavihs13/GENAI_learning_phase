from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

template = ChatPromptTemplate([
    ('system', 'You are a helpful  assistant.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readline())

prompt = template.invoke({'chat_history': chat_history, 'query': 'what about my refund ?'})

print(prompt)
print(chat_history)