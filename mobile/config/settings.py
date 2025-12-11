"""Configuration settings loader for mobile testing framework."""

import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv


class Settings:
    """Centralized settings management for mobile testing."""

    def __init__(self) -> None:
        """Initialize settings from environment variables."""
        load_dotenv()

        # Global settings
        self.log_level: str = os.getenv("LOG_LEVEL", "INFO")
        self.report_dir: str = os.getenv("REPORT_DIR", "reports")
        self.screenshot_on_failure: bool = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"

        # Appium settings
        self.appium_host: str = os.getenv("APPIUM_HOST", "localhost")
        self.appium_port: int = int(os.getenv("APPIUM_PORT", "4723"))
        self.appium_timeout: int = int(os.getenv("APPIUM_TIMEOUT", "30"))

        # Android settings
        self.android_platform_version: str = os.getenv("ANDROID_PLATFORM_VERSION", "12")
        self.android_device_name: str = os.getenv("ANDROID_DEVICE_NAME", "emulator-5554")
        self.android_package_name: str = os.getenv("ANDROID_PACKAGE_NAME", "org.wikipedia")
        self.android_activity_name: str = os.getenv("ANDROID_ACTIVITY_NAME", "org.wikipedia.main.MainActivity")
        self.android_auto_grant_permissions: bool = os.getenv("ANDROID_AUTO_GRANT_PERMISSIONS", "true").lower() == "true"

    @property
    def appium_url(self) -> str:
        """Get Appium server URL."""
        return f"http://{self.appium_host}:{self.appium_port}"


# Global settings instance
settings = Settings()
