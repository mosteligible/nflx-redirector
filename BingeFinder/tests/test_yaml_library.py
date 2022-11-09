import unittest

import yaml
from shared import TEST_DIR


class TestYaml(unittest.TestCase):
    def test_yaml_config(self):
        test_config_file = TEST_DIR / "test_config.yaml"
        expected_output = {
            "db_host": "hostaddress",
            "db_name": "db_name",
            "db_password": "myauthenticationstringfordb$&123",
            "db_port": "port_no",
            "db_table_name": "table_name",
            "db_username": "username",
            "platform": [
                {
                    "streaming_service": {
                        "category_1": {
                            "endpoint": "https://www.urltoservice1.com/api/version/endpoint.html",
                            "referer": "https://www.urltoservice2.com/",
                        },
                        "category_2": {
                            "endpoint": "https://www.urltoservice1.com/api/version/endpoint.html",
                            "referer": "https://www.urltoservice2.com/",
                        },
                    }
                }
            ],
            "user_agent": "something that is sending request",
        }
        with open(test_config_file, "r") as fp:
            generated = yaml.safe_load(fp)
        self.assertEqual(generated, expected_output)
