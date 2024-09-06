# n개의 노드가 있는 그래프
# 1번 노드에서 가장 멀리 떨어진 노드의 갯수 구하기
# n은 2만 이하
# 간선 5만 이하
# vertex 요소 [a, b]는 a번 노드와 b번 노드 사이의 간선

# BFS로 탐색
# 최대 거리를 저장해두고 현재 위치와 최대 거리와 다르면 count를 1로 초기화
# 같으면 count+=1

from collections import defaultdict, deque


def solution(n, edge):

    result = 0
    current = 0
    graph = defaultdict(list)

    max_v = 0

    for item in edge:
        prev, next = item
        graph[prev].append(next)
        graph[next].append(prev)

        max_v = max(prev, next, max_v)

    q = deque()
    q.append([1, 1])
    visited = [0] * (max_v + 1)
    visited[1] = 1

    while q:
        item, count = q.popleft()
        if current == count:
            result += 1
        else:
            current = count
            result = 1

        nexts = graph.get(item)
        if nexts:
            for next in nexts:
                if not visited[next]:
                    q.append([next, count + 1])
                    visited[next] = 1

    return result


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
