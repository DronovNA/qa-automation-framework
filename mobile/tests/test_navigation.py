"""Test cases for Wikipedia app navigation."""

import pytest

from mobile.src.base.base_test import BaseTest
from mobile.src.pages.home_page import HomePage
from mobile.src.pages.search_page import SearchPage
from mobile.src.pages.article_page import ArticlePage
from mobile.src.utils.assertions import CustomAssertions
from mobile.src.utils.logger import get_logger

logger = get_logger(__name__)


class TestNavigation(BaseTest):
    """Test cases for app navigation."""

    @pytest.mark.smoke
    def test_home_page_loads(self) -> None:
        """Test that home page loads successfully.

        Verifies that:
        - Home page appears on app launch
        - Search box is visible
        - App is ready for interaction
        """
        logger.info("Starting: test_home_page_loads")

        home_page = HomePage(self.driver)
        home_page.wait_for_page_load()

        CustomAssertions.assert_true(
            home_page.is_search_box_visible(),
            "Search box should be visible on home page"
        )
        logger.info("Home page loaded successfully")
        self.take_screenshot("home_page")

    @pytest.mark.regression
    def test_back_button_navigation(self) -> None:
        """Test back button navigation.

        Verifies that:
        - Back button returns to previous page
        - Navigation history works correctly
        """
        logger.info("Starting: test_back_button_navigation")

        home_page = HomePage(self.driver)
        home_page.wait_for_page_load()
        home_page.click_search_box()

        search_page = SearchPage(self.driver)
        search_page.wait_for_page_load()
        search_page.enter_search_query("Python")
        search_page.wait_for_search_results(timeout=15)
        search_page.click_first_result()

        article_page = ArticlePage(self.driver)
        article_page.wait_for_page_load()
        logger.info("Article page opened")

        article_page.click_back_button()
        logger.info("Clicked back button")
        self.take_screenshot("after_back_button")

    @pytest.mark.regression
    def test_search_to_article_flow(self) -> None:
        """Test complete flow from search to article.

        Verifies that:
        - User can search from home page
        - User can view search results
        - User can open article from results
        - Article page displays correctly
        """
        logger.info("Starting: test_search_to_article_flow")

        # Home page
        home_page = HomePage(self.driver)
        home_page.wait_for_page_load()
        self.take_screenshot("step_1_home")

        # Search page
        home_page.click_search_box()
        search_page = SearchPage(self.driver)
        search_page.wait_for_page_load()
        self.take_screenshot("step_2_search_opened")

        # Enter search
        search_page.enter_search_query("Artificial Intelligence")
        search_page.wait_for_search_results(timeout=15)
        results_count = search_page.get_search_results_count()
        CustomAssertions.assert_true(results_count > 0)
        self.take_screenshot("step_3_search_results")

        # Click result
        search_page.click_first_result()
        article_page = ArticlePage(self.driver)
        article_page.wait_for_page_load()
        self.take_screenshot("step_4_article_opened")

        # Verify article
        CustomAssertions.assert_true(article_page.is_article_content_visible())
        article_title = article_page.get_article_title()
        CustomAssertions.assert_not_none(article_title)
        logger.info(f"Complete flow successful. Article: {article_title}")
