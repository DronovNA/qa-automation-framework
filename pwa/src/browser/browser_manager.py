"""Manager for Playwright browser lifecycle."""

from typing import Optional
from playwright.async_api import Browser, BrowserContext, Page

from pwa.src.browser.browser_factory import BrowserFactory
from pwa.config.settings import settings
from pwa.src.utils.logger import get_logger

logger = get_logger(__name__)


class BrowserManager:
    """Manager for browser lifecycle in PWA tests."""

    _instance: Optional["BrowserManager"] = None
    _browser: Optional[Browser] = None
    _context: Optional[BrowserContext] = None
    _page: Optional[Page] = None

    def __new__(cls) -> "BrowserManager":
        """Implement singleton pattern for browser management."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def init_browser(self) -> Page:
        """Initialize browser for test.

        Returns:
            Page instance ready for testing.
        """
        logger.info("Initializing browser for test")
        self._browser = await BrowserFactory.create_browser()
        self._context = await BrowserFactory.create_context(self._browser)
        self._page = await BrowserFactory.create_page(self._context)
        await self._page.goto(settings.pwa_base_url)
        logger.info(f"Navigated to {settings.pwa_base_url}")
        return self._page

    def get_page(self) -> Page:
        """Get current page instance.

        Returns:
            Current page instance.

        Raises:
            RuntimeError: If page is not initialized.
        """
        if self._page is None:
            raise RuntimeError("Page not initialized. Call init_browser() first.")
        return self._page

    async def close_browser(self) -> None:
        """Close browser after test."""
        logger.info("Closing browser after test")
        await BrowserFactory.close_browser()
        self._page = None
        self._context = None
        self._browser = None

    @classmethod
    def reset_singleton(cls) -> None:
        """Reset singleton instance (for testing purposes)."""
        cls._instance = None
