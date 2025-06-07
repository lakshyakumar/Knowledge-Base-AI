

from app.src.common.types import GraphState, WebPageSummaryInputDependencies
from langchain_core.messages import  AIMessage, HumanMessage
from app.src.graph.agents import init_agent, summarizing_agent
from app.src.scraper.advanced_scraper import scrape_website
from app.src.scraper.simple_scraper import summarize_webpage


def init_node(state: GraphState):
    # print(f"Initializing with query: {state['query']}")
    response = init_agent.run_sync(state['query']) 
    return {
        "messages": [AIMessage(content="Initializing...")],
        "url": response.output.url,
        "comments": response.output.comments,
    }
    
def scraping_node(state: GraphState):
    # print(f"Scraping with query: {state['url']} and comments: {state['comments']}")
    if not state['url']:
        return {
            "messages": [AIMessage(content="No URL provided for scraping.")],
        }
    else:
        text, title = summarize_webpage(state['url'])

    return {
        "messages": [AIMessage(content="Scraped the webpage successfully.")],
        "scraped_text": text,
        "title": title,
    }
    
def advanced_scraping_node(state: GraphState):
    # print(f"Scraping with query: {state['url']} and comments: {state['comments']}")
    if not state['url']:
        return {
            "messages": [AIMessage(content="No URL provided for scraping.")],
        }
    else:
        text, title = scrape_website(state['url'])

    return {
        "messages": [AIMessage(content="Scraped the webpage successfully.")],
        "scraped_text": text,
        "title": title,
    }
    
def final_node(state: GraphState):
    # print(f"Finalizing process for query: {state}")
    if not state['scraped_text']:
        return {
            "messages": [AIMessage(content="No text scraped to finalize.")],
        }
    print(f"Generating summary for the scraped text with title: {state['title']}")
    response = summarizing_agent.run_sync(state["query"],deps=WebPageSummaryInputDependencies(
        query= state['query'],
        text= state['scraped_text'],
        title= state['title'],
        comments= state['comments'] if state['comments'] else None
    ))
    
    print(f"Generated title: {response}")
    
    
    return {
        "messages": [AIMessage(content=response.output["summary"])],
        "title": response.output["title"],
        "summary": response.output["summary"],
    }