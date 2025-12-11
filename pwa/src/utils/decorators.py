"""Decorators for PWA tests."""

import asyncio
from typing import TypeVar, Callable, Any
from functools import wraps

from pwa.src.utils.logger import get_logger

logger = get_logger(__name__)

F = TypeVar("F", bound=Callable[..., Any])


def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable[[F], F]:
    """Decorator to retry async function on failure.

    Args:
        max_attempts: Maximum number of attempts.
        delay: Delay between retries in seconds.

    Returns:
        Decorated function that retries on failure.
    """
    def decorator(func: F) -> F:
        @wraps(func)
        async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    logger.debug(f"Attempt {attempt}/{max_attempts} for {func.__name__}")
                    return await func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        logger.error(f"All {max_attempts} attempts failed for {func.__name__}")
                        raise
                    logger.warning(f"Attempt {attempt} failed, retrying in {delay}s: {str(e)}")
                    await asyncio.sleep(delay)

        @wraps(func)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    logger.debug(f"Attempt {attempt}/{max_attempts} for {func.__name__}")
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        logger.error(f"All {max_attempts} attempts failed for {func.__name__}")
                        raise
                    logger.warning(f"Attempt {attempt} failed, retrying in {delay}s: {str(e)}")
                    asyncio.sleep(delay)

        if asyncio.iscoroutinefunction(func):
            return async_wrapper  # type: ignore
        else:
            return sync_wrapper  # type: ignore

    return decorator
