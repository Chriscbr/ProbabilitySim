import unittest
import ttt_gamestate


class TestTTTGameState(unittest.TestCase):

    def test_str(self):
        t0 = ttt_gamestate.TTTGameState()
        self.assertEqual(str(t0), '[- - -]\n'
                                  '[- - -] (X to move)\n'
                                  '[- - -]')

    def test_repr(self):
        t0 = ttt_gamestate.TTTGameState()
        self.assertEqual(repr(t0),
                         'ttt_gamestate.TTTGameState([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0)')

    def test_is_valid_state(self):
        t0 = ttt_gamestate.TTTGameState([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(t0.is_valid_state(), True)
        t1 = ttt_gamestate.TTTGameState([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
        self.assertEqual(t1.is_valid_state(), True)

    def test_replace_with(self):
        t0 = ttt_gamestate.TTTGameState([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        t1 = t0.replace_with(0, 0, 1)
        self.assertEqual(t0, ttt_gamestate.TTTGameState([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
        self.assertEqual(t1, ttt_gamestate.TTTGameState([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))

    def test_get_next_states(self):
        t0 = ttt_gamestate.TTTGameState([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        list_t = t0.get_next_states()
        self.assertEqual(list_t,
                         [ttt_gamestate.TTTGameState([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
                          ttt_gamestate.TTTGameState([[0, 1, 0], [0, 0, 0], [0, 0, 0]], 0),
                          ttt_gamestate.TTTGameState([[0, 0, 1], [0, 0, 0], [0, 0, 0]], 0),
                          ttt_gamestate.TTTGameState([[0, 0, 0], [1, 0, 0], [0, 0, 0]], 0),
                          ttt_gamestate.TTTGameState([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 0),
                          ttt_gamestate.TTTGameState([[0, 0, 0], [0, 0, 1], [0, 0, 0]], 0),
                          ttt_gamestate.TTTGameState([[0, 0, 0], [0, 0, 0], [1, 0, 0]], 0),
                          ttt_gamestate.TTTGameState([[0, 0, 0], [0, 0, 0], [0, 1, 0]], 0),
                          ttt_gamestate.TTTGameState([[0, 0, 0], [0, 0, 0], [0, 0, 1]], 0)])
