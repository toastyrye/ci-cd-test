# ci-cd-test
# Setup Process
git checkout development branch
Download: https://www.python.org/downloads/release/python-385/
Create virtual environment
    python3 -m venv /path/to/new/virtual/environment/ci-cd-test
Install development dependencies
    pip install -r requirements.txt
Activate automated pre-commit hooks
    pre-commit install
Test tox environment
    tox
Begin developing!

# Development Process
Checkout feature-branch from development branch
Make a change
Write test for appropriate coverage
Tox until clean
Commit
Pull request
