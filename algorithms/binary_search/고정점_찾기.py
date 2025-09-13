def binary_search(arr, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if mid + 1 == arr[mid + 1]:
        return mid + 1
    elif arr[mid] < mid + 1:
        return binary_search(arr, mid + 1, end)
    else:
        return binary_search(arr, start, mid - 1)


n = int(input())
arr = list(map(int, input().split()))

print(binary_search(arr, 0, len(arr)))
