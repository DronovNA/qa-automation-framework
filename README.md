# QA Automation Framework

Production-ready test automation framework for mobile (Android/Appium) and PWA (Playwright) applications with best practices and clean code.

## 🎯 Features

- **Mobile Testing**: Appium-based framework for Android applications
- **PWA Testing**: Playwright-based framework for Progressive Web Applications
- **Best Practices**: 
  - Page Object Model (POM) pattern
  - Data-Driven Testing
  - Fixture Management
  - Comprehensive Logging
  - Custom Assertions
  - CI/CD Ready
- **Clean Code**: SOLID principles, type hints, comprehensive docstrings
- **Configuration Management**: Environment-based configuration
- **Reporting**: Detailed test reports with screenshots

## 📋 Project Structure

```
qa-automation-framework/
├── mobile/                          # Appium mobile testing framework
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   └── appium_config.py
│   ├── src/
│   │   ├── driver/
│   │   │   ├── driver_factory.py
│   │   │   └── driver_manager.py
│   │   ├── base/
│   │   │   ├── base_page.py
│   │   │   ├── base_test.py
│   │   │   └── wait_handler.py
│   │   ├── pages/
│   │   │   ├── home_page.py
│   │   │   ├── search_page.py
│   │   │   └── article_page.py
│   │   ├── models/
│   │   │   └── search_model.py
│   │   └── utils/
│   │       ├── logger.py
│   │       ├── assertions.py
│   │       └── screenshot.py
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_search.py
│   │   ├── test_navigation.py
│   │   └── test_article.py
│   ├── data/
│   │   └── test_searches.yaml
│   ├── .env.example
│   ├── pytest.ini
│   ├── requirements.txt
│   └── README.md
├── pwa/                            # Playwright PWA testing framework
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   └── browser_config.py
│   ├── src/
│   │   ├── browser/
│   │   │   ├── browser_factory.py
│   │   │   └── browser_manager.py
│   │   ├── base/
│   │   │   ├── base_page.py
│   │   │   ├── base_test.py
│   │   │   └── wait_handler.py
│   │   ├── pages/
│   │   │   ├── home_page.py
│   │   │   ├── products_page.py
│   │   │   └── cart_page.py
│   │   ├── models/
│   │   │   └── product_model.py
│   │   └── utils/
│   │       ├── logger.py
│   │       ├── assertions.py
│   │       ├── screenshot.py
│   │       └── decorators.py
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_navigation.py
│   │   ├── test_products.py
│   │   └── test_cart.py
│   ├── data/
│   │   └── test_products.yaml
│   ├── .env.example
│   ├── playwright.ini
│   ├── requirements.txt
│   └── README.md
├── docker-compose.yml
├── Dockerfile.appium
├── .github/workflows/
│   ├── mobile-tests.yml
│   └── pwa-tests.yml
├── scripts/
│   ├── setup.sh
│   ├── run_mobile_tests.sh
│   └── run_pwa_tests.sh
├── docs/
│   ├── SETUP.md
│   ├── MOBILE_SETUP.md
│   ├── PWA_SETUP.md
│   └── ARCHITECTURE.md
├── .gitignore
├── requirements.txt
└── pyproject.toml
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Java JDK (for Appium)
- Android SDK (for mobile testing)
- Docker & Docker Compose (optional)

### Installation

```bash
git clone https://github.com/DronovNA/qa-automation-framework.git
cd qa-automation-framework
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Mobile Testing (Appium)

```bash
cd mobile
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your configuration
pytest tests/ -v
```

### PWA Testing (Playwright)

```bash
cd pwa
pip install -r requirements.txt
cp .env.example .env
playwright install
pytest tests/ -v
```

## 📱 Test Targets

**Mobile**: [Wikipedia Android App](https://play.google.com/store/apps/details?id=org.wikipedia)
- Free, open-source
- Rich functionality for testing

**PWA**: [Swapy E-commerce Demo](https://demo.swapy.dev)
- Modern PWA with e-commerce features
- Publicly accessible

## 🏗️ Architecture Highlights

- **Page Object Model**: Centralized element locators and page methods
- **Data-Driven Testing**: Externalized test data in YAML/JSON
- **Fixture Management**: Proper setup/teardown with pytest fixtures
- **Custom Assertions**: Domain-specific assertions with detailed messages
- **Comprehensive Logging**: Request/response logging, test steps, error tracking
- **Screenshot Management**: Automatic screenshots on test failures

## 📚 Technologies

- **Mobile**: Python, Appium, PyTest, Android SDK
- **PWA**: Python, Playwright, PyTest
- **CI/CD**: GitHub Actions
- **Containerization**: Docker, Docker Compose
- **Configuration**: Python-dotenv, YAML, JSON

## 📖 Documentation

- [Setup Guide](docs/SETUP.md)
- [Mobile Setup Details](docs/MOBILE_SETUP.md)
- [PWA Setup Details](docs/PWA_SETUP.md)
- [Architecture Documentation](docs/ARCHITECTURE.md)

## 📄 License

MIT License

## 👤 Author

[Nikita Dronov](https://github.com/DronovNA)
