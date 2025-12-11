#!/bin/bash

set -e

echo "Running Mobile Tests (Appium)"
echo "============================="
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Change to mobile directory
cd mobile

# Run tests
echo "Starting tests..."
pytest tests/ -v --tb=short --html=../reports/mobile_report.html --self-contained-html

echo ""
echo "============================="
echo "Tests completed!"
echo "Report: reports/mobile_report.html"
echo "============================="
