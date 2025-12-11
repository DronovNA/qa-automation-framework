#!/bin/bash

set -e

echo "QA Automation Framework Setup"
echo "============================="
echo ""

# Check Python version
echo "Checking Python version..."
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "Python version: $PYTHON_VERSION"

if [[ "$PYTHON_VERSION" < "3.9" ]]; then
    echo "ERROR: Python 3.9 or higher required"
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created"
else
    echo "Virtual environment already exists"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip setuptools wheel

# Install dependencies
echo "Installing dependencies..."
echo ""
echo "1. Mobile framework dependencies..."
cd mobile
pip install -r requirements.txt
cd ..

echo ""
echo "2. PWA framework dependencies..."
cd pwa
pip install -r requirements.txt
playwright install
cd ..

# Create environment files
echo ""
echo "Creating environment configuration files..."

if [ ! -f "mobile/.env" ]; then
    cp mobile/.env.example mobile/.env
    echo "Mobile .env created"
else
    echo "Mobile .env already exists"
fi

if [ ! -f "pwa/.env" ]; then
    cp pwa/.env.example pwa/.env
    echo "PWA .env created"
else
    echo "PWA .env already exists"
fi

# Create reports directory
echo ""
echo "Creating reports directory..."
mkdir -p reports

echo ""
echo "============================="
echo "Setup completed successfully!"
echo "============================="
echo ""
echo "Next steps:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Configure mobile/.env with your Android settings"
echo "3. Configure pwa/.env with your PWA settings"
echo "4. For mobile: Start Appium server (appium)"
echo "5. Run tests: pytest mobile/tests/ -v"
echo ""
