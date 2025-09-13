# 이진 탐색을 하면서 수가 같으면 카운트 start > end 가 될떄까지 하기.


def binary_search(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)


n, x = map(int, input().split())
arr = list(map(int, input().split()))

idx = binary_search(arr, x, 0, n - 1)

if idx == -1:
    print(-1)
    exit()

result = 1

count = 1
while True:
    prev_idx = idx - count
    next_idx = idx + count

    has_next = False

    if 0 <= prev_idx < len(arr):
        prev = arr[idx - count]
        if prev == x:
            has_next = True
            result += 1

    if 0 <= next_idx < len(arr):
        next = arr[idx + count]
        if next == x:
            has_next = True
            result += 1

    if not has_next:
        break

    count += 1

print(result)
