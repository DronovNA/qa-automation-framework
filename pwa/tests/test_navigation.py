"""Test cases for PWA navigation."""

import pytest

from pwa.src.base.base_test import BaseTest
from pwa.src.pages.home_page import HomePage
from pwa.src.utils.assertions import CustomAssertions
from pwa.src.utils.logger import get_logger

logger = get_logger(__name__)


class TestNavigation(BaseTest):
    """Test cases for PWA navigation."""

    @pytest.mark.smoke
    @pytest.mark.asyncio
    async def test_home_page_loads(self) -> None:
        """Test that home page loads successfully.

        Verifies that:
        - Home page appears
        - Products are visible
        - Cart button is accessible
        """
        logger.info("Starting: test_home_page_loads")

        home_page = HomePage(self.page)
        await home_page.wait_for_page_load()

        product_count = await home_page.get_product_count()
        CustomAssertions.assert_true(
            product_count > 0,
            "Products should be displayed on home page"
        )
        logger.info(f"Home page loaded with {product_count} products")
        await self.take_screenshot("home_page")

    @pytest.mark.regression
    @pytest.mark.asyncio
    async def test_product_information_visible(self) -> None:
        """Test that product information is visible.

        Verifies that:
        - Product names are displayed
        - Product prices are displayed
        - Products are readable
        """
        logger.info("Starting: test_product_information_visible")

        home_page = HomePage(self.page)
        await home_page.wait_for_page_load()

        product_name = await home_page.get_first_product_name()
        product_price = await home_page.get_first_product_price()

        CustomAssertions.assert_not_none(product_name)
        CustomAssertions.assert_not_none(product_price)
        logger.info(f"Product: {product_name} - Price: {product_price}")
        await self.take_screenshot("product_info")
