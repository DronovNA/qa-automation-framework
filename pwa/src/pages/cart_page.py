"""Cart page object for PWA demo."""

from playwright.async_api import Page

from pwa.src.base.base_page import BasePage
from pwa.src.utils.logger import get_logger

logger = get_logger(__name__)


class CartPage(BasePage):
    """Page object for shopping cart page."""

    # Selectors
    CART_ITEMS = ".cart-item"
    ITEM_PRICE = ".item-price"
    ITEM_QUANTITY = "input[type='number']"
    REMOVE_BUTTON = "button[data-action='remove']"
    TOTAL_PRICE = ".total-price"
    CHECKOUT_BUTTON = "button:has-text('Checkout')"
    EMPTY_CART_MESSAGE = ".empty-cart-message"
    QUANTITY_INCREASE = "button[data-action='increase']"
    QUANTITY_DECREASE = "button[data-action='decrease']"

    async def wait_for_page_load(self) -> None:
        """Wait for cart page to load."""
        logger.info("Waiting for cart page to load")
        await self.page.wait_for_load_state("networkidle")
        logger.info("Cart page loaded")

    async def get_cart_items_count(self) -> int:
        """Get number of items in cart.

        Returns:
            Number of items in cart.
        """
        logger.info("Getting cart items count")
        count = await self.page.locator(self.CART_ITEMS).count()
        logger.debug(f"Items in cart: {count}")
        return count

    async def is_cart_empty(self) -> bool:
        """Check if cart is empty.

        Returns:
            True if cart is empty.
        """
        logger.info("Checking if cart is empty")
        is_visible = await self.is_element_visible(self.EMPTY_CART_MESSAGE)
        logger.debug(f"Cart empty: {is_visible}")
        return is_visible

    async def get_total_price(self) -> str:
        """Get total cart price.

        Returns:
            Total price text.
        """
        logger.info("Getting total price")
        total = await self.get_text(self.TOTAL_PRICE)
        logger.debug(f"Total price: {total}")
        return total

    async def remove_item(self, index: int) -> None:
        """Remove item from cart.

        Args:
            index: Item index (0-based).
        """
        logger.info(f"Removing item at index {index}")
        item = self.page.locator(self.CART_ITEMS).nth(index)
        await item.locator(self.REMOVE_BUTTON).click()
        logger.info("Item removed")

    async def increase_item_quantity(self, index: int) -> None:
        """Increase item quantity.

        Args:
            index: Item index (0-based).
        """
        logger.info(f"Increasing quantity for item at index {index}")
        item = self.page.locator(self.CART_ITEMS).nth(index)
        await item.locator(self.QUANTITY_INCREASE).click()
        logger.info("Quantity increased")

    async def click_checkout_button(self) -> None:
        """Click checkout button."""
        logger.info("Clicking checkout button")
        await self.click(self.CHECKOUT_BUTTON)
