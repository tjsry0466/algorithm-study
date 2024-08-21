# https://www.acmicpc.net/problem/14248

# n개의 돌이 일렬로 놓여있는 돌다리
# 돌다리에 숫자가 적혀져 있음.
# 숫자가 적혀있는 만큼 왼쪽이나 오른쪽으로 점프할 수 있음.
# 돌다리에서 방문 가능한 돌들의 개수를 알고 싶음
# 방문 가능하다는 것은 현재 위치에서 다른 돌을 적절히 밟아 해당 위치로 이동 가능
# 돌다리 수 최대 10만, 점프할 수 있는 거리 최대 10만
# 출발점 N 보다 작은 수

N = int(input())
arr = list(map(int, input().split()))
a = int(input())

q = [a-1]
visited = [0] * N
visited[a-1] = True

while len(q) > 0:
	idx = q.pop()

	distance = arr[idx]
	for i in [idx-distance, idx+distance]:
		if (i >= 0 and i < len(arr) and not visited[i]):
			visited[i] = True
			q.append(i)

print(sum(visited))
			


