import rockgame
from unittest import TestCase

class TestrockgameGame(TestCase):

    # Print resultz
    def test_who_won(self):
        
        resultz = rockgame.whowon(1,1)
        self.assertEqual(resultz, 'TIE!')

        resultz = rockgame.whowon(1,2)
        self.assertEqual(resultz, 'Computer wins! Paper beats rock!')

        resultz = rockgame.whowon(1,3)
        self.assertEqual(resultz, 'Player wins! Rock beats scissors!')

        resultz = rockgame.whowon(2,3)
        self.assertEqual(resultz, 'Computer wins! Scissors beats paper!')

        resultz = rockgame.whowon(2,1)
        self.assertEqual(resultz, 'Player wins! Paper beats rock!')

        resultz = rockgame.whowon(3,2)
        self.assertEqual(resultz, 'Player wins! Scissors beats paper!')

        resultz = rockgame.whowon(3,1)
        self.assertEqual(resultz, 'Computer wins! Rock beats scissors!')

    def test_get_comp_choice(self):

        resultz = rockgame.get_comp_choice()
        self.assertIn((resultz),(1,2,3))

        resultz = rockgame.get_comp_choice()
        self.assertNotIn((resultz),(4,5,6))
