import sys
from collections import deque


def solve() -> None:
    input = sys.stdin.readline

    n, l, r = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(start_row: int, start_col: int, visited: list[list[bool]]):
        queue = deque()
        queue.append((start_row, start_col))
        visited[start_row][start_col] = True

        union_cells = [(start_row, start_col)]
        population_sum = grid[start_row][start_col]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    if l <= abs(grid[row][col] - grid[nr][nc]) <= r:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                        union_cells.append((nr, nc))
                        population_sum += grid[nr][nc]

        return union_cells, population_sum

    days = 0
    while True:
        visited = [[False] * n for _ in range(n)]
        moved = False

        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    union_cells, population_sum = bfs(i, j, visited)
                    if len(union_cells) > 1:
                        moved = True
                        new_population = population_sum // len(union_cells)
                        for ur, uc in union_cells:
                            grid[ur][uc] = new_population

        if not moved:
            break
        days += 1

    print(days)


if __name__ == "__main__":
    solve()
