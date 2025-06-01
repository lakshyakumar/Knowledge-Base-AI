from app.src.graph.graph import Graph
from fastapi import APIRouter, Query

# Create a router instance
router = APIRouter()
main_graph = Graph()


@router.get("/")
def crawl(
     query: str = Query(..., description="What you want to scrape today?"),
):
    try:
        result = main_graph.invoke(query)
        return {"query": query, "result": result, "success": True}
    except Exception as e:
        return {"query": query, "result": None, "success": False, "error": str(e)}