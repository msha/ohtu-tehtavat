import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_player_points(self):
        pisteet = self.statistics.search("Semenko").points
        self.assertEqual(pisteet, 16)
    
    def test_player_points2(self):
        pisteet = self.statistics.search("afhd")
        self.assertEqual(pisteet, None)

    def test_top_scorers(self):
        pelaajat = len(self.statistics.top_scorers(3))
        self.assertAlmostEqual(pelaajat, 4)

    def test_team(self):
        pelaajat = len(self.statistics.team("EDM"))
        self.assertAlmostEqual(pelaajat, 3)
