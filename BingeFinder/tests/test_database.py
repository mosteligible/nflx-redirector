import unittest

from shared import TEST_DB, DB_PAYLOAD


class TestDatabase(unittest.TestCase):
    def test_addentry(self):
        payload = DB_PAYLOAD.__dict__
        self.assertTrue(TEST_DB.AddEntry(payload))

    def test_entry_successful(self):
        from_db = TEST_DB.RetreiveMovie(netflixid=DB_PAYLOAD.NetflixId)
        payload = DB_PAYLOAD.__dict__
        for key, value in from_db.items():
            self.assertEqual(value, payload[key])

        result = TEST_DB.DeleteMovie(netflixid=DB_PAYLOAD.NetflixId)
        self.assertTrue(result)
