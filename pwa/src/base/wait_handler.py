"""Wait strategies and handlers for PWA element interactions."""

from typing import Callable, TypeVar, Optional
from playwright.async_api import Page, Locator

from pwa.config.settings import settings
from pwa.src.utils.logger import get_logger

logger = get_logger(__name__)

T = TypeVar("T")


class WaitHandler:
    """Handles wait strategies and synchronization for PWA tests."""

    def __init__(self, page: Page) -> None:
        """Initialize WaitHandler.

        Args:
            page: Playwright Page instance.
        """
        self.page = page
        self.timeout = settings.playwright_timeout

    async def wait_for_selector_visible(
        self, selector: str, timeout: Optional[int] = None
    ) -> Locator:
        """Wait for element to be visible.

        Args:
            selector: CSS selector or XPath.
            timeout: Optional timeout override in milliseconds.

        Returns:
            Locator when element becomes visible.
        """
        actual_timeout = timeout or self.timeout
        logger.debug(f"Waiting for selector '{selector}' to be visible (timeout: {actual_timeout}ms)")
        await self.page.wait_for_selector(selector, state="visible", timeout=actual_timeout)
        return self.page.locator(selector)

    async def wait_for_selector_hidden(
        self, selector: str, timeout: Optional[int] = None
    ) -> None:
        """Wait for element to be hidden.

        Args:
            selector: CSS selector or XPath.
            timeout: Optional timeout override in milliseconds.
        """
        actual_timeout = timeout or self.timeout
        logger.debug(f"Waiting for selector '{selector}' to be hidden (timeout: {actual_timeout}ms)")
        await self.page.wait_for_selector(selector, state="hidden", timeout=actual_timeout)

    async def wait_for_text(
        self, selector: str, text: str, timeout: Optional[int] = None
    ) -> None:
        """Wait for text to appear in element.

        Args:
            selector: CSS selector or XPath.
            text: Text to wait for.
            timeout: Optional timeout override in milliseconds.
        """
        actual_timeout = timeout or self.timeout
        logger.debug(f"Waiting for text '{text}' in selector '{selector}'")
        locator = self.page.locator(selector)
        await locator.wait_for(timeout=actual_timeout)
        await self.page.wait_for_function(
            f"() => document.querySelector('{selector}').textContent.includes('{text}')",
            timeout=actual_timeout
        )

    async def wait_for_navigation(self, timeout: Optional[int] = None) -> None:
        """Wait for page navigation to complete.

        Args:
            timeout: Optional timeout override in milliseconds.
        """
        actual_timeout = timeout or self.timeout
        logger.debug(f"Waiting for navigation (timeout: {actual_timeout}ms)")
        await self.page.wait_for_load_state("networkidle", timeout=actual_timeout)
