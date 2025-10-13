import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if x <= 0:
        return 0
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def main():
    g = int(input())
    p = int(input())

    parent = [i for i in range(g + 1)]  # 0은 센티널(더 이상 없음)

    docked_count = 0
    for _ in range(p):
        max_gate = int(input())
        available_gate = find_parent(parent, max_gate)
        if available_gate == 0:
            break
        # available_gate에 도킹 후, 그 게이트의 대표를 (available_gate - 1)의 대표로 연결
        parent[available_gate] = find_parent(parent, available_gate - 1)
        docked_count += 1

    print(docked_count)


if __name__ == "__main__":
    main()
