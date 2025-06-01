

from dataclasses import dataclass
from typing import Annotated, Union
from pydantic import BaseModel
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class GraphState(TypedDict):
    query: str
    url: str | None
    title: str | None
    summary: str | None
    scraped_text: str | None
    comments: Union[list[str], None] = None
    messages: Annotated[list, add_messages]
    
# Pydantic schema for the output
class WebPageSummary(BaseModel):
    title: str
    summary: str
    url: str
    
@dataclass
class WebPageSummaryOutput(TypedDict):
    title: str
    summary: str

@dataclass
class WebPageSummaryInputDependencies(TypedDict):
    query: str
    text: str
    title: str
    comments: Union[list[str], None] = None
    
@dataclass
class InitAgentOutput:
    """
    object to be used in the init agent 
    """
    url: str
    comments: Union[list[str], None] = None