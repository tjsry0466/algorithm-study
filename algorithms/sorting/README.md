### 정렬 알고리즘

정렬 알고리즘은 데이터 집합을 특정 순서(오름차순 또는 내림차순)로 정렬하는 알고리즘입니다. 다양한 정렬 알고리즘이 존재하며, 각각의 알고리즘은 특정 상황에서 더 효율적일 수 있습니다. 아래에서는 몇 가지 대표적인 정렬 알고리즘을 설명합니다.

#### 1. 버블 정렬 (Bubble Sort)

**버블 정렬**은 가장 간단한 정렬 알고리즘 중 하나로, 인접한 두 요소를 비교하여 순서가 잘못된 경우 위치를 교환합니다. 이 과정이 반복되면, 큰 값이 점차 뒤쪽으로 이동하여 정렬이 완료됩니다.

- **작동 방식**:
  - 리스트의 처음부터 끝까지 순회하면서, 인접한 두 요소를 비교하고 교환합니다.
  - 첫 번째 순회에서 가장 큰 값이 리스트의 끝으로 이동합니다.
  - 이 과정을 리스트가 완전히 정렬될 때까지 반복합니다.
- **시간 복잡도**:

  - 최선: O(n) (이미 정렬된 경우)
  - 평균 및 최악: O(n²)

- **특징**:
  - 구현이 매우 간단하지만, 효율성은 낮습니다.
  - 데이터의 이동이 많아 큰 데이터셋에는 적합하지 않습니다.

#### 2. 삽입 정렬 (Insertion Sort)

**삽입 정렬**은 리스트를 순차적으로 순회하며, 각 요소를 적절한 위치에 삽입하여 정렬하는 방식입니다. 이미 정렬된 부분 리스트에서 올바른 위치를 찾아가며 삽입하는 과정을 반복합니다.

- **작동 방식**:

  - 리스트의 두 번째 요소부터 시작하여, 이전 요소들과 비교해 알맞은 위치에 삽입합니다.
  - 리스트의 크기가 커질수록, 요소를 삽입하기 위해 비교와 이동이 필요합니다.

- **시간 복잡도**:

  - 최선: O(n) (이미 정렬된 경우)
  - 평균 및 최악: O(n²)

- **특징**:
  - 작은 데이터셋이나 거의 정렬된 리스트에 효과적입니다.
  - 구현이 간단하고, 안정적인 정렬입니다.

#### 3. 퀵 정렬 (Quick Sort)

**퀵 정렬**은 분할 정복 알고리즘으로, 리스트를 두 개의 부분 리스트로 나누고 각각을 재귀적으로 정렬합니다. 피벗(pivot)을 설정하여, 피벗보다 작은 요소들은 왼쪽으로, 큰 요소들은 오른쪽으로 이동시키는 과정입니다.

- **작동 방식**:

  - 피벗을 선택하고, 리스트를 피벗을 기준으로 두 부분으로 분할합니다.
  - 피벗보다 작은 값들은 왼쪽에, 큰 값들은 오른쪽에 위치하게 합니다.
  - 이 과정을 재귀적으로 반복하여 리스트를 정렬합니다.

- **시간 복잡도**:

  - 최선 및 평균: O(n log n)
  - 최악: O(n²) (불균형하게 분할된 경우)

- **특징**:
  - 대부분의 경우 매우 빠르고 효율적입니다.
  - 불균형한 분할이 발생할 수 있으므로, 피벗 선택에 주의해야 합니다.

#### 4. 병합 정렬 (Merge Sort)

**병합 정렬** 역시 분할 정복 알고리즘의 일종으로, 리스트를 반으로 나누어 각각을 정렬한 후 병합하여 최종 정렬된 리스트를 만듭니다. 안정적인 정렬 알고리즘으로, 항상 O(n log n)의 시간 복잡도를 가집니다.

- **작동 방식**:

  - 리스트를 반으로 나누어 더 이상 나눌 수 없을 때까지 재귀적으로 나눕니다.
  - 각 부분 리스트를 정렬한 후, 병합하여 정렬된 리스트를 만듭니다.

- **시간 복잡도**:

  - 항상 O(n log n)

- **특징**:
  - 안정적인 정렬 알고리즘으로, 데이터의 크기에 상관없이 일정한 성능을 보입니다.
  - 추가적인 메모리 공간이 필요합니다.

#### 5. 힙 정렬 (Heap Sort)

**힙 정렬**은 힙(Heap) 자료구조를 이용한 정렬 알고리즘입니다. 최대 힙이나 최소 힙을 구성하여, 루트 노드(최대 또는 최소값)를 반복적으로 제거하고 리스트의 끝으로 보내는 과정을 통해 정렬합니다.

- **작동 방식**:

  - 주어진 리스트를 힙 구조로 변환합니다.
  - 힙의 루트 노드(최대값 또는 최소값)를 리스트의 끝으로 이동시키고, 남은 리스트에서 힙을 재구성합니다.
  - 이 과정을 반복하여 정렬된 리스트를 만듭니다.

- **시간 복잡도**:

  - 항상 O(n log n)

- **특징**:
  - 추가적인 메모리 공간이 거의 필요하지 않습니다(제자리 정렬).
  - 안정적인 정렬은 아니지만, 큰 데이터셋에 효율적입니다.
