# 🧠 LangChain x Neo4j x Ollama | Knowledge Graph from Text

This project demonstrates how to build a **structured knowledge graph** from unstructured text using:

- 🧱 **Neo4j** for storing and visualizing the graph  
- 🧠 **LangChain's LLMGraphTransformer** for graph extraction  
- 💬 **Ollama (Gemma3)** as the local LLM backend  
- 🧪 **LangChain Experimental** modules for graph transformation  

---

## 📌 Features

- Converts raw text into entities and relationships  
- Automatically generates graph nodes and edges using LLM  
- Inserts the knowledge graph into a running Neo4j database  
- Uses `Ollama` to run `Gemma3` locally for cost-effective LLM processing  

---

## 📦 Dependencies

```bash
pip install langchain langchain-core langchain-neo4j langchain-experimental langchain-ollama python-dotenv
````

Also make sure:

* Neo4j is installed and running (AuraDB or local)
* Ollama is installed and the `gemma3` model is pulled:

```bash
ollama pull gemma3
```

---

## ⚙️ Setup

1. Create a `.env` file with your Neo4j credentials:

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```

2. Run the script:

```bash
python main.py
```

---

## 🧪 Example Text Used

> Isaac Newton, born in 1643, was an English mathematician, physicist, astronomer, and author who is widely recognized as one of the most influential scientists of all time.
> He formulated the laws of motion and universal gravitation, laying the groundwork for classical mechanics.
> His work, *Philosophiæ Naturalis Principia Mathematica*, published in 1687, remains one of the most important scientific books ever written.
> Newton also made pioneering contributions to optics and developed a form of calculus independently around the same time as Leibniz.
> He served as president of the Royal Society and was knighted by Queen Anne in 1705.

---

## 🖼️ Output Preview

```text
Nodes: ['Person: Isaac Newton', 'Book: Philosophiæ Naturalis Principia Mathematica', 'Institution: Royal Society']
Relationships: ['WROTE', 'PRESIDENT_OF', 'WAS_KNIGHTED_BY']
```

---

## 🚀 Why This Project?

This setup is ideal for:

* Research-based knowledge extraction
* Building academic assistants
* Structured reasoning systems using LLMs

---

## 🤖 Tech Stack

| Component       | Tool                      |
| --------------- | ------------------------- |
| LLM             | Ollama (Gemma3)           |
| Graph DB        | Neo4j                     |
| Graph Extractor | LangChain Experimental    |
| Integration     | LangChain + Python dotenv |

---

## 📚 To Try It Out

Clone the repo, install the requirements, set up your `.env`, and run it locally!
You can switch out `Gemma3` for any other LLM supported by Ollama.

---
