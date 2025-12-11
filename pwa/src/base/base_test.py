"""Base Test class for all PWA tests."""

import pytest
from playwright.async_api import Page

from pwa.src.browser.browser_manager import BrowserManager
from pwa.src.utils.logger import get_logger
from pwa.src.utils.screenshot import ScreenshotHandler

logger = get_logger(__name__)


class BaseTest:
    """Base class for all PWA tests.

    Provides browser management, setup/teardown, and common test utilities.
    """

    @pytest.fixture(autouse=True)
    async def setup_and_teardown(self) -> None:
        """Setup and teardown for each test."""
        # Setup
        logger.info(f"\n{'='*60}")
        logger.info(f"Starting test: {self.__class__.__name__}")
        logger.info(f"{'='*60}")

        self.browser_manager = BrowserManager()
        self.page: Page = await self.browser_manager.init_browser()
        self.screenshot = ScreenshotHandler(self.page)

        yield

        # Teardown
        logger.info(f"\n{'='*60}")
        logger.info(f"Finishing test: {self.__class__.__name__}")
        logger.info(f"{'='*60}\n")

        await self.browser_manager.close_browser()

    async def take_screenshot(self, name: str = "screenshot") -> None:
        """Take screenshot during test.

        Args:
            name: Name for screenshot file.
        """
        logger.info(f"Taking screenshot: {name}")
        await self.screenshot.take_screenshot(name)
