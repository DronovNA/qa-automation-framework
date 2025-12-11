"""Pytest configuration and fixtures for PWA tests."""

import pytest
import yaml
from pathlib import Path

from pwa.src.browser.browser_factory import BrowserFactory
from pwa.src.browser.browser_manager import BrowserManager
from pwa.src.utils.logger import get_logger

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
    data_file = Path(__file__).parent.parent / "data" / "test_products.yaml"
    if data_file.exists():
        with open(data_file, "r") as f:
            data = yaml.safe_load(f)
        logger.info(f"Loaded test data from {data_file}")
        return data
    return {}


@pytest.fixture
async def browser_manager():
    """Provide BrowserManager instance.

    Yields:
        BrowserManager singleton instance.
    """
    manager = BrowserManager()
    yield manager
    await manager.close_browser()
    BrowserManager.reset_singleton()
