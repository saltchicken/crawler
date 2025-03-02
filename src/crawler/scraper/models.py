from dataclasses import dataclass
from typing import Optional, List

@dataclass
class PageContent:
    url: str
    title: Optional[str] = None
    headings: Optional[List[str]] = None
    paragraphs: Optional[List[str]] = None
