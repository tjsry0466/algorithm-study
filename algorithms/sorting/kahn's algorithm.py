from collections import deque

# 그래프와 진입 차수 설정
graph = {1: [2, 3], 2: [4], 3: [4, 6], 4: [5], 5: [], 6: []}

# 진입 차수 계산
in_degree = {i: 0 for i in graph}
for nodes in graph.values():
    for node in nodes:
        in_degree[node] += 1

# 진입 차수가 0인 노드를 큐에 넣기
queue = deque([node for node in graph if in_degree[node] == 0])

# 위상 정렬 결과
topo_sort = []

while queue:
    node = queue.popleft()
    topo_sort.append(node)

    # 간선 제거 후 진입 차수가 0이 된 노드를 큐에 추가
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

print("위상 정렬 결과:", topo_sort)
