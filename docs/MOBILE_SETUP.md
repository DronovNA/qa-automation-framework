# Mobile Testing Framework - Detailed Setup

Detailed setup instructions for Appium-based mobile testing framework.

## Prerequisites

### Required Software

1. **Java Development Kit (JDK) 11+**
   - Download: https://adoptopenjdk.net/
   - Verify: `java -version`

2. **Android SDK**
   - Download: https://developer.android.com/studio
   - Set ANDROID_HOME environment variable
   - Verify: `adb devices`

3. **Appium Server**
   ```bash
   npm install -g appium@latest
   npm install -g appium-uiautomator2-driver
   
   appium --version
   ```

4. **Node.js 12+**
   - Download: https://nodejs.org/
   - Verify: `node --version`

## Installation Steps

### 1. Clone and Setup

```bash
cd qa-automation-framework/mobile
pip install -r requirements.txt
cp .env.example .env
```

### 2. Configure Environment Variables

Edit `mobile/.env`:

```bash
# Appium Server
APPIUM_HOST=localhost
APPIUM_PORT=4723
APPIUM_TIMEOUT=30

# Android Settings
ANDROID_PLATFORM_VERSION=12  # Your device version
ANDROID_DEVICE_NAME=emulator-5554  # From 'adb devices'
ANDROID_PACKAGE_NAME=org.wikipedia
ANDROID_ACTIVITY_NAME=org.wikipedia.main.MainActivity
ANDROID_AUTO_GRANT_PERMISSIONS=true

# Logging
LOG_LEVEL=INFO
REPORT_DIR=reports
SCREENSHOT_ON_FAILURE=true
```

### 3. Get Device Information

```bash
# List connected devices
adb devices

# Get device details
adb shell getprop ro.build.version.release  # Android version
adb shell getprop ro.serialno              # Serial number
```

### 4. Install Test Application

Install Wikipedia Android App:

```bash
# Via adb (requires APK file)
adb install wikipedia.apk

# Or manually on device
# Play Store → Wikipedia
```

## Starting Tests

### Local Appium Server

```bash
# Terminal 1: Start Appium
appium

# Terminal 2: Run tests
cd mobile
pytest tests/ -v
```

### Docker Appium Server

```bash
# Start Appium in Docker
cd ..
docker-compose up -d appium

# Run tests
cd mobile
APPIUM_HOST=localhost APPIUM_PORT=4723 pytest tests/ -v

# Stop Appium
docker-compose down
```

## Running Tests

### Basic Commands

```bash
# All tests
pytest tests/ -v

# Specific test file
pytest tests/test_search.py -v

# Specific test
pytest tests/test_search.py::TestSearch::test_search_valid_query -v

# Smoke tests only
pytest -m smoke -v

# Regression tests
pytest -m regression -v
```

### Advanced Options

```bash
# With HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html

# With coverage
pytest tests/ --cov=src --cov-report=html

# Parallel execution (requires pytest-xdist)
pytest tests/ -n 4  # 4 workers

# With timeout
pytest tests/ --timeout=300  # 5 minutes

# Stop on first failure
pytest tests/ -x
```

## Finding Element Locators

### Using Appium Inspector

1. Install Appium Inspector
2. Start Appium server
3. Open Appium Inspector
4. Connect to Appium server
5. Inspect elements on device

### Using Android Studio

1. Open Android Studio
2. Tools → Layout Inspector
3. Select running device/emulator
4. Inspect UI elements

### Using adb

```bash
# Dump UI hierarchy
adb shell uiautomator dump /sdcard/window_dump.xml

# Pull and view
adb pull /sdcard/window_dump.xml
cat window_dump.xml
```

## Common Issues and Solutions

### Appium Connection Failed

```bash
# Verify Appium is running
lsof -i :4723

# Check firewall
sudo ufw allow 4723

# Restart Appium
appium --reset-port
```

### Device Not Found

```bash
# List devices
adb devices

# Authorize device (if showing unauthorized)
adb authorize

# Reconnect device
adb disconnect
adb connect device_ip:5555
```

### Element Not Found

1. Use Appium Inspector to verify locator
2. Increase wait timeout in .env
3. Check app is installed and running
4. Verify activity name

### App Crashes

```bash
# View app logs
adb logcat

# Clear app data
adb shell pm clear org.wikipedia

# Reinstall app
adb uninstall org.wikipedia
adb install wikipedia.apk
```

## Performance Optimization

### Reduce Test Execution Time

```bash
# Parallel execution
pytest tests/ -n auto

# Run only smoke tests
pytest -m smoke

# Skip slow tests
pytest -m "not slow"
```

### Reduce Memory Usage

```bash
# Single browser instance
APPIUM_MAX_SESSIONS=1 pytest tests/

# Reduce screenshot resolution
# Edit settings.py: screenshot resolution
```

## Continuous Integration

See `.github/workflows/mobile-tests.yml` for CI/CD configuration.

Key points:
- Runs on push and pull requests
- Multiple test configurations
- Artifact uploads for reports
- Automatic failure notifications

## Support Resources

- [Appium Documentation](http://appium.io/docs/)
- [Android SDK Guide](https://developer.android.com/studio/)
- [Wikipedia Android App](https://www.mediawiki.org/wiki/Wikimedia_Apps)
