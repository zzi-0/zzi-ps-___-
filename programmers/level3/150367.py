import math

def is_tree(bi):
    global is_tree
    n = len(bi)
    mid = n // 2
    if len(bi) == 1:
        return True
    if bi[mid] == '0':
        if not all (child == '0' for child in bi):
            return False
    return is_tree(bi[:mid]) and is_tree(bi[mid+1:])
    
def solution(numbers):
    answer = []
    
    for number in numbers:
        bi_list = bin(number)[2:]
        n = math.log(len(bi_list)+1, 2)
        if n != math.floor(n):
            m = int(math.pow(2,math.ceil(n))) - 1
            temp = '0' * (m-len(bi_list))
            bi_list = temp+ bi_list
        bi_list = ['0','0','0','1','1','1','1']

        if is_tree(bi_list):
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution([96]))