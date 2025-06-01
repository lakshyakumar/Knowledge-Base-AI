from pydantic_ai import Agent, RunContext
import os

from app.src.common.types import InitAgentOutput, WebPageSummaryInputDependencies, WebPageSummaryOutput

init_agent = Agent(
    os.getenv("MODEL", "gpt-40-mini"),
        output_type=InitAgentOutput,
        system_prompt=(
            # The system prompt instructs the agent to:
            # 1. Extract all URLs from the given text.
            # 2. Identify key things to focus on or analyze within the text.
            "Your task is to analyze the provided text. First, extract URL present in the query. "
            "Then, identify and list the key things we need to focus on or analyze based on the context."
            "return url and comments(focus areas) in the output object. "
        )
    )

summarizing_agent = Agent(
    os.getenv("MODEL", "gpt-40-mini"),
        deps_type=WebPageSummaryInputDependencies,
        output_type=WebPageSummaryOutput,
    )

@summarizing_agent.system_prompt
def generate_system_prompt(ctx: RunContext[WebPageSummaryInputDependencies]) -> str:
    """
    Dynamically generates a summary and notes from the scraped web page.
    """

    
    # add a prompt such that the llm reply to with the correct prompt if user is ambiguous
    
    
    prompt = f"""
            You are an agent that summarizes(in-depth) text and creates a flashy title. Follow these guidelines:

            - **Input Structure:**  
            Use the following fields from `ctx.deps` as input:  
              - `query: str`  
              - `text: str`  
              - `title: str`  
              - `comments: Union[list[str], None] = None`  

            - **Summarization:**  
            Summarize and create notes for the content below as md file. 
            **{ctx.deps['text']}**
            Incorporate the `query` and `comments` (if available) into the summary for additional context. 
            query: **{ctx.deps['query']}**
            comments:
            **{ctx.deps['comments']}**
                

            - **Title Generation:**  
            Use the `title` field as a base to create a **flashy and engaging title**.  
            title: **{ctx.deps['title']}** 
            Ensure the title is concise, attention-grabbing, and relevant to the summarized content.  

            - **Response Formatting:**  
            Present the output in **Markdown**, using:  
              - A bold heading for the flashy title  
              - A bullet point for the summary  

            - **Dynamic Context Updates:**  
            After generating the summary and title, update the context with the new summary and title.  

            Maintain a professional yet creative tone.
        """
    return prompt


