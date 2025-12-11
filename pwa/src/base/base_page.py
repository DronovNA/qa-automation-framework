"""Base Page Object class for all PWA pages."""

from typing import Optional, List
from playwright.async_api import Page, Locator

from pwa.src.base.wait_handler import WaitHandler
from pwa.src.utils.logger import get_logger
from pwa.src.utils.screenshot import ScreenshotHandler

logger = get_logger(__name__)


class BasePage:
    """Base class for all page objects in PWA testing framework.

    Provides common functionality for page interaction, element location,
    waiting, and logging.
    """

    def __init__(self, page: Page) -> None:
        """Initialize BasePage.

        Args:
            page: Playwright Page instance.
        """
        self.page = page
        self.wait = WaitHandler(page)
        self.screenshot = ScreenshotHandler(page)
        logger.debug(f"Initializing page: {self.__class__.__name__}")

    def find_element(self, selector: str) -> Locator:
        """Find element by selector.

        Args:
            selector: CSS selector or XPath.

        Returns:
            Locator instance.
        """
        logger.debug(f"Finding element: {selector}")
        return self.page.locator(selector)

    async def click(self, selector: str) -> None:
        """Click element.

        Args:
            selector: CSS selector or XPath.
        """
        logger.info(f"Clicking element: {selector}")
        await self.page.click(selector)

    async def fill(self, selector: str, text: str) -> None:
        """Fill text input element.

        Args:
            selector: CSS selector or XPath.
            text: Text to fill.
        """
        logger.info(f"Filling text in {selector}: {text}")
        await self.page.fill(selector, text)

    async def get_text(self, selector: str) -> str:
        """Get text from element.

        Args:
            selector: CSS selector or XPath.

        Returns:
            Text content of element.
        """
        logger.info(f"Getting text from element: {selector}")
        text = await self.page.text_content(selector)
        logger.debug(f"Element text: {text}")
        return text or ""

    async def is_element_visible(self, selector: str) -> bool:
        """Check if element is visible.

        Args:
            selector: CSS selector or XPath.

        Returns:
            True if element is visible, False otherwise.
        """
        try:
            is_visible = await self.page.is_visible(selector)
            logger.debug(f"Element {selector} visible: {is_visible}")
            return is_visible
        except Exception as e:
            logger.debug(f"Element {selector} not visible: {str(e)}")
            return False

    async def is_element_enabled(self, selector: str) -> bool:
        """Check if element is enabled.

        Args:
            selector: CSS selector or XPath.

        Returns:
            True if element is enabled, False otherwise.
        """
        try:
            is_enabled = await self.page.is_enabled(selector)
            logger.debug(f"Element {selector} enabled: {is_enabled}")
            return is_enabled
        except Exception as e:
            logger.debug(f"Element {selector} not enabled: {str(e)}")
            return False

    async def scroll_to_element(self, selector: str) -> None:
        """Scroll to element.

        Args:
            selector: CSS selector or XPath.
        """
        logger.info(f"Scrolling to element: {selector}")
        await self.page.locator(selector).scroll_into_view_if_needed()

    async def get_attribute(self, selector: str, attribute: str) -> Optional[str]:
        """Get element attribute value.

        Args:
            selector: CSS selector or XPath.
            attribute: Attribute name.

        Returns:
            Attribute value or None.
        """
        logger.debug(f"Getting attribute '{attribute}' from element {selector}")
        return await self.page.get_attribute(selector, attribute)

    async def wait_for_page_load(self) -> None:
        """Wait for page to load. Override in subclasses.

        This method should be overridden in page object subclasses
        to verify page-specific elements are visible.
        """
        logger.debug(f"Waiting for {self.__class__.__name__} to load")
        await self.page.wait_for_load_state("networkidle")
