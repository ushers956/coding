theboard = {'7':'','8':'','9':'','4':'','5':'','6':'','1':'','2':'','3':''}

board_keys = []
for key in theboard:
    board_keys.append(key)

def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():

    turn = 'x'
    count = 0



    for i in range(10):
        printboard(theboard)
        print("its your turn," + turn + ".move to witch place?")

        move = input()

        if theboard[move] =='':
            theboard[move] = turn
            count += 1
        else:
            print("that place is areadyh filled.\nmove to witch place")
            continue