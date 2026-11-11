# 3. Embeddings

## What
Covers text embeddings — converting text into numerical vectors — and using them for document similarity search.

## Tech
- `langchain-google-genai` — Gemini embedding model
- `langchain-huggingface` — local sentence-transformer embeddings
- `sentence-transformers` — underlying HF embedding model
- `scikit-learn` — cosine similarity calculation
- `numpy` — array operations
- `python-dotenv` — API key management

## Files

### `embedding_demo.py`
- **What**: Embeds a single text string into a vector.
- **How**: `GoogleGenerativeAIEmbeddings.embed_query()` returns a list of floats.
- **When**: Use to understand what an embedding looks like and verify your setup.

### `embedding_docs.py`
- **What**: Embeds a list of documents (multiple strings) at once.
- **How**: `embed_documents()` takes a list and returns a list of vectors.
- **When**: Use when you need to embed a corpus of documents for storage or comparison.

### `document_similarity.py`
- **What**: Finds the most similar document to a query using cosine similarity.
- **How**: Embeds both the query and all documents, then uses `cosine_similarity` from scikit-learn to rank results.
- **When**: Use to build a basic semantic search — find the best matching document for a user question.

### `embedding_local_repo.py`
- **What**: Generates embeddings locally using a HuggingFace sentence-transformer model.
- **How**: `HuggingFaceEmbeddings` with `sentence-transformers/all-MiniLM-L12-v2` runs entirely on your machine.
- **When**: Use when you want free, offline embeddings without any API calls.

## Key Concepts
- `embed_query()` — embeds a single string (for search queries)
- `embed_documents()` — embeds a list of strings (for a document corpus)
- `cosine_similarity` — measures how similar two vectors are (1 = identical, 0 = unrelated)
- `dimension` — controls the size of the output vector
