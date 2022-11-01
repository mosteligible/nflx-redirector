from Database import Database
from Log import APP_LOGGER
from Models import Endpoints
from utils import ReadYamlConfig

yamlConfig = ReadYamlConfig()


COLLECTION = []

for platform in yamlConfig["platform"]:
    for streamSrv, data in platform.items():
        collectionEndpoint = Endpoints(
            Service=streamSrv,
            Endpoint=data["movie"]["endpoint"],
            Referer=data["movie"]["referer"],
        )
        COLLECTION.append(collectionEndpoint)

USER_AGENT = yamlConfig["user_agent"]
DB_USERNAME = yamlConfig["db_username"]
DB_PASSWORD = yamlConfig["db_password"]
DB_HOST = yamlConfig["db_host"]
DB_NAME = yamlConfig["db_name"]
DB_PORT = yamlConfig["db_port"]
TABLE_NAME = yamlConfig["db_table_name"]

SHOW_DB = Database(
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_NAME,
    table_name=TABLE_NAME,
)

APP_LOGGER.info("Successfully initialized..")
