
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0,
    max_retries=2,
    max_tokens = 1024
)

  

try:
    response = llm.invoke(
        "Explain prompt template in simple words."
    )
    print(response.text)

except Exception as e:
    print("Error:", e)