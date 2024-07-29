# https://www.acmicpc.net/problem/1987

# 접근 방법

# 세로 R칸, 가로 C칸으로 된 표 모양의 보드
# 보드의 각 칸에는 대문자 알파벳
# 좌측 상단칸(1, 1)에는 말이 놓여있음.
# 말은 상하좌우로 이동 가능
# 새로 이동한 칸에 적혀있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과 달라야함
# 좌측 상단에서 시작해서 말이 최대한 몇칸을 지날 수 있는지 구하는 문자.
# 최초 칸도 포함.

# dfs와 bfs로 풀 수 있어 보임.
# 방문한 알파벳을 기록한 배열을 두고 상하좌우에서 이동할 수 있는 칸으로 이동.
# 더이상 이동할 수 없을때 현재 값과 기록한 값과 비교해서 더 큰값으로 저장.

# 알파벳은 65가 65인 점을 이용해 visited 배열의 인덱스에 방문 여부 기록
# 

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board=[list(input().strip()) for _ in range(n)]
visited = [0] * 26
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0

def dfs(x, y, count):
	global answer
	answer = max(count, answer)

	for i in range(4):
		nx, ny = x+dx[i], y+dy[i]
		if (0 <= nx < n and 0 <= ny < m and visited[ord(board[nx][ny])-65] == 0):
			visited[ord(board[nx][ny])-65] = 1
			dfs(nx, ny, count+1)
			visited[ord(board[nx][ny])-65] = 0

visited[ord(board[0][0])-65]=1
dfs(0,0,1)
print(answer)