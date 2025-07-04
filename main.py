from chunk_1 import load_documents, split_text
from embed_documents import save_to_chroma
from query_documents import ask_question
from convert_img import convert_pdf_image_text

import os

DATA_PATH = "data/alice_in_wonderland.md"
OCR_OUTPUT_PATH = "data/output_text.txt"
CHROMA_PATH = "chroma"

def main():

    while True:
        print("📚 PDF QA System")
        print("====================")
        print("1. Load & Embed Text-Based PDF")
        print("2. Load & Embed Scanned PDF (OCR)")
        print("3. Start Chatbot")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            docs = load_documents(DATA_PATH)
            chunks = split_text(docs)
            save_to_chroma(chunks)

        elif choice == "2":
            print("🖨️ Running OCR on scanned PDF...")
            extracted_text = convert_pdf_image_text(DATA_PATH)
            with open(OCR_OUTPUT_PATH, 'w', encoding='utf-8') as f:
                f.write(extracted_text)

            # Now load the resulting text
            docs = load_documents(OCR_OUTPUT_PATH)
            chunks = split_text(docs)
            save_to_chroma(chunks)

        elif choice == "3":
            print("🧠 Chatbot ready! Type 'exit' to stop.")
            while True:
                query = input("\nAsk a question: ")
                if query.lower() in ["exit", "quit"]:
                    break
                ask_question(query)

        elif choice == "4":
            print("👋 Goodbye.")
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
