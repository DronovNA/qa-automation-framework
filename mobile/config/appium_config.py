"""Appium-specific configuration and capabilities."""

from typing import Dict, Any

from .settings import settings


class AppiumConfig:
    """Appium driver capabilities and configuration."""

    @staticmethod
    def get_android_capabilities() -> Dict[str, Any]:
        """Get Android desired capabilities for Appium.

        Returns:
            Dictionary with Android desired capabilities.
        """
        capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "platformVersion": settings.android_platform_version,
            "deviceName": settings.android_device_name,
            "appPackage": settings.android_package_name,
            "appActivity": settings.android_activity_name,
            "autoGrantPermissions": settings.android_auto_grant_permissions,
            "noReset": False,
            "fullReset": False,
            "newCommandTimeout": settings.appium_timeout * 1000,
            "connectHardwareKeyboard": False,
        }
        return capabilities

    @staticmethod
    def get_appium_options() -> Dict[str, Any]:
        """Get Appium connection options.

        Returns:
            Dictionary with Appium connection options.
        """
        return {
            "host": settings.appium_host,
            "port": settings.appium_port,
            "timeout": settings.appium_timeout,
        }
