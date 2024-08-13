# LIS (최장 증가 부분 수열, Longest Increasing Subsequence)

- 최장 증가 부분 수열은 말 그대로 가장 길게 증가하는 부분 수열
- 어떤 수열에서 만들 수 있는 부분 수열 중에서 가장 길면서 오름차순을 유지하는 수열을 LIS라고 한다.

# LIS를 구현하는 방법

- DP

```python
# BOJ 11053번
x = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
```

N개의 수들에 대해서 현재 위치 이전의 모든 수를 다 훑어봐야 하므로 O(N^2)의 시간복잡도를 가지게 된다.

- 이분 탐색

```python
# BOJ 12015번
from bisect import bisect_left #이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다

input()
A = list(map(int, input().split()))
dp = []

for i in A:
    k = bisect_left(dp, i) #자신이 들어갈 위치 k
    if len(dp) <= k: #i가 가장 큰 숫자라면
        dp.append(i)
    else:
        dp[k] = i #자신보다 큰 수 중 최솟값과 대체
print(len(dp))
```

N개의 수들에 대해 이진 탐색을 진행하므로 O(NlogN)의 시간 복잡도를 가지게 된다.

# 참고 자료

[가장 긴 증가하는 부분 수열(LIS) 완전 정복 - 백준 파이썬](https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
