from random import choice
import numpy as np

class Opponent():
    def __init__(self, level='random'):
        assert level in ['random', 'minmax', 'alphabeta']
        self._move = MOVE_FUNC[level]
    
    def first_move(self):
        return choice(range(9))
    
    def move(self, board):
        return self._move(board)
    
def random_move(board):
    return choice(np.where(board == 0)[0])

def minmax(board):
    pass

def alphabeta(board):
    pass

MOVE_FUNC = {
    'random': random_move,
    'minmax': minmax,
    'alphabeta': alphabeta
}