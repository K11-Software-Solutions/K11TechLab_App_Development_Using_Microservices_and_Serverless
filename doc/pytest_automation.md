# Pytest Automation for OpenAPI CRUD Microservice

## Features Implemented
- **Basic and Advanced Pytest Tests**: Covers all CRUD endpoints with assertions.
- **Parameterized Tests**: Easily test multiple product inputs and edge cases.
- **Fixtures**: Shared setup for Flask test client and reusable data.
- **Coverage Reports**: Generates both terminal and HTML coverage reports.
- **HTML Test Reports**: Self-contained HTML report for easy sharing.
- **CI Integration**: Ready for GitHub Actions or other CI/CD tools.

---

## Example: Parameterized Test
```python
import pytest

@pytest.mark.parametrize("product", [
    {"name": "Camera", "price": 250},
    {"name": "Headphones", "price": 120},
    {"name": "Microphone", "price": 80}
])
def test_add_product_param(client, product):
    response = client.post('/product', json=product)
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == product["name"]
    assert data["price"] == product["price"]
```

## Example: Fixture
```python
import pytest
from crud_api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
```

## Coverage & HTML Reports
- Run: `pytest --cov=crud_api --cov-report=html --html=pytest_report.html --self-contained-html`
- Coverage HTML: `htmlcov/index.html`
- Test HTML: `pytest_report.html`

## CI Integration (GitHub Actions)
Add to `.github/workflows/python-app.yml`:
```yaml
name: Python application
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest pytest-cov pytest-html flask flask-cors
    - name: Run tests
      run: |
        pytest --cov=crud_api --cov-report=term-missing --html=pytest_report.html --self-contained-html
```

## More Reporting Options
- `--cov-report=xml` for CI coverage integration
- `--html=report.html` for custom HTML output
- `--maxfail=1` to stop on first failure
- `-v` for verbose output

---

## References
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [Pytest-Cov](https://pytest-cov.readthedocs.io/en/latest/)
- [Pytest-HTML](https://pytest-html.readthedocs.io/en/latest/)
- [GitHub Actions](https://docs.github.com/en/actions)

This document summarizes all automation, testing, and reporting features for your OpenAPI CRUD microservice.
