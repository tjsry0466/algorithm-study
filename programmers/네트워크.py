# https://school.programmers.co.kr/learn/courses/30/lessons/43162

# 연결되어 있는 네트워크를 찾는 문제
# 컴퓨터 개수 N. 최대 200
# 연결에 대한 정보 2차원 배열 computers
# i와 j가 연결되어 있으면 computers[i][j]를 1로 표현

from collections import defaultdict


def solution(n, computers):
    answer = 0
    dict = defaultdict(set)

    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] == 1:
                dict[i].add(j)

    visited = [0 for _ in range(n)]
    q = []
    for i in range(n):
        if not visited[i]:
            q.append(i)
            visited[i] = 1
            answer += 1

        while q:
            item = q.pop()
            nexts = dict.get(item)
            for next in nexts:
                if not visited[next]:
                    visited[next] = 1
                    q.append(next)

    return answer
