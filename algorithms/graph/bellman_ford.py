class Graph:
    def __init__(self, vertices):
        self.V = vertices  # 정점 개수
        self.edges = []  # 간선 목록

    # 간선을 추가하는 함수
    def add_edge(self, u, v, weight):
        self.edges.append([u, v, weight])

    # Bellman-Ford 알고리즘 함수
    def bellman_ford(self, start):
        # 초기화: 시작 정점에서 모든 정점까지의 거리를 무한대로 설정
        distance = [float("inf")] * self.V
        distance[start] = 0  # 시작 정점의 거리는 0으로 설정

        # 정점 수 - 1번 반복하며 간선 완화(Edge Relaxation)
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if distance[u] != float("inf") and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

        # 음의 사이클이 있는지 확인
        for u, v, weight in self.edges:
            if distance[u] != float("inf") and distance[u] + weight < distance[v]:
                print("Negative cycle detected")
                return

        # 결과 출력
        self.print_solution(distance)

    # 결과를 출력하는 함수
    def print_solution(self, distance):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{distance[i]}")

# 예시 그래프 생성 및 실행
if __name__ == "__main__":
    g = Graph(5)  # 정점 5개인 그래프 생성
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    # 시작 정점이 0인 경우 실행
    g.bellman_ford(0)
