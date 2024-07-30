# https://www.acmicpc.net/problem/2239

# 스도쿠를 채우는 문제
# 답이 여러개 있다면 그 중 사전식으로 앞서는 것을 출력
# dfs와 백트래킹 이용.
# 앞에서부터 1~9중에 가로열에 없고, 세로열에 없고, 같은 서브 그리드 안에 없는걸로 채운다.
# 종료조건 - 다 채웠을 때

# 구현 방법
# 방문해야될 목록을 리스트에 담고 하나씩 순회
# 각 항목에 1부터 9까지 채울 수 있는지 검사하면서 채울 수 있다면 채움
# 채우다가 불가능하다면 백트래킹을 이용해 되돌아가기

zero_area = []
sudoku = [list(map(int,list(input()))) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero_area.append([i,j])

def row(y, v):
	for i in range(9):
		if (sudoku[y][i] == v):
			return False

	return True

def column(x, v):
	for i in range(9):
		if (sudoku[i][x] == v):
				return False

	return True

def sub_grid(y, x, v):
	for i in range(3):
		for j in range(3):
			if (sudoku[y//3 * 3+i][x//3 * 3+j] == v):
				return False

	return True

def dfs(n):
	if (n == len(zero_area)):
		for i in sudoku:
			print("".join(map(str,i)))
		exit()

	now = zero_area[n]

	y, x = now
	for i in range(1, 10):
		if row(y, i) and column(x, i) and sub_grid(y, x, i):
			sudoku[y][x] = i 
			dfs(n+1)
			sudoku[y][x] = 0

dfs(0)

# 두번째 풀이

zero_area = []
sudoku = [list(map(int, list(input()))) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero_area.append([i,j])

def checkFunc(y, x):
	checked = [False] * 10
	for i in range(9):
		x_value = sudoku[y][i]
		checked[x_value] =True

		y_value = sudoku[i][x]
		checked[y_value] =True

	for i in range(3):
		for j in range(3):
			value = sudoku[y//3 * 3+i][x//3 * 3+j]
			checked[value] = True

	return checked

def dfs(n):
	if (n == len(zero_area)):
		for i in sudoku:
			print("".join(map(str,i)))
		exit()

	now = zero_area[n]

	y, x = now
	checked = checkFunc(y, x)
	for i in range(1, 10):
		if checked[i] == False:
			sudoku[y][x] = i 
			dfs(n+1)
			sudoku[y][x] = 0

dfs(0)