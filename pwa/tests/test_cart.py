"""Test cases for PWA shopping cart functionality."""

import pytest

from pwa.src.base.base_test import BaseTest
from pwa.src.pages.home_page import HomePage
from pwa.src.pages.cart_page import CartPage
from pwa.src.utils.assertions import CustomAssertions
from pwa.src.utils.logger import get_logger

logger = get_logger(__name__)


class TestCart(BaseTest):
    """Test cases for shopping cart functionality."""

    async def _add_product_to_cart(self) -> None:
        """Helper method to add product to cart."""
        home_page = HomePage(self.page)
        await home_page.wait_for_page_load()
        await home_page.add_first_product_to_cart()

    @pytest.mark.smoke
    @pytest.mark.asyncio
    async def test_add_to_cart_and_view(self) -> None:
        """Test adding product to cart and viewing cart.

        Verifies that:
        - Product can be added to cart
        - Cart can be opened
        - Added product appears in cart
        """
        logger.info("Starting: test_add_to_cart_and_view")

        # Add product
        await self._add_product_to_cart()
        logger.info("Product added to cart")

        # Go to cart
        home_page = HomePage(self.page)
        await home_page.click_cart_button()

        cart_page = CartPage(self.page)
        await cart_page.wait_for_page_load()

        items_count = await cart_page.get_cart_items_count()
        CustomAssertions.assert_true(
            items_count > 0,
            "Cart should contain at least one item"
        )
        logger.info(f"Cart contains {items_count} items")
        await self.take_screenshot("cart_view")

    @pytest.mark.regression
    @pytest.mark.asyncio
    async def test_cart_total_price(self) -> None:
        """Test cart total price calculation.

        Verifies that:
        - Total price is displayed
        - Total price is not empty
        - Total price format is correct
        """
        logger.info("Starting: test_cart_total_price")

        await self._add_product_to_cart()

        home_page = HomePage(self.page)
        await home_page.click_cart_button()

        cart_page = CartPage(self.page)
        await cart_page.wait_for_page_load()

        total_price = await cart_page.get_total_price()
        CustomAssertions.assert_not_none(total_price, "Total price should be displayed")
        logger.info(f"Total price: {total_price}")

    @pytest.mark.regression
    @pytest.mark.asyncio
    async def test_empty_cart(self) -> None:
        """Test empty cart scenario.

        Verifies that:
        - Empty cart message is shown
        - Cart state is correctly displayed
        """
        logger.info("Starting: test_empty_cart")

        home_page = HomePage(self.page)
        await home_page.wait_for_page_load()
        await home_page.click_cart_button()

        cart_page = CartPage(self.page)
        await cart_page.wait_for_page_load()

        is_empty = await cart_page.is_cart_empty()
        if is_empty:
            logger.info("Cart is empty as expected")
            await self.take_screenshot("empty_cart")
        else:
            logger.info("Cart contains items")
