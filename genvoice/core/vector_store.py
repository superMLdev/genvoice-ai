from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def create_vector_store(docs):
    embedding = OpenAIEmbeddings()
    return FAISS.from_documents(docs, embedding)