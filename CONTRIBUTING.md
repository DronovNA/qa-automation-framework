# Contributing to QA Automation Framework

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Focus on code quality and best practices
- Help others learn and grow
- Report issues through proper channels

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone <your-fork-url>`
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Set up development environment (see SETUP.md)

## Development Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use type hints for all functions
- Maximum line length: 100 characters
- Use meaningful variable names
- Add docstrings to all public methods

### Code Quality

```bash
# Format code with Black
black src/ tests/

# Sort imports with isort
isort src/ tests/

# Lint with flake8
flake8 src/ tests/

# Type check with mypy
mypy src/
```

### Testing

- Write tests for new features
- Update existing tests when changing behavior
- Ensure all tests pass: `pytest tests/ -v`
- Aim for >80% code coverage
- Use meaningful test names

### Commit Messages

Follow conventional commits:

```
type(scope): description

Detailed explanation if needed.

Issue: #123
```

Types: feat, fix, docs, style, refactor, test, chore

Example:
```
feat(mobile): add element wait handler

Implement WaitHandler class with explicit wait strategies
for reliable element interaction in mobile tests.

Issue: #42
```

### Pull Request Process

1. Update tests and documentation
2. Run tests locally and ensure they pass
3. Create descriptive pull request title and description
4. Link related issues
5. Request review from maintainers
6. Address review feedback
7. Squash commits if requested

## Issue Reporting

### Before Creating an Issue

- Search existing issues
- Check documentation
- Try running latest version
- Check CI/CD logs

### Creating an Issue

Provide:

1. **Clear description** - What is the issue?
2. **Steps to reproduce** - How to replicate it?
3. **Expected behavior** - What should happen?
4. **Actual behavior** - What actually happens?
5. **Environment** - OS, Python version, browser
6. **Screenshots/logs** - If applicable

## Feature Requests

Describe:

1. **Use case** - Why do you need this?
2. **Current workaround** - How do you currently solve it?
3. **Proposed solution** - How should it work?
4. **Alternative solutions** - Other approaches?

## Documentation

- Update relevant documentation files
- Add docstrings to code
- Include examples for new features
- Keep README.md current
- Update CHANGELOG if applicable

## Areas to Contribute

### High Priority

- Bug fixes
- Performance improvements
- Test coverage
- Documentation
- Security issues

### Welcome Contributions

- New page objects
- Additional test cases
- CI/CD improvements
- Docker optimizations
- Example scripts

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

- Open an issue with [question] tag
- Check documentation
- Review existing code examples

Thank you for contributing!
