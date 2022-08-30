import random
import math


class Field:

    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.danger_point = {"x": 11, "y": 11}
        self.win_point = None

    def generate_win_point(self):
        self.win_point = {
            "x": random.randrange(math.ceil((self.x_size + 1) / 2), self.x_size + 1, 1),
            "y": random.randrange(math.ceil((self.y_size + 1) / 2), self.y_size + 1, 1)
        }

    def generate_danger_point(self, position, random_numb):
        print(random_numb)
        start_scope_x = 0
        start_scope_y = 0
        if random_numb < 5:
            start_scope_x = position["x"] - 3 if position["x"] - 3 >= 0 else 0
            start_scope_y = position["y"] - 5 if position["y"] - 5 >= 0 else 0
        elif random_numb < 8:
            start_scope_x = position["x"] - 2 if position["x"] - 2 >= 0 else 0
            start_scope_y = position["y"] - 3 if position["y"] - 3 >= 0 else 0
        else:
            start_scope_x = position["x"] - 2 if position["x"] - 1 >= 0 else 0
            start_scope_y = position["y"] - 2 if position["y"] - 1 >= 0 else 0

        self.danger_point = {
            "x": random.randrange(start_scope_x, position["x"] + 1, 1),
            "y": random.randrange(start_scope_y, position["y"] + 1, 1)
        }

    def reset(self):
        self.danger_point = None
        self.generate_win_point()


field = Field(10, 10)

