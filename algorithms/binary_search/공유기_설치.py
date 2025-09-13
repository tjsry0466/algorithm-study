import sys

input = sys.stdin.readline


def is_possible(arr, c, distance):
    previous_value = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if arr[i] - previous_value >= distance:
            count += 1
            previous_value = arr[i]

    if count >= c:
        return True

    return False


def binary_search(arr, c, start, end):
    global result

    if start > end:
        return

    mid = (start + end) // 2

    if is_possible(arr, c, mid):
        result = max(result, mid)
        return binary_search(arr, c, mid + 1, end)
    else:
        return binary_search(arr, c, start, mid - 1)


result = 0

n, c = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()

binary_search(arr, c, 1, arr[-1] - arr[0])
print(result)
