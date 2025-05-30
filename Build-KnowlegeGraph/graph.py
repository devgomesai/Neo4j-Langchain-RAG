import os
from langchain_neo4j import Neo4jGraph
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.documents import Document
load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")


llm = ChatOllama(temperature=0, model="gemma3")

llm_transformer = LLMGraphTransformer(llm=llm)


graph = Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
    refresh_schema=False
)

text = """
Isaac Newton, born in 1643, was an English mathematician, physicist, astronomer, and author who is widely recognized as one of the most influential scientists of all time.  
He formulated the laws of motion and universal gravitation, laying the groundwork for classical mechanics.  
His work, "Philosophiæ Naturalis Principia Mathematica," published in 1687, remains one of the most important scientific books ever written.  
Newton also made pioneering contributions to optics and developed a form of calculus independently around the same time as Leibniz.  
He served as president of the Royal Society and was knighted by Queen Anne in 1705.
"""

documents = [Document(page_content=text)]
import asyncio

async def main():
    graph_documents = await llm_transformer.aconvert_to_graph_documents(documents)
    graph.add_graph_documents(graph_documents)
    print(f"Nodes: {graph_documents[0].nodes}")
    print(f"Relationships: {graph_documents[0].relationships}")
asyncio.run(main())

