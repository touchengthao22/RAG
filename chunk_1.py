from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents(path: str, encoding='utf-8'):
    try:
        loader = TextLoader(path, encoding=encoding)
        documents = loader.load()
        print(f'loaded {len(documents)} documents')
        return documents
    
    except Exception as e:
        print(f'Failed to Load: {e}')
        return []

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True
    )

    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks

if __name__ == "__main__":
    DATA_PATH = 'data/alice_in_wonderland.md'
    doc = load_documents(DATA_PATH)
    split_text(doc)