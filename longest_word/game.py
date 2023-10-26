import string
import random
import requests

# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for i in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))


    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False
        letters = self.grid.copy()
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.check_dict(word)

    @staticmethod
    def check_dict(word):
        response = requests.get(f'https://wagon-dictionary.herokuapp.com/{word}')
        json_response = response.json()
        return json_response['found']

"""
if __name__ == "__main__":
    new_game = Game()
    new_game.grid = list('KWIENFUQW')
    print(new_game.is_valid('FEUN'))
"""
