# 빈칸이 하나도 없거나(추가로 O가 4개 X가 5개 이어야함), 
# 가로 세로 대각선이 3칸이어야함
# [0][3][6] or [1][4][7] or [2][5][8]
# [0][1][2] or [3][4][5] or [6][7][8]
# [0][4][8] or [2][4][6]

games = ['XXXOO.XXX',
'XOXOXOXOX',
'OXOXOXOXO',
'XXOOOXXOX',
'XO.OX...X',
'.XXX.XOOO',
'X.OO..X..',
'OOXXXOOXO',
'XOXOXOXO.',
'OOOXXXXXO'
]

def check(type,game):
    if game[0] == game[3] == game[6] and game[0] == type:
        return True
    if game[1] == game[4] == game[7] and game[1] == type:
        return True
    if game[2] == game[5] == game[8] and game[2] == type:
        return True
    if game[0] == game[1] == game[2] and game[0] == type:
        return True
    if game[3] == game[4] == game[5] and game[3] == type:
        return True
    if game[6] == game[7] == game[8] and game[6] == type:
        return True
    if game[0] == game[4] == game[8] and game[0] == type:
        return True
    if game[2] == game[4] == game[6] and game[2] == type:
        return True
    return False



for game in games:
    x_count = game.count('X')
    o_count = game.count('O')
    
    if x_count == o_count:
        if check('O',game) and not check('X',game):
            print('valid')
        else:
            print('invalid')
    elif x_count == o_count + 1:
        if check('X',game) and not check('O',game):
            print('valid')
        elif not check('X',game) and not check('O',game) and x_count == 5:
            print('valid')
        else:
            print('invalid')
    else:
        print('invalid')
