# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability in this project, **do not open a public GitHub issue**. Instead:

**Email**: security@qa-automation.dev

Include:
- Description of the vulnerability
- Affected component(s)
- Steps to reproduce (if applicable)
- Potential impact
- Suggested fix (optional)

## Security Best Practices

### Handling Credentials

1. **Never hardcode secrets**
   ```bash
   # Bad
   APPIUM_HOST = "http://user:password@appium.example.com"
   API_KEY = "sk_test_1234567890"
   
   # Good
   APPIUM_HOST = os.getenv("APPIUM_HOST")
   API_KEY = os.getenv("API_KEY")
   ```

2. **Use .env files locally**
   ```bash
   cp .env.example .env  # Never commit .env
   ```

3. **Use GitHub Secrets in CI/CD**
   ```yaml
   - name: Run tests
     env:
       APPIUM_HOST: ${{ secrets.APPIUM_HOST }}
       API_KEY: ${{ secrets.API_KEY }}
   ```

### Logging and Debugging

1. **Mask sensitive data in logs**
   ```python
   # Bad
   logger.info(f"Token: {token}")
   
   # Good
   logger.info(f"Token: {token[:8]}...")
   ```

2. **Don't log passwords or tokens**
   ```python
   # Check loguru/requests configs
   # Avoid DEBUG level logging in production
   ```

3. **Use DEBUG level selectively**
   ```python
   if os.getenv("DEBUG"):
       logger.enable("debug_mode")
   ```

### Code Quality and Security Tools

#### Dependency Scanning
```bash
# Check for known vulnerabilities
pip audit
pip install safety && safety check

# Check specific package
pip show appium-python-client
```

#### Secret Detection
```bash
# Pre-commit hooks scan for secrets
pre-commit run --all-files

# Manual scan with detect-secrets
pip install detect-secrets
detect-secrets scan
```

#### Security Analysis
```bash
# Bandit for Python security issues
bandit -r mobile/src pwa/src

# CodeQL analysis (runs in CI)
# See .github/workflows/codeql.yml
```

#### Code Style and Type Safety
```bash
# Linting
flake8 mobile/src pwa/src

# Type checking
mypy mobile/src pwa/src

# Format check
black --check mobile/ pwa/
```

### For Test Code

1. **Validate element states**
   ```python
   element = wait.until(EC.presence_of_element_located(locator))
   assert element.is_enabled(), "Element should be clickable"
   ```

2. **Check SSL certificates (Playwright)**
   ```python
   browser = await playwright.chromium.launch(
       args=["--disable-blink-features=AutomationControlled"]
   )
   ```

3. **Verify URLs before navigation**
   ```python
   if url.startswith("https://"):
       page.goto(url)
   else:
       raise ValueError("Only HTTPS URLs allowed")
   ```

### For CI/CD

1. **GitHub Actions Secrets are encrypted**
   - Store API keys, tokens, passwords as secrets
   - Never print secrets in logs
   - Use minimal permissions (read-only by default)

2. **Branch Protection**
   - Require reviews for main branch
   - Require CI checks to pass
   - Dismiss stale PR reviews

3. **Dependabot Configuration**
   - Automated security updates weekly
   - See .github/dependabot.yml

### Environment Configuration

Example .env structure:
```bash
# Mobile (Appium)
APPIUM_HOST=http://localhost:4723
APPIUM_PLATFORM=Android
APPIUM_AUTOMATION_NAME=UiAutomator2

# PWA (Playwright)
BROWSER_TYPE=chromium
BASE_URL=https://example.com

# Testing
TEST_TIMEOUT=30
LOG_LEVEL=INFO

# CI/CD (set via GitHub Secrets)
API_TOKEN=xxx
SLACK_WEBHOOK=xxx
```

## Automated Security Checks

The repository runs automated security scanning:

| Check | Tool | Frequency |
|-------|------|----------|
| Secret Detection | TruffleHog | On push, weekly |
| Vulnerability Scan | CodeQL | On push, weekly |
| Dependency Updates | Dependabot | Weekly |
| Code Quality | Black, isort, flake8, mypy | Every push |
| Security Linting | bandit | On pre-commit |

## Known Vulnerabilities

None currently known. Security issues should be reported privately via email.

## Security Updates

- **Critical**: Released immediately
- **High**: Released in next patch
- **Medium**: Released in next minor release
- **Low**: Released in next major release

## Related Documents

- [CONTRIBUTING.md](CONTRIBUTING.md) — Development guidelines
- [README.md](README.md) — Project overview
- [.github/workflows/ci.yml](.github/workflows/ci.yml) — CI pipeline
- [.github/dependabot.yml](.github/dependabot.yml) — Dependency management

## Resources

- [OWASP Top 10](https://owasp.org/)
- [Python Security](https://docs.python.org/3/library/security_warnings.html)
- [Playwright Security](https://playwright.dev/python/docs/security)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)

## Scope

This security policy applies to:
- Core framework code and official repositories
- Dependencies declared in requirements.txt
- GitHub workflows and automation

Not included:
- User-written test code in projects using this framework
- Third-party services and integrations
- Cloud/SaaS infrastructure
