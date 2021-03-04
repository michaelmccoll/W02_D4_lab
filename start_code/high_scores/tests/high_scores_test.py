import unittest

# from src.high_scores import latest, personal_best, personal_top_three

from src.high_scores import *

class HighScoresTest(unittest.TestCase):
    # Test latest score (the last thing in the list)
    def test_latest_scores(self):
        scores = [23,43,565,34,656,76,56,5]
        self.assertEqual(5, latest_score(scores))

    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        scores = [23,43,565,34,656,76,56,5]
        self.assertEqual(656, personal_best(scores))

    # Test top three from list of scores
    def test_top_three(self):
        scores = [23,43,565,34,656,76,56,5]
        top_three = [656,565,76]
        self.assertEqual(top_three, personal_top_three(scores))

    # Test ordered from highest to lowest
    def test_highest_to_lowest(self):
        scores = [23,43,565,34,656,76,56,5]
        scores_reversed = [656,565,76,56,43,34,23,5]
        self.assertEqual(scores_reversed, highest_to_lowest(scores))
        
    # Test top three when there is a tie
    def test_top_three_tie(self):
        scores = [20,10,20,15,16,20]
        self.assertEqual([20,20,20],personal_top_three(scores))

    # Test top three when there are less than three
    def test_top_three_when_less_then_3(self):
        scores = [20,10,20,15,16]
        self.assertEqual([20,20,16],personal_top_three(scores))

    # Test top three when there is only one
    def test_top_three_when_only_1(self):
        scores = [20,10,12,15,16]
        self.assertEqual([20,16,15],personal_top_three(scores))
