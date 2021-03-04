import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):

# Test we get the right result string for a final score dictionary representing - # Home win # Away win # Draw
    def test_result(self):
        result_1 = get_result({"home score": 3,"away score": 1})
        result_2 = get_result({"home score": 0,"away score": 4})
        self.assertEqual("HOME WIN", result_1)
        self.assertEqual("AWAY WIN", result_2)
        self.assertEqual("DRAW", get_result({"home score": 3,"away score": 3}))         # Alternatively, just put into second argument

# Test we get right list of result strings for a list of final score dictionaries. 
    def test_multiple_results(self):
        football_results = get_results([{"home score": 3,
            "away score": 1},
            {"home score": 0,
            "away score": 2},
            {"home score": 4,
            "away score": 4}])
        self.assertEqual(["HOME WIN","AWAY WIN","DRAW"],football_results)

if __name__ == "__main__":
    unittest.main()
