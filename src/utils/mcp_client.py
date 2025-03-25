import requests
from config.mcp.mcp_config import MCP_API_URL, MCP_AUTH_URL, MCP_USERNAME, MCP_PASSWORD

class MCPClient:
    def __init__(self):
        self.session = requests.Session()
        self.token = None
        self._authenticate()

    def _authenticate(self):
        """Authenticate with MCP server"""
        response = self.session.post(
            MCP_AUTH_URL,
            json={
                'username': MCP_USERNAME,
                'password': MCP_PASSWORD
            }
        )
        if response.status_code == 200:
            self.token = response.json().get('token')
            self.session.headers.update({'Authorization': f'Bearer {self.token}'})
        else:
            raise Exception(f"Authentication failed: {response.text}")

    def get_test_status(self, test_id):
        """Get status of a specific test"""
        response = self.session.get(f"{MCP_API_URL}/tests/{test_id}")
        return response.json()

    def update_test_status(self, test_id, status, details=None):
        """Update status of a specific test"""
        payload = {'status': status}
        if details:
            payload['details'] = details
        response = self.session.put(f"{MCP_API_URL}/tests/{test_id}", json=payload)
        return response.json()

    def get_test_results(self, test_run_id):
        """Get results for a specific test run"""
        response = self.session.get(f"{MCP_API_URL}/test-runs/{test_run_id}/results")
        return response.json() 