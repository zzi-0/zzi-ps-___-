
s, t = ['A','B'], ['A','B','B']


while True:
    if len(s) == len(t):
        if s == t:
            print(1)
        else:
            print(0)
        break
    str = t.pop()
    if str == 'B':
        t.reverse()



