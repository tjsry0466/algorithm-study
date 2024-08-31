# https://www.acmicpc.net/problem/1822

# 몇 개의 자연수로 이루어진 두 집합 A와 B
# A에는 속하면서 B에는 속하지 않는 모든 원소를 구하는 문제

# nA와 nB는 최대 50만
# 이분탐색으로 접근하면 최대 50만인 경우 13번만에 접근이 가능하므로 모든 A집합에 대해 순회하면서 구해도 괜찮을 것 같다.
# 정렬을 해두면 B집합에 대해서 탐색할 때 특정 수 이상인 부분은 탐색하지 않도록 최적화도 가능해 보인다.


def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False


nA, nB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()

answer = []
for i in A:
    if not binary_search(i, B):
        answer.append(i)

if answer:
    answer.sort()
    print(len(answer))
    print(" ".join(map(str, answer)))
else:
    print(0)


# set을 활용한 풀이도 가능
nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = sorted(A - B)

if result:
    print(len(result))
    print(" ".join(map(str, result)))
else:
    print(0)
