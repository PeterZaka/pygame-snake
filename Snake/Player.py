class Player():

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.size = 0
        self.parts = []

        self.dir = 'right'

    def update_parts(self):
        if self.size == 0: return

        if self.size > len(self.parts): self.parts.append((self.x, self.y))
        
        self.parts.pop(0)
        self.parts.append((self.x, self.y))

    def update_movement(self):
        if self.dir == 'right': self.x += 1
        elif self.dir == 'left': self.x -= 1
        elif self.dir == 'up': self.y -= 1
        elif self.dir == 'down': self.y += 1

    def update_collision(self, size_of_area):
        if (self.x < 0 or self.x > size_of_area - 1): return True
        if (self.y < 0 or self.y > size_of_area - 1): return True

        for part in self.parts:
            if (self.x == part[0] and self.y == part[1]): return True

        return False

    def update_score(self, apple):
        if (self.x == apple.x and self.y == apple.y):
            self.size += 1