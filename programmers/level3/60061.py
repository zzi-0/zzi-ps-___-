def check(answer):
    for i in answer:
        x, y, structure = i[0], i[1], i[2]
        # 기둥(0)
        if structure == 0:
            # 기둥이 바닥에 설치 되어 있거나 왼쪽이나 오른쪽에 보가 설치되어있거나 아래에 기둥이 설치되어 있으면 가능
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        # 보(1)
        else:
            # 기둥이 왼쪽 아래나 오른쪽 아래에 설치되어있거나
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                continue
            # 양쪽에 보가 설치되어 있으면 가능
            if [x-1, y, 1] in answer and [x+1, y, 1] in answer:
                continue
            return False
    return True
    
def solution(n, build_frame):
    answer = []
    for i in build_frame:
        x, y, structure, setting = i[0], i[1], i[2], i[3]
        # 설치
        if setting == 1:
            answer.append([x, y, structure])
            if not check(answer):
                answer.remove([x, y, structure])
        # 삭제
        else:
            answer.remove([x, y, structure])
            if not check(answer):
                answer.append([x, y, structure])
    answer = sorted(answer)
    return answer

# print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))