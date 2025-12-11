# Quick Start Guide

Get started with QA Automation Framework in 5 minutes.

## Choose Your Framework

### Mobile Testing (Appium) - Wikipedia Android App
```bash
cd mobile
pip install -r requirements.txt
cp .env.example .env

# Configure Android device in .env
# Start Appium server: appium
# Run tests
pytest tests/ -v
```

### PWA Testing (Playwright) - E-Commerce Demo
```bash
cd pwa
pip install -r requirements.txt
playwright install
cp .env.example .env

# Run tests
pytest tests/ -v
```

## Using Makefile (Recommended)

```bash
# View all available commands
make help

# Install dependencies
make install

# Run all tests
make test

# Run mobile tests
make test-mobile

# Run PWA tests  
make test-pwa

# Code quality checks
make quality

# Format code
make format
```

## Using Docker (Mobile Tests)

```bash
# Start Appium server
docker-compose up -d appium

# Run mobile tests
cd mobile
pytest tests/ -v

# Stop Appium
docker-compose down
```

## Run Specific Tests

### Mobile Examples

```bash
cd mobile

# Smoke tests only
pytest -m smoke -v

# Search functionality tests
pytest tests/test_search.py -v

# Specific test method
pytest tests/test_search.py::TestSearch::test_search_valid_query -v
```

### PWA Examples

```bash
cd pwa

# Smoke tests only
pytest -m smoke -v

# Product tests
pytest tests/test_products.py -v

# Run with Firefox
BROWSER_TYPE=firefox pytest tests/ -v

# Run with headed browser (see UI)
pytest tests/ --headed -v
```

## View Reports

```bash
# Generate HTML report
pytest tests/ --html=../reports/report.html --self-contained-html

# Open report
open reports/report.html  # macOS
start reports/report.html  # Windows
```

## Project Structure

```
qa-automation-framework/
├── mobile/              # Appium framework
│   ├── config/         # Configuration
│   ├── src/            # Source code (driver, pages, utils)
│   ├── tests/          # Test cases
│   ├── data/           # Test data
│   └── requirements.txt
├── pwa/                # Playwright framework
│   ├── config/         # Configuration
│   ├── src/            # Source code (browser, pages, utils)
│   ├── tests/          # Test cases
│   ├── data/           # Test data
│   └── requirements.txt
├── docs/               # Documentation
├── scripts/            # Utility scripts
└── README.md          # Main documentation
```

## Configuration

### Mobile (.env)

```bash
APPIUM_HOST=localhost
APPIUM_PORT=4723
ANDROID_DEVICE_NAME=emulator-5554  # From 'adb devices'
ANDROID_PLATFORM_VERSION=12
```

### PWA (.env)

```bash
PWA_BASE_URL=https://demo.swapy.dev
BROWSER_TYPE=chromium  # chromium, firefox, webkit
BROWSER_HEADLESS=true
```

## Common Commands

```bash
# List connected Android devices
adb devices

# Install Playwright browsers
playwright install

# Start Appium server
appium

# Run tests with coverage
pytest tests/ --cov=src --cov-report=html

# Parallel test execution
pytest tests/ -n auto

# Run tests with detailed output
pytest tests/ -v -s

# Stop on first failure
pytest tests/ -x

# Show test names without running
pytest tests/ --collect-only
```

## Troubleshooting

### Mobile Tests Not Running

```bash
# Check Appium is running
lsof -i :4723

# Verify device connection
adb devices

# Check device version matches .env
adb shell getprop ro.build.version.release
```

### PWA Tests Timeout

```bash
# Increase timeout in .env
PLAYWRIGHT_TIMEOUT=60000

# Or run with slower execution
BROWSER_SLOWMO=500 pytest tests/ -v
```

### Import Errors

```bash
# Ensure you're in correct directory
cd mobile  # or cd pwa

# Check PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

## Next Steps

1. **Read full setup guide** → [SETUP.md](docs/SETUP.md)
2. **Framework details**:
   - [Mobile Framework](mobile/README.md)
   - [PWA Framework](pwa/README.md)
3. **Architecture overview** → [Architecture](docs/ARCHITECTURE.md)
4. **Contributing** → [Contributing Guidelines](CONTRIBUTING.md)

## Test Targets

**Mobile App**: Wikipedia Android Application
- Free, open-source
- Rich functionality
- Real-world testing

**PWA Demo**: Swapy E-Commerce Platform
- Modern PWA
- Publicly accessible
- E-commerce workflows

## Support

- 📖 Documentation: `/docs` folder
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions
- 📧 Contact: Project repository

Happy Testing! 🚀
