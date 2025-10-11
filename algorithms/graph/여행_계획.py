# 특정 원소가 속한 집합을 찾기
import sys

input = sys.stdin.readline


def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

graph = []
parent = [0] * (n + 1)  # 부모 테이블 초기화

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        if row[j - 1] == 1:
            union_parent(parent, i, j)

plan = list(map(int, input().split()))

root = find_parent(parent, plan[0])

for city in plan[1:]:
    if find_parent(parent, city) != root:
        print("NO")
        exit()

print("YES")
