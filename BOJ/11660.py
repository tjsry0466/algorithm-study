# https://www.acmicpc.net/problem/11660

# N x N개의 수가 NxN 크기의 표에 채워져 있다.
# (x1, y1) 부터 (x2, y2)까지의 합을 구하는 문제

# 예를들어 N = 4이고, 표가 아래와 같이 채워져 있는 경우

# 1	2	3	4
# 2	3	4	5
# 3	4	5	6
# 4	5	6	7

# (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6=27이고, (4,4) 부터 (4,4)까지 합을 구하면 7이다.
# 표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때 정답을 구한다.

# 첫째 줄에 표의 크기 N. 그리고 합을 구해야 하는 횟수 M (N은 1 이상, 1024이하 / M은 1 이상 100,000이하)
# 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행 부터 차례대로 주어짐
# 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2가 주어지고 (x1, y1) 부터 (x2, y2)의 합을 구해 출력
# 표에 채워져 있는 수는 1000보다 작거나 같은 자연수

# N = 표의 크기
# M = 합을 구해야 하는 횟수 

# 1. 2차원 배열의 누적합을 구한다.
# 2. 특정 영역에 대한 누적합을 다음과 같은 방법으로 구한다.
#    - (sourceX, sourceY), (targetX, targetY)의 누적합은 다음과 같다.
#    - 누적합 보드에서 가장 마지막 값(sumBoard[targetY][targetX])에서 가로, 세로에 대해 누적합이 시작되기 직전 값을 빼준다.
#    - 영역의 마지막 누적합(sumBoard[targetY][targetX]) - 세로 직전값(sumBoard[sourceY-1][sourceX]) - 가로 직전값(sumBoard[sourceY][sourceX-1])
#    - 그리고 중복해서 뺐으므로 sumBoard[sourceY-1][sourceX-1]을 더해준다. 최종적으로 다음과 같아진다.
#    - sumBoard[targetY][targetX] - sumBoard[sourceY-1][sourceX] - sumBoard[sourceY][sourceX-1] + sumBoard[sourceY-1][sourceX-1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(M)]

sumBoard = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
	for j in range(1, N+1):
		sumBoard[i][j] = sumBoard[i-1][j] + sumBoard[i][j-1] - sumBoard[i-1][j-1] + board[i-1][j-1]

for x1, y1, x2, y2 in arr:
    result = sumBoard[x2][y2] - sumBoard[x1-1][y2] - sumBoard[x2][y1-1] + sumBoard[x1-1][y1-1]
    print(result)