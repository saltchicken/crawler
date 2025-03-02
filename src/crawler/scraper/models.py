from dataclasses import dataclass
from typing import Optional, List

@dataclass
class PageContent:
    title: Optional[str] = None
    headings: Optional[List[str]] = None
