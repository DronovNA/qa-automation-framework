# PWA Testing Framework - Detailed Setup

Detailed setup instructions for Playwright-based PWA testing framework.

## Prerequisites

### Required Software

1. **Python 3.9+**
   - Download: https://www.python.org/
   - Verify: `python --version`

2. **Browsers** (automatic with Playwright)
   - Chromium
   - Firefox
   - WebKit

3. **Operating System**
   - Windows, macOS, or Linux

## Installation Steps

### 1. Clone and Setup

```bash
cd qa-automation-framework/pwa
pip install -r requirements.txt
cp .env.example .env
```

### 2. Install Playwright Browsers

```bash
playwright install

# Install specific browser
playwright install chromium
playwright install firefox
playwright install webkit

# Install system dependencies (Linux)
playwright install-deps
```

### 3. Configure Environment Variables

Edit `pwa/.env`:

```bash
# PWA Application
PWA_BASE_URL=https://demo.swapy.dev

# Browser Settings
BROWSER_TYPE=chromium  # chromium, firefox, webkit
BROWSER_HEADLESS=true
BROWSER_SLOWMO=0       # Delay in ms, 0 = no delay

# Playwright Settings
PLAYWRIGHT_TIMEOUT=30000     # in milliseconds
PLAYWRIGHT_VIEWPORT_WIDTH=1280
PLAYWRIGHT_VIEWPORT_HEIGHT=720

# Logging
LOG_LEVEL=INFO
REPORT_DIR=reports
SCREENSHOT_ON_FAILURE=true
```

## Running Tests

### Basic Commands

```bash
# All tests (Chromium)
pytest tests/ -v

# Specific test file
pytest tests/test_products.py -v

# Specific test
pytest tests/test_products.py::TestProducts::test_get_product_count -v

# Smoke tests only
pytest -m smoke -v
```

### Browser-Specific Testing

```bash
# Test with Chromium
BROWSER_TYPE=chromium pytest tests/ -v

# Test with Firefox
BROWSER_TYPE=firefox pytest tests/ -v

# Test with WebKit
BROWSER_TYPE=webkit pytest tests/ -v

# Test all browsers sequentially
for browser in chromium firefox webkit; do
  BROWSER_TYPE=$browser pytest tests/ -v
done
```

### Advanced Options

```bash
# Headed mode (see browser)
pytest tests/ -v --headed

# Slow down execution
BROWSER_SLOWMO=500 pytest tests/ -v  # 500ms delay

# Record video
pytest tests/ --video on --video-size 1280x720

# Record trace for debugging
pytest tests/ --trace on

# With HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html

# With coverage
pytest tests/ --cov=src --cov-report=html

# Parallel execution
pytest tests/ -n 4  # 4 workers

# Stop on first failure
pytest tests/ -x
```

### Debugging

```bash
# Headed mode for visual debugging
pytest tests/test_name.py -v --headed

# Slow execution for step-by-step
pytest tests/test_name.py -v --headed --browser-slowmo 1000

# Trace recording for post-mortem debugging
pytest tests/test_name.py --trace on
playwright show-trace trace.zip
```

## Element Locators

### Playwright Selector Syntax

```python
# CSS Selectors
".product-item"                    # Class
"#main-content"                    # ID
"input[type='text']"              # Attribute
"button.primary:first-child"      # Pseudo-class

# XPath
"//div[@class='product']"         # Attribute
"//button[contains(text(), 'Add')]"  # Text content
"//div[1]/span[2]"               # Position

# Text Selectors
"button:has-text('Click me')"    # Has text
"text=Welcome"                    # Exact text
"text=/pattern/"                 # Regex pattern

# Combining
"text=Login >> button"           # Chained selectors
```

### Finding Locators

```bash
# Playwright Inspector
pytest --headed --browser-slowmo 1000

# Browser DevTools
# F12 in browser, inspect elements

# Playwright Trace Viewer
playwright show-trace trace.zip
```

## Test Data

### Loading from YAML

```python
@pytest.fixture
def test_data():
    with open('data/test_products.yaml') as f:
        return yaml.safe_load(f)
```

### Example YAML Format

```yaml
products:
  - name: "Product Name"
    price: 99.99
    description: "Description"
    sku: "SKU-001"
```

## Performance Optimization

### Reduce Execution Time

```bash
# Run tests in parallel
pytest tests/ -n auto

# Reduce viewport size
PLAYWRIGHT_VIEWPORT_WIDTH=800 pytest tests/

# Disable video recording in CI
video_recording=off pytest tests/
```

### Memory Optimization

```bash
# Run single browser at a time
BROWSER_TYPE=chromium pytest tests/

# Set smaller viewport
PLAYWRIGHT_VIEWPORT_WIDTH=640 pytest tests/
```

## Continuous Integration

See `.github/workflows/pwa-tests.yml` for CI/CD configuration.

Key points:
- Tests multiple browsers
- Automatic on push and PR
- Artifact uploads for reports
- Video recording on failure

## Common Issues and Solutions

### Playwright Not Installed

```bash
playwright install
playwright install-deps
```

### Browser Not Found

```bash
# Reinstall specific browser
playwright install chromium

# Check installation
playwright install --check
```

### Timeout Errors

```bash
# Increase timeout in .env
PLAYWRIGHT_TIMEOUT=60000

# Or in test
await self.wait.wait_for_selector_visible(selector, timeout=60000)
```

### Element Not Interactable

```bash
# Scroll into view first
await self.scroll_to_element(selector)

# Wait for element to be visible
await self.wait.wait_for_selector_visible(selector)

# Use headed mode to debug
pytest test_name.py --headed --browser-slowmo 1000
```

### Network Issues

```bash
# Use network idle wait
await self.wait.wait_for_navigation()

# Configure in test
await page.wait_for_load_state("networkidle")
```

## Support Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Playwright Inspector](https://playwright.dev/python/docs/debug#playwright-inspector)
- [Swapy Demo](https://demo.swapy.dev)
