# PWA Testing Framework (Playwright)

Production-ready test automation framework for Progressive Web Applications using Playwright.

## Overview

This framework is designed for testing PWA applications like Swapy demo, demonstrating best practices in web test automation with async/await patterns.

## Features

- **Async/Await Pattern**: Modern async test execution with Playwright
- **Page Object Model**: Organized page classes with element selectors and methods
- **Wait Strategies**: Intelligent waiting for elements and conditions
- **Custom Assertions**: Domain-specific assertions with clear failure messages
- **Logging**: Comprehensive logging at multiple levels
- **Screenshots**: Automatic screenshots on failures and manual screenshots during tests
- **Data-Driven Testing**: Test data in YAML format
- **Fixture Management**: Proper setup/teardown with pytest fixtures
- **Retry Decorator**: Automatic retry mechanism for flaky operations

## Project Structure

```
pwa/
├── config/                 # Configuration management
│   ├── settings.py        # Environment-based settings loader
│   └── browser_config.py  # Playwright-specific configuration
├── src/
│   ├── browser/           # Browser factory and management
│   ├── base/              # Base classes for pages and tests
│   ├── pages/             # Page objects
│   ├── models/            # Data models
│   └── utils/             # Utilities (logger, assertions, screenshots, decorators)
├── tests/                 # Test cases
├── data/                  # Test data (YAML/JSON)
├── requirements.txt       # Python dependencies
├── playwright.ini         # Playwright/pytest configuration
├── .env.example          # Environment variables example
└── README.md             # This file
```

## Setup

### Prerequisites

- Python 3.9+
- Modern browser (Chromium, Firefox, or WebKit)

### Installation

1. **Install Python dependencies**

```bash
cd pwa
pip install -r requirements.txt
```

2. **Install Playwright browsers**

```bash
playwright install
```

3. **Configure environment**

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```bash
# PWA settings
PWA_BASE_URL=https://demo.swapy.dev
BROWSER_TYPE=chromium  # chromium, firefox, webkit
BROWSER_HEADLESS=true
BROWSER_SLOWMO=0

# Playwright settings
PLAYWRIGHT_TIMEOUT=30000
PLAYWRIGHT_VIEWPORT_WIDTH=1280
PLAYWRIGHT_VIEWPORT_HEIGHT=720
```

## Running Tests

### All tests

```bash
pytest tests/
```

### Specific test file

```bash
pytest tests/test_navigation.py -v
```

### Specific test class

```bash
pytest tests/test_products.py::TestProducts -v
```

### Specific test method

```bash
pytest tests/test_cart.py::TestCart::test_add_to_cart_and_view -v
```

### By marker (smoke, regression)

```bash
pytest -m smoke
pytest -m regression
```

### Headed mode (with browser UI)

```bash
pytest tests/ --headed
```

### With video recording

```bash
pytest tests/ --video on
```

### Parallel execution

```bash
pytest -n auto  # Using number of CPU cores
pytest -n 4     # Using 4 workers
```

## Architecture

### Page Object Model (POM)

Each page/section has its own class:

```python
from pwa.src.base.base_page import BasePage

class HomePage(BasePage):
    # Selectors
    PRODUCT_ITEM = ".product-item"
    
    # Page-specific methods
    async def click_product(self):
        await self.click(self.PRODUCT_ITEM)
```

### Base Classes

**BasePage**: Provides common element interaction methods
- `click()`, `fill()`, `get_text()`
- `is_element_visible()`, `is_element_enabled()`
- `wait` handler for intelligent waits

**BaseTest**: Provides browser management and test setup/teardown
- Automatic browser initialization
- Proper cleanup after each test
- Screenshot utility

### Wait Strategies

```python
# Wait for element to be visible
await self.wait.wait_for_selector_visible(selector)

# Wait for element to be hidden
await self.wait.wait_for_selector_hidden(selector)

# Wait for text in element
await self.wait.wait_for_text(selector, "text")

# Wait for navigation
await self.wait.wait_for_navigation()
```

### Custom Assertions

```python
from pwa.src.utils.assertions import CustomAssertions

CustomAssertions.assert_equal(actual, expected)
CustomAssertions.assert_true(condition)
CustomAssertions.assert_in(item, collection)
CustomAssertions.assert_not_none(value)
```

### Retry Decorator

```python
from pwa.src.utils.decorators import retry

@retry(max_attempts=3, delay=1.0)
async def flaky_operation():
    # Operation that might fail
    pass
```

## Test Data

Test data is stored in `data/test_products.yaml`:

```yaml
products:
  - name: "Laptop"
    price: 1299.99
    description: "High-performance laptop"
    sku: "LAPTOP-001"
```

Load in conftest:

```python
@pytest.fixture
def test_data():
    # Returns loaded YAML data
    pass
```

## Selectors

Selectors are defined as class attributes in page objects:

```python
PRODUCT_ITEM = ".product-item"
BUY_BUTTON = "button:has-text('Buy Now')"
CHECKOUT = "a[href='/checkout']"
```

### Playwright Selector Syntax

- CSS selectors: `.class`, `#id`, `[attr='value']`
- XPath: `//div[@class='name']`
- Text selectors: `button:has-text('Click me')`
- Combining: `text=/pattern/, css=selector`

## Logging

Logs are stored in `logs/test_execution.log`:

```python
from pwa.src.utils.logger import get_logger

logger = get_logger(__name__)
logger.info("Test step")
logger.debug("Debug info")
logger.error("Error message")
```

## Screenshots

Screenshots are captured in `reports/screenshots/`:

```python
# Automatic on failure (if SCREENSHOT_ON_FAILURE=true)

# Manual
await self.take_screenshot("step_name")
```

## CI/CD Integration

GitHub Actions workflow in `.github/workflows/pwa-tests.yml`:

```yaml
name: PWA Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: |
          pip install -r pwa/requirements.txt
          playwright install
      - name: Run tests
        run: pytest pwa/tests/ -v
```

## Troubleshooting

### Browser installation issues

```bash
# Ensure browsers are installed
playwright install

# Verify installation
playwright install-deps
```

### Element not found

1. Check selector accuracy with Playwright Inspector
2. Add wait with explicit timeout
3. Enable headed mode for debugging: `pytest --headed`

### Test timeout

```bash
# Increase timeout
pytest --timeout=300  # 5 minutes
```

### View test execution

```bash
# Record video
pytest --video on

# Record trace for debugging
pytest --traceviewer
```

## Best Practices

1. **Use async/await** - Properly handle asynchronous operations
2. **One action per test** - Each test should verify one feature
3. **Descriptive names** - Test name should describe what is tested
4. **Use intelligent waits** - Avoid hard sleeps, use wait handlers
5. **Externalize data** - Use YAML/JSON for test data
6. **Take screenshots** - Capture state for debugging
7. **Log actions** - Log all significant test steps
8. **Clean selectors** - Use stable, maintainable selectors
9. **Organize pages** - One page object per URL/section
10. **Handle errors** - Use try-except for graceful error handling

## Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest-Asyncio](https://github.com/pytest-dev/pytest-asyncio)
- [Playwright Inspector](https://playwright.dev/python/docs/debug#playwright-inspector)

## Support

For issues or questions, please open an issue on the project repository.
