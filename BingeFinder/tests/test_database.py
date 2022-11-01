import unittest
from datetime import datetime

from Models import ShowDetails
from utils import TEST_DB


class TestDatabase(unittest.TestCase):
    def test_addentry(self):
        db_payload = ShowDetails(
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
        self.payload = db_payload.__dict__
        self.assertTrue(TEST_DB.AddEntry(self.payload))

    def test_entry_successful(self):
        from_db = TEST_DB.RetreiveMovie(netflixid=self.payload["netflixid"])
        for key, value in from_db.items():
            self.assertEqual(value, self.payload[key])
