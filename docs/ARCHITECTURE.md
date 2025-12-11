# QA Automation Framework - Architecture Documentation

Architecture and design patterns used in the QA automation framework.

## Overview

The framework follows industry best practices and design patterns:

- **Page Object Model (POM)** - Separation of UI elements and test logic
- **Factory Pattern** - Driver/Browser creation and management
- **Singleton Pattern** - Single instance of driver/browser manager
- **Fixture Management** - Proper setup and teardown of resources
- **Data-Driven Testing** - Externalized test data

## Mobile Framework Architecture

### Layer Structure

```
Tests (pytest)
    ↓
Page Objects (BasePage)
    ↓
Driver Management (DriverManager)
    ↓
Driver Factory (DriverFactory)
    ↓
Appium Server
```

### Component Details

#### 1. Configuration Layer

```python
config/
├── settings.py          # Environment variable loader
└── appium_config.py    # Appium capabilities
```

**Settings.py** loads from `.env`:
- Appium server URL
- Android device configuration
- Timeout settings
- Logging configuration

**AppiumConfig.py** provides:
- Android capabilities
- Platform-specific options
- Device configuration

#### 2. Driver Management Layer

```python
src/driver/
├── driver_factory.py   # Creates driver instances
└── driver_manager.py   # Manages driver lifecycle
```

**DriverFactory**:
- Singleton pattern (optional)
- Creates Appium driver
- Manages driver startup/shutdown
- Handles Appium service (local)

**DriverManager**:
- Singleton for test session
- Provides driver to tests
- Handles cleanup
- Manages driver state

#### 3. Base Classes Layer

```python
src/base/
├── base_page.py        # Common page methods
├── base_test.py        # Common test setup/teardown
└── wait_handler.py     # Wait strategies
```

**BasePage**:
- Element finding methods
- Click, send_keys, get_text
- Visibility checks
- Wait integration
- Screenshot handling

**BaseTest**:
- Pytest fixtures
- Driver initialization
- Teardown and cleanup
- Screenshot utility

**WaitHandler**:
- Explicit waits
- Visibility waits
- Clickable waits
- Text waits
- Custom condition waits

#### 4. Page Objects Layer

```python
src/pages/
├── home_page.py
├── search_page.py
└── article_page.py
```

Each page object:
- Defines element locators
- Implements page-specific actions
- Inherits from BasePage
- Provides clean API for tests

#### 5. Utilities Layer

```python
src/utils/
├── logger.py           # Logging configuration
├── assertions.py       # Custom assertions
└── screenshot.py       # Screenshot capture
```

**Logger**: Rotating file handler, console output, debug/info levels

**CustomAssertions**: Domain-specific assertions with clear messages

**ScreenshotHandler**: Timestamp-based screenshots, organized storage

#### 6. Test Layer

```python
tests/
├── conftest.py         # Pytest fixtures
├── test_search.py
├── test_navigation.py
└── test_article.py
```

Test organization:
- One file per feature
- Test classes group related tests
- Fixtures provide setup/data
- Markers for categorization

## PWA Framework Architecture

Similar to mobile but with async patterns:

### Key Differences

1. **Async/Await Pattern**
   ```python
   async def click(self, selector):
       await self.page.click(selector)
   ```

2. **Browser Management**
   - Playwright browser/context/page hierarchy
   - Multiple browser support
   - Network interception capability

3. **Selectors**
   - CSS, XPath, text-based
   - More flexible than mobile

## Design Patterns

### 1. Page Object Model (POM)

**Problem**: Tests are brittle and hard to maintain with scattered locators

**Solution**: Centralize element locators and page actions

```python
class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "search")
    
    def click_search(self):
        self.click(self.SEARCH_BOX)
```

**Benefits**:
- Easy maintenance
- Reusable page methods
- Clear separation of concerns

### 2. Factory Pattern

**Problem**: Complex driver initialization

**Solution**: Factory handles all initialization logic

```python
class DriverFactory:
    @classmethod
    def create_driver(cls):
        # Handle all initialization
        driver = webdriver.Remote(...)
        return driver
```

**Benefits**:
- Centralized configuration
- Easy to change driver implementation
- Reusable across tests

### 3. Singleton Pattern

