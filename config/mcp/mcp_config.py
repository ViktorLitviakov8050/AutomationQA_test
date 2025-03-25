import os
from dotenv import load_dotenv

load_dotenv()

# MCP Configuration
MCP_HOST = os.getenv('MCP_HOST', 'localhost')
MCP_PORT = int(os.getenv('MCP_PORT', '8080'))
MCP_USERNAME = os.getenv('MCP_USERNAME', 'admin')
MCP_PASSWORD = os.getenv('MCP_PASSWORD', 'admin')

# Test Environment Configuration
ENVIRONMENT = os.getenv('ENVIRONMENT', 'local')
TEST_BROWSER = os.getenv('TEST_BROWSER', 'chrome')
TEST_PLATFORM = os.getenv('TEST_PLATFORM', 'macos')

# MCP Endpoints
MCP_BASE_URL = f'http://{MCP_HOST}:{MCP_PORT}'
MCP_API_URL = f'{MCP_BASE_URL}/api/v1'
MCP_AUTH_URL = f'{MCP_BASE_URL}/auth' 