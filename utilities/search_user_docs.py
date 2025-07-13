from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os

def search_documents(user_id: str, query: str, k: int = 3) -> dict:
    from langchain_community.vectorstores import FAISS
    from langchain_openai import OpenAIEmbeddings

    db_path = os.path.join("db", user_id)
    if not os.path.exists(db_path):
        print("DB path not found:", db_path)
        return {"context": "No indexed documents found."}

    try:
        vectordb = FAISS.load_local(
            db_path, OpenAIEmbeddings(), allow_dangerous_deserialization=True
        )
    except Exception as e:
        print("Failed to load FAISS DB:", e)
        return {"context": "Error loading user's document DB."}

    try:
        results = vectordb.similarity_search(query, k=k)
    except Exception as e:
        print("FAISS search failed:", e)
        return {"context": "Error during search."}

    print(f"Search query: {query}")
    print(f"Retrieved {len(results)} chunks.")
    for i, doc in enumerate(results):
        print(f"Chunk {i+1}:\n{doc.page_content[:200]}\n{'-'*40}")

    if not results:
        return {"context": "No relevant content found in your documents."}

    context = "\n\n".join([doc.page_content for doc in results])
    return {"context": context}

