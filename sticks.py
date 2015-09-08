def make_move(stick_count,pick_up):
    return stick_count - int(pick_up)

def whose_turn(active_player,player_1,player_2):
    if active_player == player_1:
        active_player = player_2
    else:
        active_player = player_1

    return active_player


def game_complete(stick_count):
    complete = False
    if stick_count < 1:
        complete = True
    return complete

def player_vs_player():
    player_1 = "Maple"
    player_2 = "Danai"
    active_player = player_1
    stick_count = 20


    while game_complete(stick_count) == False:
        pick_up = (input("""{}, it is your turn. How many sticks will you pick up:
            [1], [2] or [3]""".format(whose_turn(active_player, player_1,player_2,))))


        # make_move(player1, stick_count)
        stick_count = make_move(stick_count , pick_up)
        active_player = whose_turn(active_player, player_1,player_2,)
        if stick_count > 0:
            print(stick_count)
        else:
            print("0")
    print("{}, YOU LOSE AHAHAHAHAHAHAH!!!!".format(active_player))
















if __name__ == '__main__':
    player_vs_player()
