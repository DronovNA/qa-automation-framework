# QA Automation Framework - Setup Guide

Comprehensive setup guide for both mobile (Appium) and PWA (Playwright) testing frameworks.

## System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.9 or higher
- **Git**: Latest version
- **RAM**: 8GB minimum (16GB recommended)
- **Disk Space**: 10GB minimum

## Initial Setup

### 1. Clone Repository

```bash
git clone https://github.com/DronovNA/qa-automation-framework.git
cd qa-automation-framework
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Framework-Specific Setup

### Mobile Framework (Appium)

See [Mobile Setup Guide](MOBILE_SETUP.md) for detailed instructions.

Quick start:

```bash
cd mobile
pip install -r requirements.txt
cp .env.example .env
# Configure .env with your device settings
pytest tests/ -v
```

### PWA Framework (Playwright)

See [PWA Setup Guide](PWA_SETUP.md) for detailed instructions.

Quick start:

```bash
cd pwa
pip install -r requirements.txt
playwright install  # Install browsers
cp .env.example .env
pytest tests/ -v
```

## Docker Setup (Optional)

For Appium server in Docker:

```bash
# Start Appium container
docker-compose up -d appium

# Verify it's running
curl http://localhost:4723/wd/hub/status

# Run mobile tests
cd mobile
pytest tests/ -v

# Stop container
docker-compose down
```

## IDE Configuration

### PyCharm / IntelliJ IDEA

1. Open project
2. File → Project Structure → Project SDK → Add Python 3.9+
3. Configure test runner: Run → Edit Configurations → pytest
4. Set working directory to project root

### VSCode

1. Install Python extension
2. Select Python interpreter (venv)
3. Install pytest extension
4. Configure launch.json for debugging

## Configuration Files

### Root .env (Optional)

```bash
cp .env.example .env
```

Global environment variables for both frameworks.

### Mobile .env

```bash
cd mobile
cp .env.example .env
```

Configure Appium and Android settings.

### PWA .env

```bash
cd pwa
cp .env.example .env
```

Configure Playwright and browser settings.

## Verification

### Mobile Framework

```bash
cd mobile

# Run smoke tests
pytest -m smoke -v

# Check configuration
python -c "from config.settings import settings; print(f'Appium: {settings.appium_url}')"
```

### PWA Framework

```bash
cd pwa

# Run smoke tests
pytest -m smoke -v

# Verify Playwright
playwright install-deps
```

## Troubleshooting

### Python Version Issue

```bash
# Check Python version
python --version

# Ensure 3.9+
python3.10 -m venv venv
```

### Virtual Environment Issues

```bash
# Recreate venv
rm -rf venv
python -m venv venv
source venv/bin/activate  # macOS/Linux
```

### Import Errors

```bash
# Ensure you're in correct directory
cd mobile  # or cd pwa

# Verify PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Dependency Issues

```bash
# Upgrade pip, setuptools, wheel
pip install --upgrade pip setuptools wheel

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

## Next Steps

1. **Read framework-specific guides**:
   - [Mobile Setup](MOBILE_SETUP.md)
   - [PWA Setup](PWA_SETUP.md)

2. **Understand architecture**:
   - [Architecture Documentation](ARCHITECTURE.md)

3. **Run example tests**:
   ```bash
   cd mobile
   pytest tests/test_navigation.py -v
   ```

4. **Check logs**:
   ```bash
   tail -f logs/test_execution.log
   ```

5. **View reports**:
   ```bash
   open reports/report.html  # macOS
   start reports/report.html  # Windows
   ```
