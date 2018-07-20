def print_board(top):
    line = "-----------"
    board_top = " " + top[1] + " | " + top[2] + " | " + top[3] + " "
    board_mid = " " + top[4] + " | " + top[5] + " | " + top[6] + " "
    board_bot = " " + top[7] + " | " + top[8] + " | " + top[9] + " "
    print(board_top)
    print(line)
    print(board_mid)
    print(line)
    print(board_bot)

def check_win(top):
    if top[1] == top[2] and top[2] == top[3]:
        return(top[1])
    elif top[4] == top[5] and top[5] == top[6]:
        return(top[4])
    elif top[7] == top[8] and top[8] == top[9]:
        return(top[7])
    elif top[1] == top[5] and top[5] == top[9]:
        return(top[1])
    elif top[3] == top[5] and top[5] == top[7]:
        return(top[3])
    elif top[1] == top[4] and top[4] == top[7]:
        return(top[1])
    elif top[2] == top[5] and top[5] == top[8]:
        return(top[2])
    elif top[3] == top[6] and top[6] == top[9]:
        return(top[3])
    else:
        return(False)

def turn(ask, playa):
    print_board(ask)
    o = int(input("{}'s Turn. Pick a position:  ".format(playa)))
    if ask[o] != 'O' and ask[o] != 'X':
        ask[o] = playa
    else:
        print("Something's there, you wasted a turn you genius")
    if check_win(ask) == playa:
        print("{} WINS SUCKA!".format(playa))
        return(False)
    else:
        print("Next Turn")

ask = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

i = 1
while i < 10:
    if i % 2 == 1:
        if turn(ask, "X") == False:
            break
        else:
            i += 1
    else:
        if turn(ask, "O") == False:
            break
        else:
            i += 1

