import itertools

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# 순열 구하기
combinations = sorted(set(list(itertools.combinations(arr, M))))

# 출력
for i in combinations:
  print(*i)

  