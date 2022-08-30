from player import player
from field import field
import random


class Game:

    def __init__(self, is_lose, is_win):
        self.is_lose = is_lose
        self.is_win = is_win
        self.player = player
        self.field = field
        self.game_round = 0

    def game_start(self):
        self.field.generate_win_point()
        print("Welcome to my world Tancula")
        print("your position is [x=0,y=0]")

        while self.is_win == self.is_lose:
            self.handle_move_player()
            self.check_if_lose()
            self.handle_check_game_status()

    def handle_move_player(self):
        print(f'you need to get to {self.field.win_point}')
        direct = input('Choose direct w[up]/s[down]/a[left]/d[right]: \n').lower()
        result = self.move_player(direct)

        while not result:
            direct = input('Choose correct direct w[y+1]/s[y-1]/a[x-1]/d[x+1]: \n').lower()
            result = self.move_player(direct)

        print(f'you position is: {self.player.get_position()}')

    def move_player(self, direct):
        result = False
        match direct:
            case "w":
                result = self.player.move_forward()

            case "s":
                result = self.player.move_down()

            case "a":
                result = self.player.move_left()

            case "d":
                result = self.player.move_right()

            case _:
                result = False

        return result

    def check_if_lose(self):
        if self.field.danger_point["y"] == self.player.y and self.field.danger_point["x"] == self.player.x:
            print('Oh noo!, you lose!, try again')
            self.is_lose = True

    def handle_check_game_status(self):
        if self.field.win_point["x"] == self.player.x and self.field.win_point["y"] == self.player.y:
            print('Congrats you win!')
            self.is_win = True
        else:
            print('Danger point is generating...')
            random_level = random.randrange(self.game_round, self.game_round + 3, 1)
            self.field.generate_danger_point({"x": player.x, "y": player.y}, random_level)
            if self.field.danger_point["y"] == self.player.y and self.field.danger_point["x"] == self.player.x:
                print('Oh noo!, you lose!, try again')
                self.is_lose = True
            else:
                print(f'Danger point is located on {self.field.danger_point}')
            self.game_round += 1


game = Game(False, False)