**Problem**: Need single driver instance per test

**Solution**: Singleton ensures one instance

```python
class DriverManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

**Benefits**:
- Single driver per test
- Easy cleanup
- Global access without globals

### 4. Wait Pattern

**Problem**: Hard-coded sleeps and brittle waits

**Solution**: Explicit intelligent waits

```python
await self.wait.wait_for_element_visible(locator)
await self.wait.wait_for_text_in_element(locator, text)
```

**Benefits**:
- Tests run fast
- Better reliability
- Clear intent

## Data Flow

### Mobile Test Execution

```
Test Method
    ↓
PageObject (HomePage)
    ↓
BasePage.click() / get_text() / etc
    ↓
WaitHandler (explicit waits)
    ↓
Selenium WebDriver
    ↓
Appium Server
    ↓
Android Device
```

### PWA Test Execution

```
Test Method (async)
    ↓
PageObject (HomePage)
    ↓
BasePage.click() / get_text() / etc (await)
    ↓
WaitHandler (Playwright waits)
    ↓
Playwright Browser
    ↓
Browser Engine (Chromium/Firefox/WebKit)
    ↓
Web Application
```

## Configuration Management

### Settings Hierarchy

1. **Environment Variables** (.env file)
   - Highest priority
   - Local configuration
   - Secret management

2. **Default Settings** (settings.py)
   - Fallback values
   - Documented defaults
   - Framework constants

3. **Runtime Overrides**
   - Command-line arguments
   - Programmatic changes
   - Test-specific configuration

## Error Handling

### Exception Strategy

```python
try:
    element = self.find_element(locator)
except NoSuchElementException:
    logger.error(f"Element not found: {locator}")
    self.screenshot.take_screenshot("element_not_found")
    raise
```

**Key Points**:
- Log before raising
- Take screenshot on failure
- Preserve original exception
- Add context information

## Logging Strategy

### Log Levels

- **DEBUG**: Detailed information for debugging
- **INFO**: General information about test execution
- **WARNING**: Something unexpected happened
- **ERROR**: Test failed, with details
- **CRITICAL**: Framework error, cannot continue

### Log Format

```
2024-01-15 10:30:45 - mobile.src.pages.home_page - INFO - Clicking search box
```

## Performance Considerations

### Optimization Strategies

1. **Parallel Execution**
   - Multiple workers with pytest-xdist
   - Isolated test environments
   - Independent state

2. **Reuse Resources**
   - Driver per test (not session)
   - Fast setup/teardown
   - Proper cleanup

3. **Efficient Waits**
   - Explicit waits (not sleep)
   - Minimal timeout values
   - Smart element detection

## Testing Best Practices

### Test Design

1. **Single Responsibility**
   - One feature per test
   - Clear test name
   - Focused assertions

2. **Data Independence**
   - Use test data fixtures
   - Reset state between tests
   - Avoid test interdependencies

3. **Clean Setup/Teardown**
   - Fixtures for setup
   - Proper resource cleanup
   - No leftover state

### Code Quality

1. **Readability**
   - Clear variable names
   - Comprehensive docstrings
   - Consistent formatting

2. **Maintainability**
   - DRY principle
   - Reusable methods
   - Helper functions

3. **Type Safety**
   - Type hints
   - Mypy compliance
   - Clear interfaces

## Continuous Integration

### CI/CD Pipeline

```
Push to GitHub
    ↓
GitHub Actions Triggered
    ↓
Setup Environment
    ↓
Install Dependencies
    ↓
Run Tests (parallel)
    ↓
Generate Reports
    ↓
Upload Artifacts
    ↓
Notify Results
```

## Security Considerations

### Sensitive Data

- Store credentials in .env
- Never commit .env files
- Use environment variables in CI/CD
- Mask sensitive logs

### URL Safety

- Use HTTPS URLs
- Validate SSL certificates
- Avoid hardcoding credentials in URLs

## Scalability

### Horizontal Scaling

1. **Parallel Execution**
   - Multiple workers
   - Distributed testing
   - Load balancing

2. **Docker Containers**
   - Appium in containers
   - Multiple browser instances
   - Easy deployment

3. **Cloud Integration**
   - BrowserStack integration
   - Lambda execution
   - CloudWatch logging
