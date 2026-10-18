from langchain_huggingface import HuggingFaceEmbeddings

embedding  = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")

text = "In an open source model, the software source code is publicly available on a web-based platform, allowing anyone to download, view, modify, and distribute the software for free. This model encourages a culture of openness and collaboration, where developers and users can work together to improve and maintain the software."

try:
    vector = embedding.embed_query(text)
    print("Embedding vector:", str(vector))
except Exception as e:
    print("Error:", e)    
