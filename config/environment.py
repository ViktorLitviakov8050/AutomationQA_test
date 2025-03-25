import os
import yaml
from typing import Dict, Any

class Environment:
    def __init__(self):
        self.config = self._load_config()
        self.env = os.getenv('ENVIRONMENT', 'local')
        self.base_url = self.config['environment'][self.env]['base_url']
        self.browser_config = self.config['browser']
        self.reporting_config = self.config['reporting']
        self.test_data = self.config['test_data']

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    @property
    def browser_name(self) -> str:
        return self.browser_config['name']

    @property
    def is_headless(self) -> bool:
        return self.browser_config['headless']

    @property
    def implicit_wait(self) -> int:
        return self.browser_config['implicit_wait']

    @property
    def explicit_wait(self) -> int:
        return self.browser_config['explicit_wait'] 