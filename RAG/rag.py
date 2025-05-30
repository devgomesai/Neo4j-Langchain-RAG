from langchain_neo4j import GraphCypherQAChain, Neo4jGraph
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

# LLM Model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001", temperature=0, api_key=os.getenv("GOOGLE_API_KEY"))

#Graph Database
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)
graph.query(
"""
MERGE (m:Movie {name:"Top Gun", runtime: 120})
WITH m
UNWIND ["Tom Cruise", "Val Kilmer", "Anthony Edwards", "Meg Ryan"] AS actor
MERGE (a:Actor {name:actor})
MERGE (a)-[:ACTED_IN]->(m)
"""
)

graph.refresh_schema()
print('** GRAPH SCHEMA **')
print(graph.schema)
print('** --- **')

if __name__ == "__main__":
    chain = GraphCypherQAChain.from_llm(llm=llm, graph=graph, verbose=True, allow_dangerous_requests=True)
    while True:
        user_query = input("Enter your query: ")
        if user_query in ["exit", "quit", "bye"]:
            print("Exiting...") 
            break
        print(chain.invoke({"query": user_query})['result'])
        print('** --- **')


