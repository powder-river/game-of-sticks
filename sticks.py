player1 = "Maple"
player2 = "Danai"

stick_count = 20
def make_move(player, sticks):
    return stick_count - sticks

def game_complete(stick_count):
    complete = False
    if stick_count < 1:
        complete = True
    return complete















if __name__ == '__main__':
    main()
