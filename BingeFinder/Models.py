from dataclasses import dataclass
from datetime import datetime


@dataclass
class Endpoints:
    Service: str
    Endpoint: str
    Referer: str


@dataclass
class ShowDetails:
    Title: str
    ReleaseDate: datetime
    Type: str
    Rating: str
    Quality: str
    Starring: str
    Category: str
    Runtime: str
    NetflixId: str
    Language: str
    Description: str
    Director: str
    Imdb: str
