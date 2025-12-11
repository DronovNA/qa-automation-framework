"""Home page object for Wikipedia mobile app."""

from selenium.webdriver.common.by import By

from mobile.src.base.base_page import BasePage
from mobile.src.utils.logger import get_logger

logger = get_logger(__name__)


class HomePage(BasePage):
    """Page object for Wikipedia home page."""

    # Locators
    SEARCH_BOX = (By.ID, "org.wikipedia:id/search_container")
    MENU_BUTTON = (By.ID, "org.wikipedia:id/menu_overflow_button")
    SETTINGS_BUTTON = (By.ID, "org.wikipedia:id/menu_overflow_button")
    LANGUAGE_BUTTON = (By.ID, "org.wikipedia:id/main_drawer_lang_button")
    HISTORY_LINK = (By.XPATH, "//android.widget.FrameLayout[@resource-id='org.wikipedia:id/history_tab']")
    SAVED_LINK = (By.XPATH, "//android.widget.FrameLayout[@resource-id='org.wikipedia:id/saved_tab']")

    def wait_for_page_load(self) -> None:
        """Wait for home page to fully load."""
        logger.info("Waiting for home page to load")
        self.wait.wait_for_element_visible(self.SEARCH_BOX, timeout=15)
        logger.info("Home page loaded successfully")

    def click_search_box(self) -> None:
        """Click on search box to open search."""
        logger.info("Clicking search box")
        self.click(self.SEARCH_BOX)

    def is_search_box_visible(self) -> bool:
        """Check if search box is visible."""
        return self.is_element_displayed(self.SEARCH_BOX)

    def click_menu_button(self) -> None:
        """Click overflow menu button."""
        logger.info("Clicking menu button")
        self.click(self.MENU_BUTTON)

    def click_language_button(self) -> None:
        """Click language selection button."""
        logger.info("Clicking language button")
        self.click(self.LANGUAGE_BUTTON)

    def click_history_tab(self) -> None:
        """Click history tab."""
        logger.info("Clicking history tab")
        self.click(self.HISTORY_LINK)

    def click_saved_tab(self) -> None:
        """Click saved articles tab."""
        logger.info("Clicking saved tab")
        self.click(self.SAVED_LINK)
