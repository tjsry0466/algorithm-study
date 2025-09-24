# 1부터 떡의 길이중 제일 높은 값 -1 까지 자를 수 있음.
# 이진탐색을 통해 자를 수 있는 떡의 길이를 찾음.
# 적어도 m만큼 떡을 가져갈 때 자르는 길이를 구하는 문제


def binary_search(rices, target, start, end):
    global result

    if start > end:
        return

    mid = (start + end) // 2

    # h는 남는 값
    h = sum(map(lambda x: max(x - mid, 0), rices))

    # print(h, list(map(lambda x: max(x - mid, 0), rices)))
    # print(mid, target)

    # 많이 남으면 (h가 target보다 크면) 조건은 만족, 더 작은게 있는지 찾아야함.
    if target <= h:
        result = max(result, mid)
        return binary_search(rices, target, mid + 1, end)
    # 많이 남으면 (h가 target보다 크면) 조건을 만족하지 않음, 더 큰값을 탐색해야 함.
    else:
        return binary_search(rices, target, start, mid - 1)


n, m = map(int, input().split())
h = list(map(int, input().split()))

max_height = max(h)

result = 0
binary_search(h, m, 1, max_height - 1)
print(result)
