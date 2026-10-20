from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash")

chatHistory = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input("you: ")
    chatHistory.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    try:
        response = model.invoke(chatHistory)
        chatHistory.append(AIMessage(content=response.content))
        print("WALi: ", response.text)
    except Exception as e:
        print("Error:", e)    

print("Chat session ended.")
print("Conversation History:")
print(chatHistory)  