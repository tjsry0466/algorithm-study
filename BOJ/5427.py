# https://www.acmicpc.net/problem/5427

# 불이나 불이 동서남북으로 퍼져 나간다.
# 얼마나 빨리 빌딩을 탈출 할 수 있는지 구하는 프로그램 작성

# 케이스 개수 최대 100개
# ".": 빈 공간, "#": 벽, "@": 상근이의 시작 위치, "*", 불
# 탈출 -> 배열 밖으로 나갈 수 있는 경우
# 불가능한 경우 IMPOSSIBLE 출력

# 접근 방법
# 불과 상근이에게 2개의 큐를 두고 이동시킨다.
# 동시에 같은 칸으로 이동할 수 없으므로 불을 먼저 이동한 후에 방문처리를 한다.
# 이후 남은 칸으로 상근이가 이동한다.

from collections import deque


def bfs(W, H, board):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    fire_queue = deque()
    sg_queue = deque()

    for i in range(H):
        for j in range(W):
            if board[i][j] == "*":
                fire_queue.append((i, j))
            elif board[i][j] == "@":
                sg_queue.append((i, j, 0))
                board[i][j] = "."

    while sg_queue:
        fire_size = len(fire_queue)
        for _ in range(fire_size):
            fx, fy = fire_queue.popleft()
            for i in range(4):
                nfx, nfy = fx + dx[i], fy + dy[i]
                if 0 <= nfx < H and 0 <= nfy < W and board[nfx][nfy] == ".":
                    board[nfx][nfy] = "*"
                    fire_queue.append((nfx, nfy))

        sg_size = len(sg_queue)
        for _ in range(sg_size):
            x, y, time = sg_queue.popleft()

            if x == 0 or x == H - 1 or y == 0 or y == W - 1:
                return time + 1

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == ".":
                    board[nx][ny] = "@"
                    sg_queue.append((nx, ny, time + 1))

    return "IMPOSSIBLE"


def solve():
    W, H = map(int, input().split())
    board = [list(input().strip()) for _ in range(H)]
    print(bfs(W, H, board))


T = int(input())
for _ in range(T):
    solve()
