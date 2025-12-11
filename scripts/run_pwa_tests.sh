#!/bin/bash

set -e

echo "Running PWA Tests (Playwright)"
echo "============================="
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Change to pwa directory
cd pwa

# Run tests
echo "Starting tests..."
pytest tests/ -v --tb=short --html=../reports/pwa_report.html --self-contained-html

echo ""
echo "============================="
echo "Tests completed!"
echo "Report: reports/pwa_report.html"
echo "============================="
