# Playwright Python Automation Boilerplate

A clean and scalable **Playwright + Pytest test automation framework** built using the **Page Object Model (POM)** design pattern.

This boilerplate provides a solid foundation for building maintainable UI automation tests.

---

## Features

- Playwright UI automation
- Pytest test framework
- Page Object Model (POM)
- Environment variable configuration (.env)
- Automatic screenshots on test failure
- HTML test reports
- Clean and scalable project structure
- Easy to extend for CI/CD

---

## Project Structure

```
playwright-python-automation-boilerplate
│
├── pages
│   ├── base_page.py
│   └── login_page.py
│
├── tests
│   └── test_login.py
│
├── utils
│   └── screenshot.py
│
├── config
│   └── config.py
│
├── reports
│   └── screenshots
│
├── .env
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/playwright-python-automation-boilerplate.git
cd playwright-python-automation-boilerplate
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Mac / Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browsers

```bash
playwright install
```

---

## Environment Configuration

Create a `.env` file in the project root:

```
BASE_URL=https://example.com
USERNAME=test@example.com
PASSWORD=password123
```

---

## Running Tests

Run all tests

```bash
pytest
```

Run specific test

```bash
pytest tests/test_login.py
```

Run with verbose output

```bash
pytest -v
```

---

## Test Reporting

HTML reports are automatically generated.

Example location:

```
reports/report.html
```

Screenshots for failed tests are saved in:

```
reports/screenshots
```

---

## Example Test

```python
from pages.login_page import LoginPage
from config.config import BASE_URL

def test_login(browser_page):
    page = browser_page

    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login()

    assert "Dashboard" in page.title()
```

---

## Technologies Used

- Python
- Playwright
- Pytest
- python-dotenv

---

## Future Improvements

- Parallel test execution
- Allure reporting
- Video recording
- Playwright trace viewer
- CI/CD integration (GitHub Actions)

---

## Contributing

Pull requests are welcome. Feel free to open issues for suggestions or improvements.

---

## Author

Created by **Bonsa Desalegn**
