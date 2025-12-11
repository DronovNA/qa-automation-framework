"""Base Page Object class for all mobile pages."""

from typing import Optional, List
from selenium.webdriver.common.by import By
from appium.webdriver.webdriver import WebDriver

from mobile.src.base.wait_handler import WaitHandler
from mobile.src.utils.logger import get_logger
from mobile.src.utils.screenshot import ScreenshotHandler

logger = get_logger(__name__)


class BasePage:
    """Base class for all page objects in mobile testing framework.

    Provides common functionality for page interaction, element location,
    waiting, and logging.
    """

    def __init__(self, driver: WebDriver) -> None:
        """Initialize BasePage.

        Args:
            driver: Appium WebDriver instance.
        """
        self.driver = driver
        self.wait = WaitHandler(driver)
        self.screenshot = ScreenshotHandler(driver)
        logger.debug(f"Initializing page: {self.__class__.__name__}")

    def find_element(self, locator: tuple) -> webdriver.WebElement:
        """Find single element by locator.

        Args:
            locator: Tuple of (By, value).

        Returns:
            WebElement if found.
        """
        logger.debug(f"Finding element: {locator}")
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple) -> List[webdriver.WebElement]:
        """Find multiple elements by locator.

        Args:
            locator: Tuple of (By, value).

        Returns:
            List of WebElements.
        """
        logger.debug(f"Finding elements: {locator}")
        return self.driver.find_elements(*locator)

    def click(self, locator: tuple) -> None:
        """Click element.

        Args:
            locator: Tuple of (By, value).
        """
        logger.info(f"Clicking element: {locator}")
        element = self.wait.wait_for_element_clickable(locator)
        element.click()

    def send_keys(self, locator: tuple, text: str) -> None:
        """Send text to element.

        Args:
            locator: Tuple of (By, value).
            text: Text to send.
        """
        logger.info(f"Sending keys to element {locator}: {text}")
        element = self.wait.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Get text from element.

        Args:
            locator: Tuple of (By, value).

        Returns:
            Text content of element.
        """
        logger.info(f"Getting text from element: {locator}")
        element = self.wait.wait_for_element_visible(locator)
        text = element.text
        logger.debug(f"Element text: {text}")
        return text

    def is_element_displayed(self, locator: tuple) -> bool:
        """Check if element is displayed.

        Args:
            locator: Tuple of (By, value).

        Returns:
            True if element is displayed, False otherwise.
        """
        try:
            element = self.find_element(locator)
            is_displayed = element.is_displayed()
            logger.debug(f"Element {locator} displayed: {is_displayed}")
            return is_displayed
        except Exception as e:
            logger.debug(f"Element {locator} not displayed: {str(e)}")
            return False

    def is_element_enabled(self, locator: tuple) -> bool:
        """Check if element is enabled.

        Args:
            locator: Tuple of (By, value).

        Returns:
            True if element is enabled, False otherwise.
        """
        try:
            element = self.find_element(locator)
            is_enabled = element.is_enabled()
            logger.debug(f"Element {locator} enabled: {is_enabled}")
            return is_enabled
        except Exception as e:
            logger.debug(f"Element {locator} not enabled: {str(e)}")
            return False

    def scroll_to_element(self, locator: tuple) -> None:
        """Scroll to element.

        Args:
            locator: Tuple of (By, value).
        """
        logger.info(f"Scrolling to element: {locator}")
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_attribute(self, locator: tuple, attribute: str) -> Optional[str]:
        """Get element attribute value.

        Args:
            locator: Tuple of (By, value).
            attribute: Attribute name.

        Returns:
            Attribute value or None.
        """
        logger.debug(f"Getting attribute '{attribute}' from element {locator}")
        element = self.find_element(locator)
        return element.get_attribute(attribute)

    def wait_for_page_load(self) -> None:
        """Wait for page to load. Override in subclasses.

        This method should be overridden in page object subclasses
        to verify page-specific elements are visible.
        """
        logger.debug(f"Waiting for {self.__class__.__name__} to load")
