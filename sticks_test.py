import unittest
from sticks import *

player1 = "John"
stick_count = 20

class TestMysteryWord(unittest.TestCase):


    def test_pick_up_sticks(self):
        self.assertEqual(make_move(player1,2), 18 )

    def test_game_over(self):
        self.assertEqual(game_complete(stick_count),False)
        self.assertEqual(game_complete(0),True)
        self.assertEqual(game_complete(-2),True)

    # def test_player_vs_player(self):


    # def test_medium_words(self):
    #     self.assertEqual(medium_words(word_list), ["stream", "kneecap", "cookbook", "language", "sneaker"])
    #
    #
    # def test_hard_words(self):
    #     self.assertEqual(hard_words(word_list), ["cookbook", "language", "algorithm", "integration"])
    #
    #
    # def test_random_word(self):
    #     """This test is not very good. Testing things that are random is hard,
    #     in that there's not a predictable choice. The best we can do is make
    #     sure we have valid output."""
    #     word = random_word(word_list)
    #     self.assertTrue(word in word_list)
    #
    #
    # def test_display_word(self):
    #     word = "integration"
    #     self.assertEqual(display_word(word, []), "_ _ _ _ _ _ _ _ _ _ _")
    #     self.assertEqual(display_word(word, ["z"]), "_ _ _ _ _ _ _ _ _ _ _")
    #     self.assertEqual(display_word(word, ["g"]), "_ _ _ _ G _ _ _ _ _ _")
    #     self.assertEqual(display_word(word, ["i"]), "I _ _ _ _ _ _ _ I _ _")
    #     self.assertEqual(display_word(word, ["i", "g"]), "I _ _ _ G _ _ _ I _ _")
    #     self.assertEqual(display_word(word, ["i", "n", "z"]), "I N _ _ _ _ _ _ I _ N")
    #
    #
    # def test_is_word_complete(self):
    #     word = "river"
    #     self.assertFalse(is_word_complete(word, []))
    #     self.assertFalse(is_word_complete(word, ["r"]))
    #     self.assertFalse(is_word_complete(word, ["r", "e"]))
    #     self.assertFalse(is_word_complete(word, ["r", "e", "z"]))
    #     self.assertTrue(is_word_complete(word, ["r", "e", "v", "i"]))

if __name__ == '__main__':
    unittest.main()
