class UnableToScrape(Exception):
    def __init__(self, message="Unable to scrape website"):
        super().__init__(message)

class NotFound(Exception):
    def __init__(self, message="Page Not Found"):
        super().__init__(message)
