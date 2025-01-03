# Union-Find 알고리즘

## 정의

- **Union-Find 알고리즘**(또는 **Disjoint Set Union, DSU**)은 **서로소 집합**(Disjoint Set)을 관리하는 자료구조입니다.
- 주로 **여러 개의 원소들이 어떤 집합에 속해 있는지**를 관리하거나, **두 원소가 같은 집합에 속해 있는지**를 확인하는 데 사용됩니다.
- **Kruskal 알고리즘**과 같은 그래프 문제에서 **사이클을 확인**하거나, **동일 집합 여부를 빠르게 검사**할 때 사용됩니다.

## 주요 연산

Union-Find 알고리즘은 크게 두 가지 연산을 제공합니다:

1. **Find**: 특정 원소가 속한 **집합의 대표자**(루트)를 찾습니다.
2. **Union**: 두 집합을 하나의 집합으로 **합칩니다**.

### Find 연산

- Find 연산은 **주어진 원소가 속한 집합의 대표자**를 찾는 연산입니다.
- 이를 위해 각 원소는 부모(parent) 정보를 가지며, 부모가 자기 자신인 경우 그 원소는 **집합의 루트**입니다.
- **경로 압축(Path Compression)** 기법을 사용하여, **트리의 높이를 줄이는 방식**으로 빠르게 루트를 찾을 수 있습니다.

### Union 연산

- Union 연산은 **두 원소가 속한 집합을 하나로 합치는 연산**입니다.
- 두 집합의 루트를 비교하여 하나의 집합으로 병합합니다.
- **랭크**(Rank) 또는 **크기**(Size)를 기준으로, 작은 집합을 큰 집합에 합침으로써 **트리의 높이를 최소화**할 수 있습니다.

## 알고리즘 과정

### 1. 초기화

- 각 원소는 자신을 부모로 설정하여, 모든 원소가 **독립된 집합**으로 시작합니다.

```cpp
for (int i = 0; i < n; i++) {
    parent[i] = i;  // 각 원소의 부모를 자기 자신으로 초기화
    rank[i] = 1;    // 각 집합의 높이를 1로 초기화
}
```
