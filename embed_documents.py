# from langchain.document_loaders import DirectoryLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import openai 
import os
import shutil
from chunk_1 import load_documents, split_text

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


CHROMA_PATH = "chroma"
FILE_PATH = "data/output_text.txt"

def main():
      doc = load_documents(FILE_PATH)
      chunks = split_text(doc)
      save_to_chroma(chunks)
      

def save_to_chroma(chunks):
    if os.path.exists(CHROMA_PATH):
            shutil.rmtree(CHROMA_PATH)
    
    db = Chroma.from_documents(
          chunks, embedding=embedding, persist_directory=CHROMA_PATH
    )

    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

if __name__ == "__main__":
      main()



