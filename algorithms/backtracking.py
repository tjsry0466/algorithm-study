import sys

li = [[1, 5, 3], [2, 5, 7], [5, 3, 5]]
chk = [False] * 3
m = sys.maxsize

def backtracking(row, score):
    global m  # 전역 변수 m을 사용하기 위해 필요
    if row == 3:  # 행의 인덱스가 3일 때 종료
        if score < m:
            m = score
        return
    for i in range(3):
        if chk[i] == False:  # 백트래킹에서의 한정조건
            chk[i] = True
            backtracking(row + 1, score + li[row][i])
            chk[i] = False
    return 

backtracking(0, 0)  # 초기 행을 0으로 시작
print(m)
