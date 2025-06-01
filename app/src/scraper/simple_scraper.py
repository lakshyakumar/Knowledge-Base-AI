import httpx
from bs4 import BeautifulSoup

from app.src.common.types import WebPageSummary



# Function to extract clean text from HTML
def extract_visible_text(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')

    # Remove script/style tags
    for tag in soup(['script', 'style', 'noscript']):
        tag.decompose()

    return soup.get_text(separator='\n', strip=True)

# Function to fetch and summarize a webpage
def summarize_webpage(url: str) -> WebPageSummary:
    response = httpx.get(url)
    response.raise_for_status()

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string if soup.title else 'Untitled'
    text = extract_visible_text(html)

    return text, title