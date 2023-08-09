import unittest
from unittest.mock import Mock
import blackjack


class TestCardValues(unittest.TestCase):
    def test_blackjack_as(self):
        deck_mock = Mock(spec=blackjack.Deck)
        deck_mock.get_ini_cards.return_value = ["1P", "13C"]
        player = blackjack.Player(deck_mock.get_ini_cards())
        self.assertEqual(21, player.get_cards_value(), "Should be blackjack")

    def test_as_value(self):
        deck_mock = Mock(spec=blackjack.Deck)
        deck_mock.get_ini_cards.return_value = ["1P", "13C", "12P"]
        player = blackjack.Player(deck_mock.get_ini_cards())
        self.assertEqual(21, player.get_cards_value(), "Should be blackjack")

    def test_card_value_calculator(self):
        deck_mock = Mock(spec=blackjack.Deck)
        deck_mock.get_ini_cards.return_value = ["1P", "7H", "12P"]
        player = blackjack.Player(deck_mock.get_ini_cards())
        self.assertEqual(18, player.get_cards_value(), "Should be 18")

    def test_card_value_over_21(self):
        deck_mock = Mock(spec=blackjack.Deck)
        deck_mock.get_ini_cards.return_value = ["13P", "7H", "12P"]
        player = blackjack.Player(deck_mock.get_ini_cards())
        game = blackjack.Game()
        self.assertEquals(True, game.over_21(player), "Should be passed")


if __name__ == "__main__":
    unittest.main()
    print("Test pasados")
