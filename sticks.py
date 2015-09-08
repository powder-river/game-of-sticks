
player2 = "Danai"


def make_move(stick_count, pick_up):
    return stick_count - int(pick_up)

def game_complete(stick_count):
    complete = False
    if stick_count < 1:
        complete = True
    return complete

def player_vs_player():
    player1 = "Maple"
    stick_count = 20
    print("There are {} sticks in play.\n".format(stick_count))
    pick_up = input("""{}, it is your turn. How many sticks will you pick up:
        [1], [2] or [3]""".format(player1))
    stick_count = make_move(stick_count , pick_up)
    print(stick_count)
















if __name__ == '__main__':
    player_vs_player()
