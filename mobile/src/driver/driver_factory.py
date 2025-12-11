"""Factory for creating and managing Appium driver instances."""

from typing import Optional

from appium import webdriver
from appium.webdriver.appium_service import AppiumService

from mobile.config.appium_config import AppiumConfig
from mobile.config.settings import settings
from mobile.src.utils.logger import get_logger

logger = get_logger(__name__)


class DriverFactory:
    """Factory class for creating Appium driver instances."""

    _appium_service: Optional[AppiumService] = None
    _driver: Optional[webdriver.WebDriver] = None

    @classmethod
    def create_driver(cls) -> webdriver.WebDriver:
        """Create and return Appium driver.

        Returns:
            Appium WebDriver instance.

        Raises:
            Exception: If driver creation fails.
        """
        if cls._driver is not None:
            logger.warning("Driver already exists, returning existing instance")
            return cls._driver

        try:
            logger.info(f"Creating Appium driver connecting to {settings.appium_url}")

            capabilities = AppiumConfig.get_android_capabilities()
            logger.debug(f"Android capabilities: {capabilities}")

            cls._driver = webdriver.Remote(
                command_executor=settings.appium_url,
                desired_capabilities=capabilities,
            )

            logger.info("Appium driver created successfully")
            return cls._driver

        except Exception as e:
            logger.error(f"Failed to create Appium driver: {str(e)}")
            raise

    @classmethod
    def quit_driver(cls) -> None:
        """Quit and close Appium driver.

        Safely closes the driver and removes reference.
        """
        if cls._driver is not None:
            try:
                logger.info("Quitting Appium driver")
                cls._driver.quit()
                logger.info("Appium driver closed successfully")
            except Exception as e:
                logger.error(f"Error closing driver: {str(e)}")
            finally:
                cls._driver = None

    @classmethod
    def get_driver(cls) -> webdriver.WebDriver:
        """Get current Appium driver instance.

        Returns:
            Current Appium WebDriver instance.

        Raises:
            RuntimeError: If driver is not initialized.
        """
        if cls._driver is None:
            raise RuntimeError("Driver is not initialized. Call create_driver() first.")
        return cls._driver

    @classmethod
    def start_appium_service(cls) -> None:
        """Start local Appium service.

        Useful for local testing without Docker.
        """
        try:
            logger.info("Starting Appium service")
            cls._appium_service = AppiumService()
            cls._appium_service.start()
            logger.info("Appium service started successfully")
        except Exception as e:
            logger.error(f"Failed to start Appium service: {str(e)}")
            raise

    @classmethod
    def stop_appium_service(cls) -> None:
        """Stop local Appium service."""
        if cls._appium_service is not None:
            try:
                logger.info("Stopping Appium service")
                cls._appium_service.stop()
                logger.info("Appium service stopped successfully")
            except Exception as e:
                logger.error(f"Error stopping Appium service: {str(e)}")
            finally:
                cls._appium_service = None
