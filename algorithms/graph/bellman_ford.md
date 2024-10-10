# Bellman-Ford 알고리즘

## 개요

Bellman-Ford 알고리즘은 **단일 시작점**에서 **모든 정점**까지의 **최단 경로**를 찾는 알고리즘입니다.  
**음의 가중치**가 있는 그래프에서도 사용할 수 있으며, 음의 사이클(negative cycle)을 감지할 수 있습니다.

## 알고리즘 설명

1. **초기화**

   - 시작 정점에서 모든 정점까지의 거리를 무한대로 설정합니다.
   - 시작 정점에서 자신으로의 거리는 0으로 설정합니다.

2. **엣지 릴랙스(Edge Relaxation) 반복**

   - 모든 간선을 확인하며, 해당 간선을 통해 더 짧은 경로가 존재할 경우 거리를 업데이트합니다.
   - 이 과정을 **그래프의 정점 수 - 1번** 반복합니다.

3. **음의 사이클 검출**
   - 한 번 더 모든 간선을 확인하여, 만약 거리가 업데이트된다면, 이는 **음의 사이클**이 존재함을 의미합니다.
   - 음의 사이클이 있으면 최단 경로가 존재하지 않습니다.

## Bellman-Ford 알고리즘 의사 코드

```python
def bellman_ford(graph, start): # 초기화
distance = {v: float('inf') for v in graph}
distance[start] = 0

    # 엣지 릴랙스
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    # 음의 사이클 검출
    for u in graph:
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                return "Negative cycle detected"

    return distance
```

## 시간 복잡도

- **O(V \* E)**:
  - `V`는 정점(Vertex)의 개수,
  - `E`는 간선(Edge)의 개수입니다.
  - Bellman-Ford는 정점의 개수만큼 반복하며, 매 반복마다 모든 간선을 검사합니다.

## 장점

- **음의 가중치**가 있는 그래프에서도 동작합니다.
- **음의 사이클**이 존재하는지 여부를 검출할 수 있습니다.

## 단점

- Dijkstra 알고리즘에 비해 **시간이 오래 걸릴 수** 있습니다.
- **음의 사이클**이 없는 경우, Dijkstra 알고리즘이 더 **효율적**입니다.

## 사용 사례

- **네트워크 경로 최적화**
- **금융 시스템**에서 음의 사이클을 통해 차익 거래 탐지
