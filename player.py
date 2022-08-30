from field import field


class Player:

    def __init__(self, x_size, y_size):
        self.x = x_size
        self.y = y_size

    def reset(self):
        self.x = 0
        self.y = 0

    def get_position(self):
        return f'[x = {self.x}, y = {self.y}]'

    def move_forward(self):
        if self.y >= field.y_size:
            self.y = 0
        else:
            self.y += 1
        return True

    def move_down(self):
        if self.y <= 0:
            self.y = field.y_size
        else:
            self.y -= 1
        return True

    def move_left(self):
        if self.x <= 0:
            self.x = field.x_size
        else:
            self.x -= 1
        return True

    def move_right(self):
        if self.x >= field.x_size:
            self.x = 0
        else:
            self.x += 1
        return True


player = Player(0, 0)
print(player.y)
