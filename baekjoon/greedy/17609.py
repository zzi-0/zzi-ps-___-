import sys
input = sys.stdin.readline

t = 7
words = ['abba','summuus','xabba','xabbay','comcom','comwwmoc','comwwtmoc']

def is_palindrome(word):
    n = len(word)
    half = n // 2
    for i in range(half):
        if word[i] != word[n-i-1]:
            return [False, i, n-i-1]
    return [True,0,0]


for word in words:
    [result, left, right] = is_palindrome(word)
    if result:
        print(0)
    else:
        if is_palindrome(word[:left]+word[left+1:])[0] or is_palindrome(word[:right]+word[right+1:])[0]:
            print(1)
        else:
            print(2)