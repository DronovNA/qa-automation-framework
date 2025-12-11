"""Wait strategies and handlers for element interactions."""

from typing import Callable, TypeVar, Optional
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from mobile.src.utils.logger import get_logger

logger = get_logger(__name__)

T = TypeVar("T")


class WaitHandler:
    """Handles wait strategies and synchronization for mobile tests."""

    DEFAULT_TIMEOUT = 10
    DEFAULT_POLL_FREQUENCY = 0.5

    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Initialize WaitHandler.

        Args:
            driver: Appium WebDriver instance.
            timeout: Maximum wait time in seconds.
        """
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout, self.DEFAULT_POLL_FREQUENCY)

    def wait_for_element_visible(
        self, locator: tuple, timeout: Optional[int] = None
    ) -> webdriver.WebElement:
        """Wait for element to be visible.

        Args:
            locator: Tuple of (By, value) for element locator.
            timeout: Optional timeout override.

        Returns:
            WebElement when it becomes visible.

        Raises:
            TimeoutException: If element not visible within timeout.
        """
        actual_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, actual_timeout)
        logger.debug(f"Waiting for element {locator} to be visible (timeout: {actual_timeout}s)")
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(
        self, locator: tuple, timeout: Optional[int] = None
    ) -> webdriver.WebElement:
        """Wait for element to be clickable.

        Args:
            locator: Tuple of (By, value) for element locator.
            timeout: Optional timeout override.

        Returns:
            WebElement when it becomes clickable.
        """
        actual_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, actual_timeout)
        logger.debug(f"Waiting for element {locator} to be clickable (timeout: {actual_timeout}s)")
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_presence(
        self, locator: tuple, timeout: Optional[int] = None
    ) -> webdriver.WebElement:
        """Wait for element to be present in DOM.

        Args:
            locator: Tuple of (By, value) for element locator.
            timeout: Optional timeout override.

        Returns:
            WebElement when it is present in DOM.
        """
        actual_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, actual_timeout)
        logger.debug(f"Waiting for element {locator} to be present (timeout: {actual_timeout}s)")
        return wait.until(EC.presence_of_element_located(locator))

    def wait_for_text_in_element(
        self, locator: tuple, text: str, timeout: Optional[int] = None
    ) -> bool:
        """Wait for text to appear in element.

        Args:
            locator: Tuple of (By, value) for element locator.
            text: Text to wait for.
            timeout: Optional timeout override.

        Returns:
            True when text is found in element.
        """
        actual_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, actual_timeout)
        logger.debug(f"Waiting for text '{text}' in element {locator}")
        return wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_for_condition(
        self, condition: Callable[..., T], timeout: Optional[int] = None
    ) -> T:
        """Wait for custom condition to be true.

        Args:
            condition: Callable that returns True when condition is met.
            timeout: Optional timeout override.

        Returns:
            Result of the condition callable.
        """
        actual_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, actual_timeout)
        logger.debug(f"Waiting for custom condition (timeout: {actual_timeout}s)")
        return wait.until(condition)
