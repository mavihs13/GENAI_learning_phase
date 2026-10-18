from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model = "gemini-embedding-001",
    dimension = 32
)
documents = [
    "In an open source model, the software source code is publicly available on a web-based platform, ",
    "allowing anyone to download, view, modify, and distribute the software for free. This model encourages a culture of openness and collaboration,",
    " where developers and users can work together to improve and maintain the software."
]
embed = embedding.embed_documents(documents)
print(str(embed))