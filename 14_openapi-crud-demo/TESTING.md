# Testing & Automation for OpenAPI CRUD Microservice

## Test Suite Overview
- All endpoints are covered with pytest tests
- Parameterized tests for multiple product inputs
- Shared fixture for Flask test client
- Coverage and HTML reports generated automatically

---

## How to Run Tests

### Basic Test Run
```sh
pytest test_crud_api_pytest.py -v
```

### Run with Coverage & HTML Report
```sh
pytest --cov=crud_api --cov-report=html --html=pytest_report.html --self-contained-html test_crud_api_pytest.py -v
```

- Coverage HTML report: `htmlcov/index.html`
- Test HTML report: `pytest_report.html`

---

## Example Output

### Terminal Output
```
test_crud_api_pytest.py::test_add_product_param[product0] PASSED
...
========================================== tests coverage =========================================
Name          Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------
crud_api.py      32      4      6      1    87%   47-49, 52
---------------------------------------------------------
TOTAL            32      4      6      1    87%
======================================== 8 passed in 0.24s =========================================
```

### HTML Report
- Open `pytest_report.html` in your browser for a detailed, shareable test report
- Open `htmlcov/index.html` for coverage details

---

## Advanced Features
- Parameterized tests: Easily add more product cases
- Fixtures: Shared setup for all tests
- CI/CD ready: Integrate with GitHub Actions or other CI tools
- Custom reporting: Use `--cov-report=xml` or other formats as needed

---

## References
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [Pytest-Cov](https://pytest-cov.readthedocs.io/en/latest/)
- [Pytest-HTML](https://pytest-html.readthedocs.io/en/latest/)

This README documents all testing, automation, and reporting features for this microservice.
