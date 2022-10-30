from dataclasses import dataclass

from Database import Database
from utils import ReadYamlConfig

yamlConfig = ReadYamlConfig()


@dataclass
class Endpoints:
    Endpoint: str
    Referer: str


NETFLIX_DATA = Endpoints(
    Endpoint=yamlConfig["netflix"]["movie"]["endpoint"],
    Referer=yamlConfig["netflix"]["movie"]["referer"],
)
USER_AGENT = yamlConfig["user_agent"]
DB_USERNAME = yamlConfig["db_username"]
DB_PASSWORD = yamlConfig["db_password"]
DB_HOST = yamlConfig["db_host"]
DB_NAME = yamlConfig["db_name"]
DB_PORT = yamlConfig["db_port"]
TABLE_NAME = yamlConfig["db_table_name"]

SHOW_DB = Database(
    username=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST, database=DB_NAME
)
