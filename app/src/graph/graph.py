from langgraph.graph.state import StateGraph, START
from app.src.common.types import GraphState
from app.src.graph.nodes import final_node, init_node, scraping_node
from langchain_core.messages import AIMessage, HumanMessage

class Graph:
    graph = None
    def __init__(self):
        self.graph_builder = StateGraph(GraphState)
        
        self.graph_builder.add_node( "init_node", init_node )
        self.graph_builder.add_node("scraping_node", scraping_node)
        self.graph_builder.add_node("final_node", final_node)
        
        self.graph_builder.add_edge(START, "init_node")
        self.graph_builder.add_edge("init_node", "scraping_node")
        self.graph_builder.add_edge("scraping_node", "final_node")
        self.graph = self.graph_builder.compile()
        
    def invoke(self, query: str):
        try:
            state = GraphState(query=query, messages=[HumanMessage(content=query)])
            result = self.graph.invoke(state)
            return result["messages"][-1].content if result["messages"] else "No response generated."
        except Exception as e:
            print(f"An error occurred in invoke: {str(e)}")
            return f"An error occurred: {str(e)}"