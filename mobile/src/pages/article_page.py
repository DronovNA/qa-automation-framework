"""Article page object for Wikipedia mobile app."""

from selenium.webdriver.common.by import By

from mobile.src.base.base_page import BasePage
from mobile.src.utils.logger import get_logger

logger = get_logger(__name__)


class ArticlePage(BasePage):
    """Page object for Wikipedia article page."""

    # Locators
    ARTICLE_TITLE = (By.ID, "org.wikipedia:id/page_title")
    ARTICLE_CONTENT = (By.ID, "org.wikipedia:id/page_web_view")
    SAVE_BUTTON = (By.ID, "org.wikipedia:id/page_save_button")
    SHARE_BUTTON = (By.ID, "org.wikipedia:id/page_share_button")
    LANGUAGE_BUTTON = (By.ID, "org.wikipedia:id/page_language_button")
    BACK_BUTTON = (By.ID, "org.wikipedia:id/icon_back")
    SEARCH_BUTTON = (By.ID, "org.wikipedia:id/search_container")
    TABLE_OF_CONTENTS = (By.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia:id/toc_item']")

    def wait_for_page_load(self) -> None:
        """Wait for article page to load."""
        logger.info("Waiting for article page to load")
        self.wait.wait_for_element_visible(self.ARTICLE_TITLE, timeout=15)
        logger.info("Article page loaded")

    def get_article_title(self) -> str:
        """Get title of current article.

        Returns:
            Article title text.
        """
        logger.info("Getting article title")
        return self.get_text(self.ARTICLE_TITLE)

    def is_article_content_visible(self) -> bool:
        """Check if article content is visible.

        Returns:
            True if article content is displayed.
        """
        return self.is_element_displayed(self.ARTICLE_CONTENT)

    def click_save_button(self) -> None:
        """Click save article button."""
        logger.info("Clicking save article button")
        self.click(self.SAVE_BUTTON)

    def click_share_button(self) -> None:
        """Click share article button."""
        logger.info("Clicking share button")
        self.click(self.SHARE_BUTTON)

    def click_language_button(self) -> None:
        """Click language selection button."""
        logger.info("Clicking language button")
        self.click(self.LANGUAGE_BUTTON)

    def click_back_button(self) -> None:
        """Click back button to return to previous page."""
        logger.info("Clicking back button")
        self.click(self.BACK_BUTTON)

    def scroll_down(self) -> None:
        """Scroll down article page."""
        logger.info("Scrolling down article")
        self.driver.swipe(540, 1000, 540, 400, 500)

    def scroll_up(self) -> None:
        """Scroll up article page."""
        logger.info("Scrolling up article")
        self.driver.swipe(540, 400, 540, 1000, 500)
