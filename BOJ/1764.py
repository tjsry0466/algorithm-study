# https://www.acmicpc.net/problem/1764

# 듣도 못한 사람의 명단과 보도 못한 사람의 명단이 주어질 때
# 듣도 보도 못한 사람의 명단을 구하는 문제

# 집합 A와 집합 B에 공통으로 존재하는 요소를 구하는 문제

N, M = map(int, input().split())

group1 = set([input() for _ in range(N)])
group2 = set([input() for _ in range(M)])

intersection = list(group1 & group2)
intersection.sort()

print(len(intersection))
for i in intersection:
    print(i)
