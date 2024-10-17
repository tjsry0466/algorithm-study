class UnionFind:
    def __init__(self, n):
        """
        n: 집합에 속한 원소의 개수
        각 원소는 자신을 부모로 초기화
        """
        self.parent = [i for i in range(n)]
        self.rank = [1] * n  # 트리의 깊이(랭크)를 추적하여 효율적으로 트리를 병합

    def find(self, x):
        """
        Find 연산: x가 속한 집합의 루트(대표자)를 찾습니다.
        경로 압축 기법을 사용하여 트리의 깊이를 줄임.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 경로 압축
        return self.parent[x]

    def union(self, x, y):
        """
        Union 연산: 두 집합을 합칩니다.
        """
        rootX = self.find(x)
        rootY = self.find(y)

        # 두 집합의 루트가 다르면 합침 (Union by Rank)
        if rootX != rootY:
            # 랭크가 더 큰 쪽을 부모로 설정
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1  # 랭크가 같으면 하나의 트리 깊이를 증가시킴

    def connected(self, x, y):
        """
        두 원소 x와 y가 같은 집합에 속해 있는지 확인
        """
        return self.find(x) == self.find(y)


# 사용 예시
if __name__ == "__main__":
    # 원소 0부터 9까지 10개의 집합 초기화
    uf = UnionFind(10)

    # Union 연산으로 집합 합치기
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)

    # 같은 집합에 속해 있는지 확인
    print(uf.connected(1, 5))
    print(uf.connected(5, 7))
    print(uf.connected(4, 9))

    # 다른 집합을 합침
    uf.union(4, 9)
    print(uf.connected(4, 9))
