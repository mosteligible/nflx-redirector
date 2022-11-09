import unittest
from utils import (
    formatString,
    getShowDetails,
)

from data import MOVIE_DETAILS, MOVIE_DETAILS_OUTPUT

class TestUtils(unittest.TestCase):
    maxDiff: int | None = None

    def test_formarString(self):
        inputs = [
            "a sentence that starts with noth\\'ing is don\\'t right",
            "this isn\\'t right, expect exclamation! or backslash\ double \\",
            "A test Sentence\\ to check sentence"
        ]
        expected = [
            "a sentence that starts with noth'ing is don't right",
            "this isn't right, expect exclamation! or backslash\ double \\",
            "A test Sentence\\ to check sentence"
        ]

        for index, inputSentence in enumerate(inputs):
            outputSentence = formatString(inputSentence)
            self.assertEqual(outputSentence, expected[index])

    def test_getShowDetails(self):
        for index, detail in enumerate(MOVIE_DETAILS):
            outputDetail = getShowDetails(detail)
            self.assertDictEqual(MOVIE_DETAILS_OUTPUT[index], outputDetail)
