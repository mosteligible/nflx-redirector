from typing import Dict

import yaml
from Log import APP_LOGGER
from Models import ShowDetails


def ReadYamlConfig():
    with open("config.yaml", "r") as fp:
        config = yaml.safe_load(fp)
    return config


def formatString(sentence: str):
    sentence = sentence.replace("\\'", "'")
    return sentence


def getShowDetails(item: Dict) -> Dict:
    imdbRating = item.get("imdb")
    try:
        """
        imdb ratings are provided one of two ways, either as float
        between 0 and 10 or as fraction: 5/10 or 7/10.
        If its a float number, string to float will work, else split
        based on front slash "/" and take the first number.
        """
        if imdbRating is None or imdbRating == "":
            imdbRating = 0.0
        else:
            imdbRating = float(imdbRating)
    except ValueError:
        if "n/a" in imdbRating.lower():
            imdbRating = 0.0
        elif "/" in imdbRating:
            imdbRating = imdbRating.split("/")[0]
        else:
            imdbRating = 0.0

    data = ShowDetails(
        Starring=formatString(item.get("actors")),
        Category=formatString(item.get("category")),
        ReleaseDate=item.get("date_released"),
        Description=formatString((item.get("description"))),
        Director=formatString(item.get("director")),
        Imdb=imdbRating,
        Language=item.get("language"),
        NetflixId=item.get("netflixid"),
        Quality=item.get("quality"),
        Rating=item.get("rating"),
        Runtime=item.get("runtime"),
        Title=item.get("title"),
        Type=item.get("type"),
    )
    return data.__dict__
