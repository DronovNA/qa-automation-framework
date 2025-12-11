"""Manager for Appium driver lifecycle."""

from typing import Optional

from appium import webdriver

from mobile.src.driver.driver_factory import DriverFactory
from mobile.src.utils.logger import get_logger

logger = get_logger(__name__)


class DriverManager:
    """Manager for driver lifecycle in tests."""

    _instance: Optional["DriverManager"] = None
    _driver: Optional[webdriver.WebDriver] = None

    def __new__(cls) -> "DriverManager":
        """Implement singleton pattern for driver management."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def init_driver(self) -> webdriver.WebDriver:
        """Initialize driver for test.

        Returns:
            Appium WebDriver instance.
        """
        logger.info("Initializing driver for test")
        self._driver = DriverFactory.create_driver()
        return self._driver

    def get_driver(self) -> webdriver.WebDriver:
        """Get current driver instance.

        Returns:
            Current driver instance.

        Raises:
            RuntimeError: If driver is not initialized.
        """
        if self._driver is None:
            raise RuntimeError("Driver not initialized. Call init_driver() first.")
        return self._driver

    def close_driver(self) -> None:
        """Close driver after test."""
        logger.info("Closing driver after test")
        DriverFactory.quit_driver()
        self._driver = None

    def reset(self) -> None:
        """Reset driver state."""
        logger.info("Resetting driver state")
        if self._driver:
            try:
                self._driver.reset()
                logger.info("Driver reset successfully")
            except Exception as e:
                logger.warning(f"Error resetting driver: {str(e)}")

    @classmethod
    def reset_singleton(cls) -> None:
        """Reset singleton instance (for testing purposes)."""
        cls._instance = None
