"""Data models for Wikipedia search tests."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class SearchQuery:
    """Model for search query."""

    query: str
    expected_results_min: int = 1
    expected_title: Optional[str] = None
    description: Optional[str] = None


@dataclass
class Article:
    """Model for Wikipedia article."""

    title: str
    description: Optional[str] = None
    language: str = "English"
    is_saved: bool = False
