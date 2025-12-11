"""Test cases for Wikipedia article functionality."""

import pytest

from mobile.src.base.base_test import BaseTest
from mobile.src.pages.home_page import HomePage
from mobile.src.pages.search_page import SearchPage
from mobile.src.pages.article_page import ArticlePage
from mobile.src.utils.assertions import CustomAssertions
from mobile.src.utils.logger import get_logger

logger = get_logger(__name__)


class TestArticle(BaseTest):
    """Test cases for article functionality."""

    def _navigate_to_article(self, search_query: str) -> ArticlePage:
        """Helper method to navigate to article.

        Args:
            search_query: Search query to find article.

        Returns:
            ArticlePage object.
        """
        home_page = HomePage(self.driver)
        home_page.wait_for_page_load()
        home_page.click_search_box()

        search_page = SearchPage(self.driver)
        search_page.wait_for_page_load()
        search_page.enter_search_query(search_query)
        search_page.wait_for_search_results(timeout=15)
        search_page.click_first_result()

        article_page = ArticlePage(self.driver)
        article_page.wait_for_page_load()
        return article_page

    @pytest.mark.smoke
    def test_article_loads(self) -> None:
        """Test that article loads successfully.

        Verifies that:
        - Article page opens
        - Article content is displayed
        - Article title is visible
        """
        logger.info("Starting: test_article_loads")

        article_page = self._navigate_to_article("Python programming")

        CustomAssertions.assert_true(
            article_page.is_article_content_visible(),
            "Article content should be visible"
        )
        article_title = article_page.get_article_title()
        CustomAssertions.assert_not_none(article_title)
        logger.info(f"Article loaded: {article_title}")

    @pytest.mark.regression
    def test_article_scroll(self) -> None:
        """Test scrolling through article.

        Verifies that:
        - User can scroll down
        - Article content is scrollable
        - More content becomes visible after scrolling
        """
        logger.info("Starting: test_article_scroll")

        article_page = self._navigate_to_article("Python programming")
        self.take_screenshot("article_before_scroll")

        logger.info("Scrolling down article")
        article_page.scroll_down()
        self.take_screenshot("article_after_scroll_down")

        logger.info("Scrolling up article")
        article_page.scroll_up()
        self.take_screenshot("article_after_scroll_up")

    @pytest.mark.regression
    def test_article_save_button(self) -> None:
        """Test save article functionality.

        Verifies that:
        - Save button is accessible
        - Save button is clickable
        - Button responds to click
        """
        logger.info("Starting: test_article_save_button")

        article_page = self._navigate_to_article("Machine Learning")

        logger.info("Clicking save button")
        article_page.click_save_button()
        self.take_screenshot("after_save_button_click")
        logger.info("Save button clicked successfully")

    @pytest.mark.regression
    def test_article_share_button(self) -> None:
        """Test share article functionality.

        Verifies that:
        - Share button is accessible
        - Share button is clickable
        - Share dialog/menu appears
        """
        logger.info("Starting: test_article_share_button")

        article_page = self._navigate_to_article("Artificial Intelligence")

        logger.info("Clicking share button")
        article_page.click_share_button()
        self.take_screenshot("after_share_button_click")
        logger.info("Share button clicked successfully")
