# 다익스트라 알고리즘

## 개요

다익스트라(Dijkstra) 알고리즘은 **단일 시작점**에서 **모든 정점**까지의 **최단 경로**를 찾는 알고리즘입니다.  
**가중치가 양수**인 그래프에서만 동작하며, 음의 가중치가 없는 경우에 가장 효율적으로 사용됩니다.  
그래프의 모든 정점에 대해 **가장 짧은 경로**를 구하는 데 유용합니다.

## 알고리즘 설명

1. **초기화**

   - 시작 정점에서 모든 정점까지의 거리를 무한대로 설정합니다.
   - 시작 정점에서 자신으로의 거리는 0으로 설정합니다.
   - 모든 정점은 아직 방문하지 않은 상태로 표시합니다.

2. **최단 거리 계산**

   - 현재 방문하지 않은 정점 중 가장 작은 거리를 가진 정점을 선택합니다.
   - 선택한 정점에서 인접한 정점으로 가는 간선을 통해 새로운 경로가 더 짧으면, 그 경로로 거리를 업데이트합니다.

3. **반복**

   - 모든 정점을 방문할 때까지 2번 과정을 반복합니다.
   - 이미 방문한 정점은 다시 방문하지 않습니다.

## 다익스트라 알고리즘 의사 코드

def dijkstra(graph, start): # 초기화
distance = {v: float('inf') for v in graph}
distance[start] = 0
visited = set()

    while len(visited) < len(graph):
        # 방문하지 않은 정점 중 가장 작은 거리를 가진 정점 선택
        min_vertex = None
        for vertex in graph:
            if vertex not in visited:
                if min_vertex is None or distance[vertex] < distance[min_vertex]:
                    min_vertex = vertex

        # 해당 정점에서 인접한 정점으로 가는 경로 업데이트
        for neighbor, weight in graph[min_vertex]:
            if distance[min_vertex] + weight < distance[neighbor]:
                distance[neighbor] = distance[min_vertex] + weight

        # 방문한 정점으로 표시
        visited.add(min_vertex)

    return distance

## 시간 복잡도

- **O(V^2)**: 단순 구현의 경우, `V`는 정점(Vertex)의 개수입니다.
  - 이 경우, 모든 정점에 대해 최단 거리를 계산하고, 인접한 정점을 확인하는 과정에서 복잡도가 발생합니다.
- **O((V + E) log V)**: 우선순위 큐(Heap)를 사용하면 성능을 개선할 수 있으며, `V`는 정점(Vertex)의 개수, `E`는 간선(Edge)의 개수입니다.

## 장점

- **양의 가중치**가 있는 그래프에서 매우 효율적입니다.
- 다익스트라 알고리즘은 **음의 사이클**이 없을 때 가장 빠르게 최단 경로를 찾습니다.

## 단점

- **음의 가중치**가 있는 그래프에서는 동작하지 않습니다.
- **음의 사이클**을 감지하지 못합니다.

## 사용 사례

- **네트워크 라우팅**: 네트워크 상에서 최단 경로를 찾는 데 사용됩니다.
- **교통 경로 계산**: 도시 내에서 최단 경로를 찾는 문제에 적용할 수 있습니다.
