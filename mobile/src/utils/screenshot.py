"""Screenshot capture and management utilities."""

from pathlib import Path
from datetime import datetime

from appium.webdriver.webdriver import WebDriver

from mobile.config.settings import settings
from mobile.src.utils.logger import get_logger

logger = get_logger(__name__)


class ScreenshotHandler:
    """Handles screenshot capture and storage."""

    def __init__(self, driver: WebDriver) -> None:
        """Initialize ScreenshotHandler.

        Args:
            driver: Appium WebDriver instance.
        """
        self.driver = driver
        self.screenshot_dir = Path(settings.report_dir) / "screenshots"
        self.screenshot_dir.mkdir(parents=True, exist_ok=True)

    def take_screenshot(self, name: str = "screenshot") -> str:
        """Take and save screenshot.

        Args:
            name: Name for screenshot file (without extension).

        Returns:
            Path to saved screenshot file.
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}.png"
            filepath = self.screenshot_dir / filename

            self.driver.save_screenshot(str(filepath))
            logger.info(f"Screenshot saved: {filepath}")
            return str(filepath)
        except Exception as e:
            logger.error(f"Failed to take screenshot: {str(e)}")
            raise
