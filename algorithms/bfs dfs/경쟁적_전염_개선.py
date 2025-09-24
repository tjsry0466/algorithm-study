from collections import deque

n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def spread_viruses():
    # 모든 바이러스의 위치를 바이러스 번호 순으로 큐에 저장
    queue = deque()

    # 바이러스 번호 순으로 초기 위치들을 큐에 추가
    for virus_num in range(1, k + 1):
        for i in range(n):
            for j in range(n):
                if graph[i][j] == virus_num:
                    queue.append((i, j, virus_num, 0))  # (x, y, 바이러스번호, 시간)

    # BFS로 바이러스 확산
    while queue:
        x, y, virus_num, time = queue.popleft()

        # 시간이 s초를 넘으면 중단
        if time >= s:
            break

        # 4방향으로 확산
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 빈 공간이면 바이러스 확산
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus_num
                    queue.append((nx, ny, virus_num, time + 1))


spread_viruses()
print(graph[x - 1][y - 1])
