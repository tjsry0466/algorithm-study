# https://www.acmicpc.net/problem/2644

# 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현
# 부모와 자식 사이를 1촌으로 정의
# 할아버지는 2촌
# 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌
# 여러 사람들에 대한 부모 자실들 간의 관계가 주어졌을 때, 두 사람의 촌수를 계산하는 문제

# 사람들은 1부터 100까지 연속된 번호로 표시

from collections import defaultdict

N = int(input())
A, B = map(int, input().split())
M = int(input())

dict = defaultdict(set)

arr = []

for i in range(M):
	A1, B1 = map(int, input().split())
	arr.append([A1, B1])
	dict[A1].add(B1)
	dict[B1].add(A1)

arr.sort(key= lambda x: x[1])

min_value = min(A, B)
max_value = max(A, B)

q = [min_value]

visited = []
def bfs(x, sources):
	global visited
	global dict

	# print("sources", sources)

	while len(sources) > 0:
		source = sources.pop()

		if (source == max_value):
			print(x)
			exit()

		visited.append(source)
		targets = list(dict.get(source))

		filteredTargets = list(filter(lambda x: not x in visited, targets))
		
		bfs(x+1, filteredTargets)

visited += [min_value]
items = list(dict.get(min_value))

bfs(1, items)
print(-1)

# test case
# 6
# 1 5
# 5
# 1 2
# 2 3
# 2 4
# 4 5
# 4 6