from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from loguru import logger

from scraper.models import PageContent

def check_robots_txt(url):
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    robots_url = base_url + "/robots.txt"
    rp = RobotFileParser(robots_url)
    rp.read()
    if rp.can_fetch("*", url):
        logger.debug("Robots.txt allows scraping.")
        return True
    else:
        return False

def get_html(url):
    if check_robots_txt(url) == False:
        raise UnableToScrape("Robots.txt disallows scraping.")
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration
    options.add_argument("--no-sandbox")  # Disable sandboxing
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(url)
    html = driver.page_source
    driver.quit()
    if html:
        return html
    else:
        raise UnableToScrape("Unable to scrape website")

def scrape_website(url):
    try:
        html = get_html(url)
    except Exception as e:
        print(f"Error: {e}")
        return

    # TODO: Make sure that soup was successful
    soup = BeautifulSoup(html, "lxml")

    page_content = PageContent()

    if soup.title:
        title = soup.title.string
        if "404" in title:
            raise NotFound()
        if title == "Not Found":
            raise NotFound()
        page_content.title = title

    headings = soup.find_all("h1", "h2", "h3")
    page_content.headings = [heading.text.strip() for heading in soup.find_all(['h1', 'h2', 'h3'])]

    return page_content



if __name__ == "__main__":
    # Example usage
    url = "https://en.wikipedia.org"
    get_html(url)

