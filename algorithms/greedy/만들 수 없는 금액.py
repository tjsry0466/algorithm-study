# 정렬하고 앞에서부터 몇개씩 집어가지고 순열에 대해 최소값이 커지는지 파악하면 될듯.

from itertools import combinations

n = int(input())

coins = list(map(int, input().split()))
coins.sort()

arr = set()

for i in range(1, n + 1):
    permutation_list = list(combinations(coins, i))
    for permutation in permutation_list:
        arr.add(sum(permutation))

arr = list(arr)
arr.sort()

for i in range(len(arr)):
    if arr[i] != i + 1:
        print(i + 1)
        break
else:
    print(arr[-1] + 1)
