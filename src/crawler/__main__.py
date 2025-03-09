from .scraper import scrape_website
from .llm.api import query_ollama


def main():
    url = "https://en.wikipedia.org/wiki/Java"
    page_content = scrape_website(url)
    system_message = "Summarize the following text"
    for paragraph in page_content.paragraphs:
        response = query_ollama("test", paragraph, system_message, verbose=True)
        print(response)


if __name__ == "__main__":
    main()
