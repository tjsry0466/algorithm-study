# 키 포인트
# 빈공간을 배열로 선언하고 빈 공간만큼 채워졌으면 끝냄
# 1부터 9까지 해당 공간에 둘 수 있는지 검사
# 가로, 세로, 해당 서브그리드
# 서브그리드를 검사하려면 i, j 에 대해서 3만큼 반복하면서 아래 로직처럼 순회하면 
# 해당 x, y좌표가 존재하는 서브 그리드의 모든 영역을 순회할 수 있다.
# sudoku[y // 3 * 3 + i][x // 3 * 3 + i]

def row(a, n): # 가로
    for i in range(9):
        if n == sudoku[a][i]: # 이미 있으면
            return False
    return True

def column(a, n): # 세로
    for i in range(9):
        if n == sudoku[i][a]: # 이미 있으면
            return False
    return True

def square(y, x, n): # 3x3 칸
    for i in range(3):
        for j in range(3):
            if n == sudoku[y//3 * 3 + i][x//3 * 3 + j]: # 칸내에 이미 있으면
                return False
    return True

def find(n):
    if n == len(blank): # 빈 공간 만큼 사용했으면
        for i in sudoku: # 출력 후
            print(*i) 
        exit() # 강제 종료

    for i in range(1,10):
        y = blank[n][0]
        x = blank[n][1]
        if column(x,i) and row(y,i) and square(y, x, i):
            sudoku[y][x] = i
            find(n+1)
            sudoku[y][x] = 0

import sys

sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i,j])
find(0)