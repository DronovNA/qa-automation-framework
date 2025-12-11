"""Playwright-specific configuration and capabilities."""

from typing import Dict, Any
from pwa.config.settings import settings


class BrowserConfig:
    """Playwright browser configuration."""

    @staticmethod
    def get_browser_options() -> Dict[str, Any]:
        """Get browser launch options for Playwright.

        Returns:
            Dictionary with browser launch options.
        """
        options = {
            "headless": settings.browser_headless,
            "slow_mo": settings.browser_slowmo,
        }
        return options

    @staticmethod
    def get_context_options() -> Dict[str, Any]:
        """Get browser context options.

        Returns:
            Dictionary with context options.
        """
        options = {
            "viewport": {
                "width": settings.viewport_width,
                "height": settings.viewport_height,
            },
            "ignore_https_errors": True,
        }
        return options

    @staticmethod
    def get_navigation_options() -> Dict[str, Any]:
        """Get page navigation options.

        Returns:
            Dictionary with navigation options.
        """
        return {
            "wait_until": "networkidle",
            "timeout": settings.playwright_timeout,
        }
