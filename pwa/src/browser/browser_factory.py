"""Factory for creating and managing Playwright browser instances."""

from typing import Optional
from playwright.async_api import async_playwright, Browser, BrowserContext, Page

from pwa.config.browser_config import BrowserConfig
from pwa.config.settings import settings
from pwa.src.utils.logger import get_logger

logger = get_logger(__name__)


class BrowserFactory:
    """Factory class for creating Playwright browser instances."""

    _browser: Optional[Browser] = None
    _context: Optional[BrowserContext] = None
    _page: Optional[Page] = None
    _playwright = None

    @classmethod
    async def create_browser(cls) -> Browser:
        """Create and return Playwright browser.

        Returns:
            Playwright Browser instance.

        Raises:
            Exception: If browser creation fails.
        """
        if cls._browser is not None:
            logger.warning("Browser already exists, returning existing instance")
            return cls._browser

        try:
            logger.info(f"Creating {settings.browser_type} browser")

            cls._playwright = await async_playwright().start()
            browser_launcher = getattr(cls._playwright, settings.browser_type)
            options = BrowserConfig.get_browser_options()
            logger.debug(f"Browser options: {options}")

            cls._browser = await browser_launcher.launch(**options)
            logger.info(f"{settings.browser_type} browser created successfully")
            return cls._browser

        except Exception as e:
            logger.error(f"Failed to create browser: {str(e)}")
            raise

    @classmethod
    async def create_context(cls, browser: Browser) -> BrowserContext:
        """Create browser context.

        Args:
            browser: Browser instance.

        Returns:
            Browser context.
        """
        try:
            logger.info("Creating browser context")
            options = BrowserConfig.get_context_options()
            cls._context = await browser.new_context(**options)
            logger.info("Browser context created successfully")
            return cls._context
        except Exception as e:
            logger.error(f"Failed to create context: {str(e)}")
            raise

    @classmethod
    async def create_page(cls, context: BrowserContext) -> Page:
        """Create page in context.

        Args:
            context: Browser context.

        Returns:
            Page instance.
        """
        try:
            logger.info("Creating page")
            page = await context.new_page()
            logger.info("Page created successfully")
            return page
        except Exception as e:
            logger.error(f"Failed to create page: {str(e)}")
            raise

    @classmethod
    async def close_browser(cls) -> None:
        """Close browser and cleanup resources."""
        try:
            if cls._page:
                logger.info("Closing page")
                await cls._page.close()
                cls._page = None

            if cls._context:
                logger.info("Closing context")
                await cls._context.close()
                cls._context = None

            if cls._browser:
                logger.info("Closing browser")
                await cls._browser.close()
                cls._browser = None

            if cls._playwright:
                logger.info("Stopping playwright")
                await cls._playwright.stop()
                cls._playwright = None

            logger.info("Browser closed successfully")
        except Exception as e:
            logger.error(f"Error closing browser: {str(e)}")

    @classmethod
    def get_page(cls) -> Optional[Page]:
        """Get current page instance.

        Returns:
            Current page instance or None.
        """
        return cls._page

    @classmethod
    async def set_page(cls, page: Page) -> None:
        """Set current page instance.

        Args:
            page: Page to set as current.
        """
        cls._page = page
