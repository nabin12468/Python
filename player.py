import math
import random 
class Player:
    def __init__(self, letter):
        self.name = letter
        self.score = 0

    def update_score(self, points):
        self.score += points

    def get_score(self):
        return self.score

    def greet(self):
        print(f"Hello, {self.name}! Your current score is {self.score}.")