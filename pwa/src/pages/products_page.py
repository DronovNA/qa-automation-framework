"""Products page object for PWA demo."""

from playwright.async_api import Page

from pwa.src.base.base_page import BasePage
from pwa.src.utils.logger import get_logger

logger = get_logger(__name__)


class ProductsPage(BasePage):
    """Page object for products listing page."""

    # Selectors
    PRODUCTS_GRID = ".products-grid"
    PRODUCT_CARD = ".product-card"
    PRODUCT_TITLE = ".product-title"
    PRODUCT_DESCRIPTION = ".product-description"
    PRODUCT_PRICE = ".product-price"
    ADD_TO_CART = "button[data-action='add-to-cart']"
    FILTER_BUTTON = "button:has-text('Filter')"
    SORT_DROPDOWN = "select[name='sort']"
    LOADING_SPINNER = ".spinner"

    async def wait_for_page_load(self) -> None:
        """Wait for products page to load."""
        logger.info("Waiting for products page to load")
        await self.wait.wait_for_selector_hidden(self.LOADING_SPINNER, timeout=30000)
        await self.wait.wait_for_selector_visible(self.PRODUCTS_GRID, timeout=10000)
        logger.info("Products page loaded")

    async def get_product_count(self) -> int:
        """Get number of products on page.

        Returns:
            Number of products.
        """
        logger.info("Getting product count")
        count = await self.page.locator(self.PRODUCT_CARD).count()
        logger.debug(f"Products found: {count}")
        return count

    async def get_product_titles(self) -> list:
        """Get list of all product titles.

        Returns:
            List of product titles.
        """
        logger.info("Getting all product titles")
        titles = await self.page.locator(self.PRODUCT_TITLE).all_text_contents()
        logger.debug(f"Found {len(titles)} product titles")
        return titles

    async def add_product_to_cart(self, index: int) -> None:
        """Add product at specific index to cart.

        Args:
            index: Product index (0-based).
        """
        logger.info(f"Adding product at index {index} to cart")
        product = self.page.locator(self.PRODUCT_CARD).nth(index)
        await product.locator(self.ADD_TO_CART).click()
        logger.info("Product added to cart")

    async def sort_by(self, sort_option: str) -> None:
        """Sort products by option.

        Args:
            sort_option: Sort option value.
        """
        logger.info(f"Sorting products by {sort_option}")
        await self.page.select_option(self.SORT_DROPDOWN, sort_option)
        await self.wait.wait_for_navigation(timeout=30000)
        logger.info("Products sorted")
