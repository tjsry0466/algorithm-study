# https://www.acmicpc.net/problem/2667

# 단지 번호 붙이기

# 정사각형 모양의 지도가 있음.
# 1은 집이 있는 곳, 0은 집이 없는 곳
# 연결된 집의 모임인 단지를 정의하고 단지에 번호를 붙여야 함
# 상하좌우든 연결되어 있으면 같은 단지임

# 각 단지에 속하는 집의 수를 오름차순으로 출력

from collections import deque

N = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

d = [list(map(int, input())) for _ in range(N)]
q = deque()
check = [[False] * N for _ in range(N)]

answer = 0
counts = []

for i in range(N):
    for j in range(N):
        if check[i][j] == False and d[i][j] == 1:
            check[i][j] = True
            q.append((i, j))
            answer+=1
            counts.append(1)

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if d[nx][ny] == 1 and check[nx][ny] == False:
                            q.append((nx, ny))
                            check[nx][ny] = True
                            counts[len(counts)-1] +=1
                            
print(answer)
counts.sort()
for i in counts:
    print(i)