from scraper import scrape_website

def main():
    url = "https://en.wikipedia.org/wiki/Java"
    page_content = scrape_website(url)
    print(page_content)

if __name__ == "__main__":
    main()
