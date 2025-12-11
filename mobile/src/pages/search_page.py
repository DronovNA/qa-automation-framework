"""Search page object for Wikipedia mobile app."""

from typing import List
from selenium.webdriver.common.by import By

from mobile.src.base.base_page import BasePage
from mobile.src.utils.logger import get_logger

logger = get_logger(__name__)


class SearchPage(BasePage):
    """Page object for Wikipedia search functionality."""

    # Locators
    SEARCH_INPUT = (By.ID, "org.wikipedia:id/search_src_text")
    SEARCH_RESULTS = (By.XPATH, "//android.widget.LinearLayout[@resource-id='org.wikipedia:id/page_list_item_container']")
    RESULT_TITLE = (By.ID, "org.wikipedia:id/page_list_item_title")
    RESULT_DESCRIPTION = (By.ID, "org.wikipedia:id/page_list_item_description")
    NO_RESULTS_TEXT = (By.XPATH, "//android.widget.TextView[contains(@text, 'No results')]")
    CLEAR_SEARCH_BUTTON = (By.XPATH, "//android.widget.ImageView[@resource-id='org.wikipedia:id/search_close_btn']")

    def wait_for_page_load(self) -> None:
        """Wait for search page to load."""
        logger.info("Waiting for search page to load")
        self.wait.wait_for_element_visible(self.SEARCH_INPUT, timeout=10)
        logger.info("Search page loaded")

    def enter_search_query(self, query: str) -> None:
        """Enter search query in search box.

        Args:
            query: Search query string.
        """
        logger.info(f"Entering search query: {query}")
        self.send_keys(self.SEARCH_INPUT, query)

    def wait_for_search_results(self, timeout: int = 10) -> None:
        """Wait for search results to appear.

        Args:
            timeout: Maximum wait time in seconds.
        """
        logger.info(f"Waiting for search results (timeout: {timeout}s)")
        self.wait.wait_for_element_visible(self.SEARCH_RESULTS, timeout=timeout)

    def get_search_results_count(self) -> int:
        """Get number of search results displayed.

        Returns:
            Number of search results.
        """
        results = self.find_elements(self.SEARCH_RESULTS)
        logger.info(f"Search results count: {len(results)}")
        return len(results)

    def get_first_result_title(self) -> str:
        """Get title of first search result.

        Returns:
            Title of first search result.
        """
        logger.info("Getting first search result title")
        return self.get_text(self.RESULT_TITLE)

    def click_first_result(self) -> None:
        """Click first search result."""
        logger.info("Clicking first search result")
        first_result = self.find_elements(self.SEARCH_RESULTS)[0]
        first_result.click()

    def is_no_results_displayed(self) -> bool:
        """Check if no results message is displayed.

        Returns:
            True if no results message is visible.
        """
        return self.is_element_displayed(self.NO_RESULTS_TEXT)

    def clear_search(self) -> None:
        """Clear search box."""
        logger.info("Clearing search")
        self.click(self.CLEAR_SEARCH_BUTTON)
