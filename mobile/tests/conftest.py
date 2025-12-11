"""Pytest configuration and fixtures for mobile tests."""

import pytest
import yaml
from pathlib import Path

from mobile.src.driver.driver_factory import DriverFactory
from mobile.src.driver.driver_manager import DriverManager
from mobile.src.utils.logger import get_logger
from mobile.config.settings import settings

logger = get_logger(__name__)

# Register markers
def pytest_configure(config):
    """Register custom pytest markers."""
    config.addinivalue_line("markers", "smoke: smoke tests")
    config.addinivalue_line("markers", "regression: regression tests")
    config.addinivalue_line("markers", "integration: integration tests")
    config.addinivalue_line("markers", "slow: slow tests")


@pytest.fixture(scope="session")
def test_data():
    """Load test data from YAML file.

    Yields:
        Loaded test data dictionary.
    """
    data_file = Path(__file__).parent.parent / "data" / "test_searches.yaml"
    if data_file.exists():
        with open(data_file, "r") as f:
            data = yaml.safe_load(f)
        logger.info(f"Loaded test data from {data_file}")
        return data
    return {}


@pytest.fixture(scope="function")
def driver():
    """Provide Appium driver for tests.

    Yields:
        Configured Appium WebDriver.
    """
    logger.info("Creating driver fixture")
    driver = DriverFactory.create_driver()
    yield driver
    logger.info("Closing driver fixture")
    DriverFactory.quit_driver()
    DriverManager.reset_singleton()


@pytest.fixture(scope="function")
def driver_manager():
    """Provide DriverManager instance.

    Yields:
        DriverManager singleton instance.
    """
    manager = DriverManager()
    yield manager
    manager.close_driver()
    DriverManager.reset_singleton()
