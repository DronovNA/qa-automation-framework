"""Home page object for Swapy PWA demo."""

from playwright.async_api import Page

from pwa.src.base.base_page import BasePage
from pwa.src.utils.logger import get_logger

logger = get_logger(__name__)


class HomePage(BasePage):
    """Page object for Swapy home page."""

    # Selectors
    PRODUCTS_HEADING = "h1"
    PRODUCT_ITEM = ".product-item"
    PRODUCT_NAME = ".product-name"
    PRODUCT_PRICE = ".product-price"
    ADD_TO_CART_BUTTON = "button:has-text('Add to Cart')"
    CART_BUTTON = "a:has-text('Cart')"
    NAVBAR = "nav"

    async def wait_for_page_load(self) -> None:
        """Wait for home page to fully load."""
        logger.info("Waiting for home page to load")
        await self.wait.wait_for_selector_visible(self.PRODUCTS_HEADING, timeout=30000)
        logger.info("Home page loaded successfully")

    async def get_product_count(self) -> int:
        """Get number of products displayed.

        Returns:
            Number of products on page.
        """
        logger.info("Getting product count")
        count = await self.page.locator(self.PRODUCT_ITEM).count()
        logger.debug(f"Found {count} products")
        return count

    async def get_first_product_name(self) -> str:
        """Get name of first product.

        Returns:
            First product name.
        """
        logger.info("Getting first product name")
        first_product = self.page.locator(self.PRODUCT_ITEM).first
        name = await first_product.locator(self.PRODUCT_NAME).text_content()
        return name or ""

    async def get_first_product_price(self) -> str:
        """Get price of first product.

        Returns:
            First product price.
        """
        logger.info("Getting first product price")
        first_product = self.page.locator(self.PRODUCT_ITEM).first
        price = await first_product.locator(self.PRODUCT_PRICE).text_content()
        return price or ""

    async def add_first_product_to_cart(self) -> None:
        """Add first product to cart."""
        logger.info("Adding first product to cart")
        first_product = self.page.locator(self.PRODUCT_ITEM).first
        await first_product.locator(self.ADD_TO_CART_BUTTON).click()
        logger.info("Product added to cart")

    async def click_cart_button(self) -> None:
        """Click cart button to navigate to cart."""
        logger.info("Clicking cart button")
        await self.click(self.CART_BUTTON)
