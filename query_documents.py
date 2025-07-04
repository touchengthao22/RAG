from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

CHROMA_PATH = "chroma"
MODEL_NAME = "mistral"  # you can use "llama2", "phi", etc. if installed via Ollama

def ask_question(query: str):
    # Load embedding and vector store
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding)
    retriever = db.as_retriever()

    # Test retriever returns docs
    docs = retriever.get_relevant_documents(query)
    print(f"Found {len(docs)} relevant documents.")

    # Use Ollama model
    llm = Ollama(model=MODEL_NAME)

    # Retrieval + Generation
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # Run the query
    answer = qa_chain.run(query)
    print("\n💬 Answer:\n", answer)

if __name__ == "__main__":
    while True:
        query = input("\nAsk a question about the PDF (or type 'exit'): ")
        if query.lower() in ["exit", "quit"]:
            break
        ask_question(query)
