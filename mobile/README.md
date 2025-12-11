# Mobile Testing Framework (Appium)

Production-ready test automation framework for Android mobile applications using Appium.

## Overview

This framework is designed for testing the Wikipedia Android application, demonstrating best practices in mobile test automation.

## Features

- **Page Object Model**: Organized page classes with element locators and methods
- **Wait Strategies**: Intelligent waiting for elements and conditions
- **Custom Assertions**: Domain-specific assertions with clear failure messages
- **Logging**: Comprehensive logging at multiple levels
- **Screenshots**: Automatic screenshots on failures and manual screenshots during tests
- **Data-Driven Testing**: Test data in YAML format
- **Fixture Management**: Proper setup/teardown with pytest fixtures

## Project Structure

```
mobile/
├── config/                 # Configuration management
│   ├── settings.py        # Environment-based settings loader
│   └── appium_config.py   # Appium-specific capabilities
├── src/
│   ├── driver/            # Driver factory and management
│   ├── base/              # Base classes for pages and tests
│   ├── pages/             # Page objects
│   ├── models/            # Data models
│   └── utils/             # Utilities (logger, assertions, screenshots)
├── tests/                 # Test cases
├── data/                  # Test data (YAML/JSON)
├── requirements.txt       # Python dependencies
├── pytest.ini             # Pytest configuration
├── .env.example          # Environment variables example
└── README.md             # This file
```

## Setup

### Prerequisites

- Python 3.9+
- Java JDK 11+
- Android SDK (with platform tools)
- Appium server
- Android device or emulator

## Running Tests

### All tests
```bash
pytest tests/
```

### Specific marker
```bash
pytest -m smoke
pytest -m regression
```

### With output
```bash
pytest tests/ -v
```

## Test Cases

### Search Tests (`test_search.py`)
- `test_search_valid_query` - Search with valid query
- `test_search_empty_query` - Search with empty query
- `test_search_special_characters` - Search with special characters
- `test_search_clear_functionality` - Clear search box
- `test_search_result_click` - Click on search result

### Navigation Tests (`test_navigation.py`)
- `test_home_page_loads` - Home page loads successfully
- `test_back_button_navigation` - Back button navigation
- `test_search_to_article_flow` - Complete search to article flow

### Article Tests (`test_article.py`)
- `test_article_loads` - Article page loads
- `test_article_scroll` - Scroll through article
- `test_article_save_button` - Save article button
- `test_article_share_button` - Share article button
