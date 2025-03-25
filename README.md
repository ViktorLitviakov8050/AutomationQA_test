# Automation QA Test Project

This project contains automated tests for QA purposes.

## Project Structure
```
AQA_tests/
├── src/                    # Source code
│   ├── pages/             # Page objects
│   ├── tests/             # Test cases
│   └── utils/             # Utility functions
├── config/                # Configuration files
├── docs/                  # Documentation
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Setup
1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests
```bash
pytest src/tests/
```
