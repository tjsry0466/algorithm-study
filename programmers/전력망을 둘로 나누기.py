# https://school.programmers.co.kr/learn/courses/30/lessons/86971#

# 그래프 분할 문제 유형으로 그래프를 둘로 나눴을 때 두 그래프 노드의 차가 최소가 되는 수를 구하는 문제
# 어느 엣지를 없애야 그래프 노드 수의 차이가 최소가 되는지 알아내야 한다
# 완전 탐색을 통해 해결할 수 있다.

# 풀이 방법
# 1. 주어진 노드 정보로 그래프를 만든다
# 2. 각 노드 정보를 순회하며 해당 노드간의 연결을 끊고 
#    한쪽 노드의 수를 구해서 전체 노드의 수와 빼서 최소 차이를 구한다.

from collections import defaultdict, deque

def bfs(start, graph, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
                
    return count

def solution(n, wires):
    graph = defaultdict(list)
    
    # 그래프 구성
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
    
    min_difference = float('inf')
    
    # 각 전선을 제거해가며 그래프를 분할하고 차이를 계산
    for u, v in wires:
        # 현재 전선(u, v) 제거
        graph[u].remove(v)
        graph[v].remove(u)
        
        # 한 쪽 영역의 노드 개수 계산 (u에서 시작)
        node_count = bfs(u, graph, n)
        
        # 두 영역의 노드 개수 차이 계산
        difference = abs((n - node_count) - node_count)
        
        # 최소 차이 갱신
        min_difference = min(min_difference, difference)
        
        # 제거했던 전선을 다시 복구
        graph[u].append(v)
        graph[v].append(u)
    
    return min_difference


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) # 3