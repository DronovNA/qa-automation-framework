"""Configuration settings loader for PWA testing framework."""

import os
from dotenv import load_dotenv


class Settings:
    """Centralized settings management for PWA testing."""

    def __init__(self) -> None:
        """Initialize settings from environment variables."""
        load_dotenv()

        # Global settings
        self.log_level: str = os.getenv("LOG_LEVEL", "INFO")
        self.report_dir: str = os.getenv("REPORT_DIR", "reports")
        self.screenshot_on_failure: bool = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"

        # PWA settings
        self.pwa_base_url: str = os.getenv("PWA_BASE_URL", "https://demo.swapy.dev")
        self.browser_type: str = os.getenv("BROWSER_TYPE", "chromium")
        self.browser_headless: bool = os.getenv("BROWSER_HEADLESS", "true").lower() == "true"
        self.browser_slowmo: int = int(os.getenv("BROWSER_SLOWMO", "0"))

        # Playwright settings
        self.playwright_timeout: int = int(os.getenv("PLAYWRIGHT_TIMEOUT", "30000"))
        self.viewport_width: int = int(os.getenv("PLAYWRIGHT_VIEWPORT_WIDTH", "1280"))
        self.viewport_height: int = int(os.getenv("PLAYWRIGHT_VIEWPORT_HEIGHT", "720"))


# Global settings instance
settings = Settings()
