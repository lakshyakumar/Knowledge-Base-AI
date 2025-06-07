import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service 
from bs4 import BeautifulSoup
from app.config.config import CONFIG

# Function to extract clean text from HTML
def extract_visible_text(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')

    if soup.body:
        # Remove script/style tags
        for tag in soup(['script', 'style', 'noscript']):
            tag.decompose()

        return soup.get_text(separator='\n', strip=True)
    return ""
    

def scrape_website(website):
    print(f"Scraping website: {website}")
    chrome_driver_path = CONFIG["chrome_driver_path"]  # Update this path to your chromedriver location
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    try:
        driver.get(website)
        title = driver.title
        content = driver.page_source
        # print(f"Content scraped from {website}: {content[:100]}...")  # Print first 100 characters
        text = extract_visible_text(content)
        return text, title
    except Exception as e:
        print(f"Error scraping {website}: {e}")
    finally:
        driver.quit()
        print(f"Driver closed for {website}")
        
    
    