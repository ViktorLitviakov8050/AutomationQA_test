import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base URL for the application
BASE_URL = os.getenv('BASE_URL', 'http://localhost:3000')

# Browser configuration
BROWSER = os.getenv('BROWSER', 'chrome')
HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'

# Test configuration
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20

# Screenshot configuration
SCREENSHOT_DIR = 'test-results/screenshots'
REPORT_DIR = 'test-results/reports' 