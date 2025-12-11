"""Test cases for Wikipedia search functionality."""

import pytest
from appium import webdriver

from mobile.src.base.base_test import BaseTest
from mobile.src.pages.home_page import HomePage
from mobile.src.pages.search_page import SearchPage
from mobile.src.pages.article_page import ArticlePage
from mobile.src.utils.assertions import CustomAssertions
from mobile.src.utils.logger import get_logger

logger = get_logger(__name__)


class TestSearch(BaseTest):
    """Test cases for search functionality."""

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_search_valid_query(self, test_data) -> None:
        """Test searching with valid query.

        Verifies that:
        - Search box is accessible
        - Search returns results
        - Results are displayed correctly
        """
        logger.info("Starting: test_search_valid_query")

        home_page = HomePage(self.driver)
        home_page.wait_for_page_load()
        home_page.click_search_box()

        search_page = SearchPage(self.driver)
        search_page.wait_for_page_load()

        search_query = "Python programming"
        search_page.enter_search_query(search_query)
        search_page.wait_for_search_results(timeout=15)

        results_count = search_page.get_search_results_count()
        CustomAssertions.assert_true(
            results_count > 0,
            f"Expected search results for query '{search_query}'"
        )
        logger.info(f"Found {results_count} search results")

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_search_empty_query(self) -> None:
        """Test searching with empty query.

        Verifies that:
        - Empty query doesn't cause errors
        - App handles empty input gracefully
        """
        logger.info("Starting: test_search_empty_query")

        home_page = HomePage(self.driver)
        home_page.wait_for_page_load()
        home_page.click_search_box()

        search_page = SearchPage(self.driver)
        search_page.wait_for_page_load()

        search_page.enter_search_query("")
        logger.info("Entered empty search query")
        self.take_screenshot("empty_search")

    @pytest.mark.regression
    def test_search_special_characters(self) -> None:
        """Test search with special characters.

        Verifies that:
        - Special characters are handled properly
        - Search doesn't crash with special input
        """
        logger.info("Starting: test_search_special_characters")

        home_page = HomePage(self.driver)
        home_page.wait_for_page_load()
        home_page.click_search_box()

        search_page = SearchPage(self.driver)
        search_page.wait_for_page_load()

        special_query = "C++ programming"
        search_page.enter_search_query(special_query)
        search_page.wait_for_search_results(timeout=15)

        results_count = search_page.get_search_results_count()
        CustomAssertions.assert_true(
            results_count > 0,
            f"Expected search results for query with special characters '{special_query}'"
        )

    @pytest.mark.regression
    def test_search_clear_functionality(self) -> None:
        """Test clearing search query.

        Verifies that:
        - Clear button works correctly
        - Search box is cleared after clicking clear
        """
        logger.info("Starting: test_search_clear_functionality")

        home_page = HomePage(self.driver)
        home_page.wait_for_page_load()
        home_page.click_search_box()

        search_page = SearchPage(self.driver)
        search_page.wait_for_page_load()

        search_query = "Python"
        search_page.enter_search_query(search_query)
        search_page.wait_for_search_results(timeout=10)

        logger.info("Clearing search")
        search_page.clear_search()
        self.take_screenshot("search_cleared")

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_search_result_click(self) -> None:
        """Test clicking on search result.

        Verifies that:
        - Clicking result navigates to article
        - Article page loads correctly
        """
        logger.info("Starting: test_search_result_click")

        home_page = HomePage(self.driver)
        home_page.wait_for_page_load()
        home_page.click_search_box()

        search_page = SearchPage(self.driver)
        search_page.wait_for_page_load()

        search_page.enter_search_query("Python programming")
        search_page.wait_for_search_results(timeout=15)

        first_result_title = search_page.get_first_result_title()
        logger.info(f"First result title: {first_result_title}")
        CustomAssertions.assert_not_none(first_result_title)

        search_page.click_first_result()
        article_page = ArticlePage(self.driver)
        article_page.wait_for_page_load()

        article_title = article_page.get_article_title()
        CustomAssertions.assert_not_none(article_title)
        logger.info(f"Article loaded: {article_title}")
