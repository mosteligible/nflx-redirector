from pathlib import Path
from datetime import datetime

import yaml
from Database import Database
from Models import ShowDetails


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

DB_PAYLOAD = ShowDetails(
            Title="movie_title",
            ReleaseDate=datetime(year=2020, month=10, day=20),
            Type="movie_type",
            Rating="movie_rating",
            Quality="movie_quality",
            Starring="Tom Cruise",
            Category="movie_category",
            Runtime="99 mins",
            NetflixId="1234567890",
            Language="English",
            Description="An elaborate description of movie",
            Director="Tom Cruise",
            Imdb=7.5,
        )

TEST_DB = Database(
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_NAME,
    table_name=TABLE_NAME,
)
