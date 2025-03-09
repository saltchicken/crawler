import argparse
from .scraper import scrape_website
from .llm.api import query_ollama


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The URL to scrape")
    args = parser.parse_args()

    page_content = scrape_website(args.url)
    system_message = "Summarize the following text"
    for paragraph in page_content.paragraphs:
        print(paragraph)
        # response = query_ollama("test", paragraph, system_message, verbose=True)
        # print(response)


if __name__ == "__main__":
    main()
