"""Base Test class for all mobile tests."""

import pytest
from appium.webdriver.webdriver import WebDriver

from mobile.src.driver.driver_manager import DriverManager
from mobile.src.utils.logger import get_logger
from mobile.src.utils.screenshot import ScreenshotHandler
from mobile.config.settings import settings

logger = get_logger(__name__)


class BaseTest:
    """Base class for all mobile tests.

    Provides driver management, setup/teardown, and common test utilities.
    """

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self) -> None:
        """Setup and teardown for each test."""
        # Setup
        logger.info(f"\n{'='*60}")
        logger.info(f"Starting test: {self.__class__.__name__}")
        logger.info(f"{'='*60}")

        self.driver_manager = DriverManager()
        self.driver: WebDriver = self.driver_manager.init_driver()
        self.screenshot = ScreenshotHandler(self.driver)

        yield

        # Teardown
        logger.info(f"\n{'='*60}")
        logger.info(f"Finishing test: {self.__class__.__name__}")
        logger.info(f"{'='*60}\n")

        self.driver_manager.close_driver()

    def take_screenshot(self, name: str = "screenshot") -> None:
        """Take screenshot during test.

        Args:
            name: Name for screenshot file.
        """
        logger.info(f"Taking screenshot: {name}")
        self.screenshot.take_screenshot(name)
