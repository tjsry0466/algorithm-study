# https://www.acmicpc.net/problem/1889

# 선물 교환 이벤트를 한다.
# 각자 두개의 선물을 준비해 두명의 친구에게 준다.
# 모든 학생들이 두 개의 선물을 주고, 정확히 두 개의 선물만을 받도록 해야한다.
# 주고자 하는 두 명의 학생이 누구인지 알아냈을 때 모든 인원들이 선물을 두 개씩 받도록 하는 학생이 최대가 되는 참여 학생들을 구하는 문제

# 입력
# 학생수는 3명 이상 20만명 이하

# 출력
# 첫째 줄에 최대로 참여시킬 수 있는 학생의 수를 출력
# 둘째 줄에는 참여할 학생들의 번호를 증가하는 순서대로 빈 칸을 사이에 두고 출력
# 가능한 방법중 한가지를 출력하면 됨
# 한명의 학생도 참여시킬 수 없는 경우에는 첫째 줄에 0만 출력

from collections import defaultdict, deque


def bfs_remove_edges(start_node):
    """연결된 엣지가 2개 미만인 노드를 제거하는 BFS 함수"""
    queue = deque([start_node])

    while queue:
        node = queue.popleft()

        if len(adj_list[node]) < 2 and answers[node] == 1:
            a, b = edges[node]
            adj_list[a].remove(node)
            adj_list[b].remove(node)
            answers[node] = 0

            # 두 노드가 2개 미만의 엣지를 가지면 큐에 추가
            if len(adj_list[a]) < 2:
                queue.append(a)
            if len(adj_list[b]) < 2:
                queue.append(b)


def main():
    size = int(input().strip())

    # 초기화
    global edges, adj_list, answers
    edges = [None] * (size + 1)
    adj_list = defaultdict(list)
    answers = [1] * (size + 1)

    # 입력 처리
    for i in range(1, size + 1):
        a, b = map(int, input().split())
        adj_list[a].append(i)
        adj_list[b].append(i)
        edges[i] = (a, b)

    # BFS 방식으로 엣지 제거
    for i in range(1, size + 1):
        bfs_remove_edges(i)

    # 결과 출력
    result = [i for i in range(1, size + 1) if answers[i] == 1]

    if result:
        print(len(result))
        print(" ".join(map(str, result)))
    else:
        print(0)


if __name__ == "__main__":
    main()
