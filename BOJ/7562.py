# https://www.acmicpc.net/problem/7562

from collections import deque

dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(L, start, end):
    start_y, start_x = start
    end_y, end_x = end

    if start == end:
        return 0

    visited = [[0] * L for _ in range(L)]
    visited[start_y][start_x] = 1

    q = deque()
    q.append((start_y, start_x, 0))

    while q:
        y, x, moves = q.popleft()

        if y == end_y and x == end_x:
            return moves

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < L and 0 <= ny < L and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx, moves + 1))

    return -1


N = int(input())

for i in range(N):
    L = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    print(bfs(L, start, end))
