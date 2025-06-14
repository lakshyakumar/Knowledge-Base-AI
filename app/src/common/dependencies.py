from dataclasses import dataclass
from typing import Union


@dataclass
class WebPageSummarizeAgentDependency:
    """
    object to be used in the agent 
    """
    title: str
    text: str