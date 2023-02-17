import sys
input = sys.stdin.readline
original_str = 'mirkovC4nizCC44'
explosion_str = 'C4'
n = len(explosion_str)
stack = []

for str in original_str:
    stack.append(str)
    if ''.join(stack[-n:]) == explosion_str:
        for _ in range(n):
            stack.pop()
            
changed_str = ''.join(stack)
if changed_str == '':
    print('FRULA')
else:
    print(changed_str)
        