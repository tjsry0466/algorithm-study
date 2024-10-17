class UnionFind:
    def __init__(self, n):
        # 각 노드의 부모를 자기 자신으로 초기화
        self.parent = [i for i in range(n)]
        # 각 트리의 랭크를 0으로 초기화
        self.rank = [0] * n

    def find(self, x):
        # 경로 압축 기법을 사용하여 루트 노드를 찾음
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # 두 집합을 합침 (Union by Rank 사용)
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            # 랭크가 높은 쪽을 부모로 설정
            if self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[y_root] = x_root
                if self.rank[x_root] == self.rank[y_root]:
                    self.rank[x_root] += 1


def kruskal(n, edges):
    """
    n: 정점의 개수
    edges: (가중치, 정점1, 정점2)의 튜플로 이루어진 리스트
    """
    # 간선을 가중치 순으로 정렬
    edges.sort()
    uf = UnionFind(n)
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        # 두 정점이 같은 집합에 속해 있지 않으면 간선 추가
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


# 예제 사용법
if __name__ == "__main__":
    # 정점의 개수
    n = 5
    # 간선 리스트: (가중치, 정점1, 정점2)
    edges = [
        (1, 0, 1),
        (2, 0, 2),
        (3, 1, 2),
        (4, 1, 3),
        (5, 2, 3),
        (6, 2, 4),
        (7, 3, 4),
    ]

    mst, total_weight = kruskal(n, edges)

    print("MST에 포함된 간선:")
    for u, v, weight in mst:
        print(f"{u} -- {v} (가중치: {weight})")
    print(f"최소 신장 트리의 총 가중치: {total_weight}")
