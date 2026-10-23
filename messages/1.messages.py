from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain prompt template in simple words."),
]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))
print(messages)