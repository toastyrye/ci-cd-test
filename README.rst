# ci-cd-test
# Setup Process
git checkout development branch
Download: https://www.python.org/downloads/release/python-385/
Create virtual environment
    python3 -m venv /path/to/new/virtual/environment/ci-cd-test
Install development dependencies
    pip install -r requirements.txt
Checkout development branch
Test tox environment
    tox
Activate automated pre-commit hooks
    pre-commit install
Begin developing!

# Development Process
Checkout feature-branch from development branch
Make a change
Write test for appropriate coverage
Tox until clean
Commit
Pull request
