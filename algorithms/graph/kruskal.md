# Kruskal 알고리즘

## 정의

- **Kruskal 알고리즘**은 **그리디 알고리즘**의 일종으로, 그래프에서 **최소 신장 트리**(MST: Minimum Spanning Tree)를 구하는 알고리즘입니다.
- 간선을 중심으로 동작하며, 간선의 가중치를 오름차순으로 정렬하여 **사이클을 생성하지 않으면서** 가장 작은 가중치의 간선들을 선택하여 트리를 구성합니다.

## 알고리즘 과정

1. 그래프의 **모든 간선을 가중치 순으로 정렬**합니다.
2. 가장 작은 가중치의 간선부터 선택합니다.
3. **사이클이 생기지 않으면** 그 간선을 트리에 추가합니다. (사이클 여부는 **유니온-파인드(Union-Find)** 자료구조를 통해 확인)
4. \(V-1\)개의 간선을 선택할 때까지 반복합니다. (V는 정점의 수)

## Kruskal 알고리즘의 주요 개념

### 1. **유니온-파인드(Union-Find)** 자료구조

- **사이클 검사를 위한 자료구조**로, 그래프에서 간선을 추가할 때 **사이클이 발생하는지 여부**를 빠르게 확인하기 위해 사용됩니다.
- **Find**: 특정 정점이 속한 트리를 찾는 연산.
- **Union**: 두 정점이 속한 트리를 합치는 연산.
- **경로 압축**(Path Compression)과 **랭크(rank)를 기반으로 한 합치기**를 사용하여 시간 복잡도를 효율적으로 줄일 수 있습니다.

### 2. **사이클 검사**

- 간선을 추가할 때, 선택된 두 정점이 이미 같은 트리에 속해 있으면 **사이클이 발생**한 것이므로 해당 간선은 추가하지 않습니다.
- 유니온-파인드를 사용하여 두 정점이 같은 트리에 속해 있는지 여부를 확인합니다.

## 알고리즘의 과정 예시

### 예시 그래프

정점 \(A, B, C, D, E\)와 다음과 같은 간선들이 있다고 가정합니다.

- 간선 \(A-B\), 가중치 1
- 간선 \(A-C\), 가중치 2
- 간선 \(B-C\), 가중치 3
- 간선 \(B-D\), 가중치 4
- 간선 \(C-D\), 가중치 5
- 간선 \(C-E\), 가중치 6
- 간선 \(D-E\), 가중치 7

### 알고리즘 단계

1. **간선 정렬**: 간선들을 가중치 순으로 오름차순 정렬.
   - \(A-B(1), A-C(2), B-C(3), B-D(4), C-D(5), C-E(6), D-E(7)\)
2. **가중치가 가장 작은 간선부터 선택**:

   - \(A-B\) 간선 선택 (사이클 없음).
   - \(A-C\) 간선 선택 (사이클 없음).
   - \(B-C\) 간선은 사이클을 만들기 때문에 선택하지 않음.
   - \(B-D\) 간선 선택 (사이클 없음).
   - \(C-D\) 간선은 사이클을 만들기 때문에 선택하지 않음.
   - \(C-E\) 간선 선택 (사이클 없음).

3. **최종 MST**: 선택된 간선들은 \(A-B\), \(A-C\), \(B-D\), \(C-E\)로 이루어진 최소 신장 트리입니다.

## 시간 복잡도

- 간선의 수를 \(E\), 정점의 수를 \(V\)라고 할 때:
  1. 간선 정렬: \(O(E \log E)\)
  2. 유니온-파인드 연산(Find와 Union): \(O(\alpha(V))\) (경로 압축과 랭크를 사용한 최적화 시 거의 상수 시간)

따라서 **전체 시간 복잡도**는 \(**O(E \log E)**\)입니다. 이는 대부분의 경우에서 \(E \geq V\)이므로, 이 시간 복잡도는 매우 효율적입니다.

## 장점

- **희소 그래프**(sparse graph)에서 효율적입니다.
- 구현이 상대적으로 간단하며, 간선 수가 적을 때 성능이 좋습니다.

## 단점

- 간선 정렬 과정이 시간이 걸리기 때문에, 간선이 많은 **밀집 그래프**(dense graph)에서는 비효율적일 수 있습니다.

## Kruskal 알고리즘과 Prim 알고리즘 비교

| 비교 항목                | Kruskal 알고리즘                     | Prim 알고리즘                        |
| ------------------------ | ------------------------------------ | ------------------------------------ |
| 접근 방식                | 간선 중심 (간선 선택)                | 정점 중심 (정점 확장)                |
| 시간 복잡도              | \(O(E \log E)\)                      | \(O(E \log V)\)                      |
| 사용 자료구조            | 유니온-파인드 (Union-Find)           | 우선순위 큐 (Priority Queue)         |
| 적합한 그래프            | **희소 그래프** (간선이 적은 그래프) | **밀집 그래프** (간선이 많은 그래프) |
| 간선 정렬 필요 여부      | 필요함                               | 불필요                               |
| 간선의 수가 많을 때 성능 | 성능이 떨어질 수 있음                | 간선이 많을 때 효율적                |

## Kruskal 알고리즘의 활용

- **네트워크 최적화**: 컴퓨터 네트워크, 전력망 등의 인프라를 최소 비용으로 연결하는 문제에서 사용됩니다.
- **도로망 설계**: 도시를 최소 비용으로 연결하는 도로 설계에서 유용합니다.
- **그래프 이론 문제**: 다양한 그래프 이론 문제 해결에 적용될 수 있습니다.
