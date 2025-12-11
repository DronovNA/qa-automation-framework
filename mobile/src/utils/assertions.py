"""Custom assertions for mobile tests."""

from typing import Any, Optional
from appium.webdriver.webdriver import WebDriver

from mobile.src.utils.logger import get_logger

logger = get_logger(__name__)


class CustomAssertions:
    """Custom assertion methods for mobile testing."""

    @staticmethod
    def assert_equal(actual: Any, expected: Any, message: str = "") -> None:
        """Assert that two values are equal.

        Args:
            actual: Actual value.
            expected: Expected value.
            message: Optional assertion message.

        Raises:
            AssertionError: If values are not equal.
        """
        assert_message = f"Expected {expected}, but got {actual}"
        if message:
            assert_message = f"{message}: {assert_message}"
        logger.info(f"Asserting: {assert_message}")
        assert actual == expected, assert_message

    @staticmethod
    def assert_true(condition: bool, message: str = "") -> None:
        """Assert that condition is True.

        Args:
            condition: Condition to check.
            message: Optional assertion message.

        Raises:
            AssertionError: If condition is False.
        """
        assert_message = f"Expected condition to be True, but was False"
        if message:
            assert_message = f"{message}: {assert_message}"
        logger.info(f"Asserting: {assert_message}")
        assert condition is True, assert_message

    @staticmethod
    def assert_false(condition: bool, message: str = "") -> None:
        """Assert that condition is False.

        Args:
            condition: Condition to check.
            message: Optional assertion message.

        Raises:
            AssertionError: If condition is True.
        """
        assert_message = f"Expected condition to be False, but was True"
        if message:
            assert_message = f"{message}: {assert_message}"
        logger.info(f"Asserting: {assert_message}")
        assert condition is False, assert_message

    @staticmethod
    def assert_in(item: Any, container: Any, message: str = "") -> None:
        """Assert that item is in container.

        Args:
            item: Item to search for.
            container: Container to search in.
            message: Optional assertion message.

        Raises:
            AssertionError: If item not found in container.
        """
        assert_message = f"Expected {item} to be in {container}"
        if message:
            assert_message = f"{message}: {assert_message}"
        logger.info(f"Asserting: {assert_message}")
        assert item in container, assert_message

    @staticmethod
    def assert_not_none(value: Any, message: str = "") -> None:
        """Assert that value is not None.

        Args:
            value: Value to check.
            message: Optional assertion message.

        Raises:
            AssertionError: If value is None.
        """
        assert_message = f"Expected value to not be None"
        if message:
            assert_message = f"{message}: {assert_message}"
        logger.info(f"Asserting: {assert_message}")
        assert value is not None, assert_message
