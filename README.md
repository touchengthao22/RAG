# 🧠 RAG-Powered Medical Document Analyzer

This project is a **Retrieval-Augmented Generation (RAG)** system designed to help review medical documents efficiently and accurately. It combines semantic search with a powerful language model to answer questions and summarize medical content.

---

## 📌 Purpose

I created this project to **assist with reading and analyzing medical documents** while reviewing worker compensation claims. The goal is to:

- Quickly determine an employee's **work status**
- Decide if a case is **OSHA-recordable**
- Save time and reduce errors during **manual review**

This tool is especially useful when dealing with high volumes of documents and ambiguous clinical language.

---

## 🛠️ How It Works

1. **Ingest Documents**: Load `.txt` or `.pdf` files into a vector store using embeddings
2. **Semantic Search**: Retrieve the most relevant document chunks for a given question
3. **LLM Generation**: Use a language model (e.g. OpenAI GPT-3.5) to generate human-like answers or summaries based on retrieved content

---
