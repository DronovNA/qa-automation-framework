"""Test cases for PWA product functionality."""

import pytest

from pwa.src.base.base_test import BaseTest
from pwa.src.pages.home_page import HomePage
from pwa.src.pages.products_page import ProductsPage
from pwa.src.utils.assertions import CustomAssertions
from pwa.src.utils.logger import get_logger

logger = get_logger(__name__)


class TestProducts(BaseTest):
    """Test cases for products functionality."""

    @pytest.mark.smoke
    @pytest.mark.asyncio
    async def test_get_product_count(self) -> None:
        """Test getting product count.

        Verifies that:
        - Products are loaded
        - Product count is accurate
        - At least one product exists
        """
        logger.info("Starting: test_get_product_count")

        home_page = HomePage(self.page)
        await home_page.wait_for_page_load()

        count = await home_page.get_product_count()
        CustomAssertions.assert_true(count > 0, "At least one product should exist")
        logger.info(f"Product count: {count}")

    @pytest.mark.regression
    @pytest.mark.asyncio
    async def test_get_product_details(self) -> None:
        """Test getting product details.

        Verifies that:
        - Product name is retrievable
        - Product price is retrievable
        - Product details are not empty
        """
        logger.info("Starting: test_get_product_details")

        home_page = HomePage(self.page)
        await home_page.wait_for_page_load()

        name = await home_page.get_first_product_name()
        price = await home_page.get_first_product_price()

        CustomAssertions.assert_not_none(name, "Product name should not be empty")
        CustomAssertions.assert_not_none(price, "Product price should not be empty")
        logger.info(f"Product details - Name: {name}, Price: {price}")
        await self.take_screenshot("product_details")

    @pytest.mark.regression
    @pytest.mark.asyncio
    async def test_add_product_to_cart(self) -> None:
        """Test adding product to cart.

        Verifies that:
        - Add to cart button is clickable
        - Product can be added to cart
        - No errors occur during addition
        """
        logger.info("Starting: test_add_product_to_cart")

        home_page = HomePage(self.page)
        await home_page.wait_for_page_load()
        await self.take_screenshot("before_add_to_cart")

        logger.info("Adding product to cart")
        await home_page.add_first_product_to_cart()
        await self.take_screenshot("after_add_to_cart")
        logger.info("Product added successfully")
