from pathlib import Path

import yaml
from Database import Database

WORK_DIR = Path(__file__).resolve().parent.parent
TEST_DIR = WORK_DIR / "tests"

with open(TEST_DIR / "test.yaml", "r") as fp:
    yamlConfig = yaml.safe_load(fp)

USER_AGENT = yamlConfig["user_agent"]
DB_USERNAME = yamlConfig["db_username"]
DB_PASSWORD = yamlConfig["db_password"]
DB_HOST = yamlConfig["db_host"]
DB_NAME = yamlConfig["db_name"]
DB_PORT = yamlConfig["db_port"]
TABLE_NAME = yamlConfig["db_table_name"]

TEST_DB = Database(
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_NAME,
    table_name=TABLE_NAME,
)
