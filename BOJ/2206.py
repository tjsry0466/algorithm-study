from collections import deque

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

q = deque()
q.append([0, 0, 1, 1])

while q:
    item = q.popleft()
    y, x, count, skill = item

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
            # 스킬 사용이 가능한 경우 스킬을 사용처리하고 다음 위치로 이동
            if board[ny][nx] == "1" and skill == 1:
                if nx == M - 1 and ny == N - 1:
                    print(count + 1)
                    exit()
                q.append([ny, nx, count + 1, 0])
                visited[ny][nx] = 1
            elif board[ny][nx] == "0":
                if nx == M - 1 and ny == N - 1:
                    print(count + 1)
                    exit()
                q.append([ny, nx, count + 1, skill])
                visited[ny][nx] = 1

print(-1)
