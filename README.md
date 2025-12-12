# QA Automation Framework

[![Build Status](https://github.com/DronovNA/qa-automation-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/DronovNA/qa-automation-framework/actions/workflows/ci.yml)
[![CodeQL](https://github.com/DronovNA/qa-automation-framework/actions/workflows/codeql.yml/badge.svg)](https://github.com/DronovNA/qa-automation-framework/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)

Production-ready test automation framework for mobile (Android/Appium) and PWA (Playwright) applications with best practices and clean code.

## Features

- **Mobile Testing**: Appium-based framework for Android applications
- **PWA Testing**: Playwright-based framework for Progressive Web Applications
- **Best Practices**: Page Object Model, data-driven testing, fixture management, comprehensive logging, custom assertions, CI/CD ready
- **Clean Code**: SOLID principles, type hints, comprehensive docstrings
- **Configuration Management**: Environment-based configuration with python-dotenv
- **Reporting**: Detailed test reports with coverage metrics and screenshots
- **Security**: CodeQL analysis, secret detection, dependency scanning
- **CI/CD**: GitHub Actions with Python 3.9/3.10 matrix, artifact uploads, coverage tracking

## Project Structure

```
qa-automation-framework/
├── mobile/                          # Appium mobile testing framework
│   ├── config/                      # Configuration modules
│   ├── src/
│   │   ├── driver/                  # Driver factory and manager
│   │   ├── base/                    # Base page/test classes
│   │   ├── pages/                   # Page Object Model implementations
│   │   ├── models/                  # Data models
│   │   └── utils/                   # Logger, assertions, screenshots
│   ├── tests/                       # Test cases
│   ├── data/                        # Test data (YAML)
│   └── requirements.txt
├── pwa/                             # Playwright PWA testing framework
│   ├── config/                      # Configuration modules
│   ├── src/
│   │   ├── browser/                 # Browser factory and manager
│   │   ├── base/                    # Base page/test classes
│   │   ├── pages/                   # Page Object Model implementations
│   │   ├── models/                  # Data models
│   │   └── utils/                   # Logger, assertions, decorators
│   ├── tests/                       # Test cases
│   ├── data/                        # Test data (YAML)
│   └── requirements.txt
├── .github/workflows/               # CI/CD workflows
│   ├── ci.yml                       # Main CI pipeline (tests, lint, coverage)
│   ├── codeql.yml                   # Security analysis
│   ├── secret-detection.yml         # Secret scanning
│   └── dependabot.yml               # Automated dependency updates
├── docs/                            # Extended documentation
├── scripts/                         # Setup and execution scripts
├── pyproject.toml                   # Project config and tool settings
├── requirements.txt                 # Root dependencies
└── .pre-commit-config.yaml          # Pre-commit hooks config
```

## Quick Start

### Prerequisites

- Python 3.9 or 3.10
- Git
- (Mobile) Java JDK and Android SDK
- (Mobile) Appium server running (optional with Docker)

### Installation

```bash
# Clone repository
git clone https://github.com/DronovNA/qa-automation-framework.git
cd qa-automation-framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install root dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install
```

### Running Tests Locally

#### Mobile Tests (Appium)

```bash
cd mobile
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your configuration (APPIUM_HOST, device caps, etc.)

# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_search.py -v

# Run with markers
pytest tests/ -m smoke -v
pytest tests/ -m regression -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html --cov-report=term-missing
```

#### PWA Tests (Playwright)

```bash
cd pwa
pip install -r requirements.txt
cp .env.example .env
playwright install  # Downloads browsers (Chromium, Firefox, WebKit)

# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_products.py -v

# Run with markers
pytest tests/ -m smoke -v

# Run with specific browser
BROWSER_TYPE=firefox pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html --cov-report=term-missing

# Run in headed mode for debugging
HEADED=1 pytest tests/ -v
```

### Code Quality

```bash
# Format with black
black mobile/ pwa/

# Sort imports with isort
isort mobile/ pwa/

# Lint with flake8
flake8 mobile/src mobile/tests pwa/src pwa/tests

# Type check with mypy
mypy mobile/src pwa/src

# Security check with bandit
bandit -r mobile/src pwa/src

# Run all pre-commit hooks
pre-commit run --all-files

# Check dependencies for vulnerabilities
pip audit
```

## Test Targets

**Mobile**: [Wikipedia Android App](https://play.google.com/store/apps/details?id=org.wikipedia)
- Free, open-source
- Rich functionality for testing

**PWA**: [Swapy E-commerce Demo](https://demo.swapy.dev)
- Modern PWA with e-commerce features
- Publicly accessible

## Architecture Highlights

- **Page Object Model**: Centralized element locators and page methods
- **Data-Driven Testing**: Externalized test data in YAML format
- **Fixture Management**: Proper setup/teardown with pytest fixtures
- **Custom Assertions**: Domain-specific assertions with detailed messages
- **Logging**: Request/response logging, test steps, error tracking with loguru
- **Screenshot Management**: Automatic screenshots on test failures
- **Type Safety**: Type hints throughout codebase for better IDE support

## Technologies

| Component | Stack |
|-----------|-------|
| **Mobile** | Python, Appium, PyTest, Android SDK |
| **PWA** | Python, Playwright, PyTest |
| **CI/CD** | GitHub Actions, CodeQL, Dependabot |
| **Code Quality** | Black, isort, flake8, mypy, bandit |
| **Configuration** | python-dotenv, YAML, Pydantic |
| **Reporting** | Pytest, Allure, Coverage |

## CI/CD Pipeline

The repository includes comprehensive CI/CD workflows:

- **main CI workflow** (ci.yml): Tests on Python 3.9 & 3.10, coverage, artifact uploads
- **CodeQL** (codeql.yml): Security analysis on every push
- **Secret Detection** (secret-detection.yml): Prevents credential commits
- **Dependabot** (dependabot.yml): Automated dependency updates

All workflows run with minimal permissions (read-only by default).

## Documentation

- [Setup Guide](docs/SETUP.md)
- [Mobile Setup Details](docs/MOBILE_SETUP.md)
- [PWA Setup Details](docs/PWA_SETUP.md)
- [Architecture Documentation](docs/ARCHITECTURE.md)
- [Security Policy](SECURITY.md)
- [Contributing Guidelines](CONTRIBUTING.md)

## Security

- Never commit `.env` files or credentials
- Use GitHub Secrets for sensitive data in CI/CD
- Review SECURITY.md for best practices
- Report vulnerabilities to security@qa-automation.dev (non-public)

## License

MIT License — see LICENSE file

## Author

[Nikita Dronov](https://github.com/DronovNA)
