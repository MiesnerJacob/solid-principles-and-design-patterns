import json

class ConfigManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.config = {}

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            self.config = json.load(file)

    def get_setting(self, key):
        return self.config[key]

# Create a sample JSON configuration file named 'config.json'
sample_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "password": "password"
    },
    "api": {
        "host": "0.0.0.0",
        "port": 8000
    }
}

with open("config.json", "w") as f:
    json.dump(sample_config, f)


if __name__ == "__main__":
    # Testing the singleton behavior and config management
    config1 = ConfigManager()
    config2 = ConfigManager()

    print(f"config1: {id(config1)}")
    print(f"config2: {id(config2)}")

    config1.load_config("config.json")
    print(config1.get_setting("database"))
    print(config2.get_setting("api"))