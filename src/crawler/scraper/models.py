from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class PageContent:
    url: str
    title: Optional[str] = None
    headings: Optional[List[str]] = None
    paragraphs: Optional[List[str]] = field(default_factory=list)
    num_paragraphs: int = 0

    def __set_item__(self, key, value):
        super().__setattr__(key, value)
        if key == "paragraphs":
            self.num_paragraphs = len(value)

