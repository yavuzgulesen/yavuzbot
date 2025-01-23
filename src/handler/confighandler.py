import yaml

class Config:
    def __init__(self, config_file='../config.yaml'):
        self.config_data = self._load_config(config_file)

    def _load_config(self, config_file):
        with open(config_file, 'r') as file:
            return yaml.safe_load(file)

    def get(self, section, key):
        # Retrieve a specific key from a section
        return self.config_data.get(section, {}).get(key)