from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm  = HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", task = "text-generation")
try:
   model  = ChatHuggingFace(llm=llm)

   result = model.invoke("explain what is open source model") 

   print(result.text)
except Exception as e:
    print("Error:", e)   
