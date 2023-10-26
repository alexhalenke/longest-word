from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
            new_game = Game()

            # exercise
            grid = new_game.grid

            # verify
            assert type(grid) == list
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase

    def test_game_validity(self):
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'
        new_game.grid = list(test_grid)
        assert new_game.is_valid(test_word) is True
        assert new_game.grid == list(test_grid)

    def test_empty_word_is_invalid(self):
        new_game = Game()
        assert new_game.is_valid('') is False

    def test_is_invalid(self):
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'SANDWICH'
        # exerice
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is False
        # teardown
        assert new_game.grid == list(test_grid)

    def test_for_unknown_word(self):
        """A word that is not in the english directory should notbe valid"""
        new_game=Game()
        new_game.grid = list('KWIENFUQW')
        assert new_game.is_valid('FEUN') is False
