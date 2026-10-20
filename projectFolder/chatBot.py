from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b",temperature=0.5)

chatHistory = []

while True:
    user_input = input("you: ")
    chatHistory.append(user_input)
    if user_input.lower() == "exit":
        break
    try:
        response = llm.invoke(chatHistory)
        chatHistory.append(response.text)
        print("WALi: ", response.text)
    except Exception as e:
        print("Error:", e)    

print("Chat session ended.")
print("Conversation History:")
print("\n".join(chatHistory))        