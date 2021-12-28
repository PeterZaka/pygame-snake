import random

class Apple():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update_collision(self, player, size_of_area):
        if (self.x == player.x and self.y == player.y):
            self.x = random.randint(0, size_of_area - 1)
            self.y = random.randint(0, size_of_area - 1)