from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    dimension=300
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

question = "Who is the best Indian cricketer?"

embed_documents = embedding.embed_documents(documents)
embed_question = embedding.embed_query(question)

score =  cosine_similarity([embed_question], embed_documents)[0]

index,score = sorted(list(enumerate(score)),key=lambda X:X[1])[-1]

print("Question:", question)
print("Most similar document:", documents[index])
print("Similarity score:", score)