# https://www.acmicpc.net/problem/1495

# N개의 곡을 연주
# 매번 곡이 시자하기 전에 볼륨을 바꾸고 연주
# 볼륨 리스트 V. V[i]는 i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨을 의미
# 현재 볼륨이 P. i번째 곡을 연주하기 전이라면, i번 곡은 P+V[i]나 P-V[i]로 연주해야 한다.
# 0보다 작은 값으로 볼륨을 바꾸거나, M보다 큰 값으로 볼륨을 바꿀 수 없다.
# 곡의 개수 N, 시작 볼륨 S, 그리고 최대 볼륨 M이 주어졌을 때, 마지막 곡을 연주할 수 있는 볼륨 중 최댓값을 구하는 문제

# 백트래킹을 무조건 써야할 것 같음.

N, S, M = map(int, input().split())
volumes = list(map(int,input().split()))
dp = [0 for _ in range(N+1)]

dp[0] = S

max_x = 0

def recr(x, v):
	global max_x
	max_x = max(max_x, x)
	
	dp[x] = max(dp[x], v)

	if (x == N):
		return

	add = v + volumes[x]
	subtract = v - volumes[x]

	if (add <= M):
		recr(x+1, add)
	
	if (subtract >= 0):
		recr(x+1, subtract)

recr(0, S)
if (max_x != N):
	print(-1)
else:
	print(dp[N])


# 정답

N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))

# dp[i][j]는 i번째 곡을 연주할 때 볼륨 j가 가능한지 여부를 나타냄
dp = [[False] * (M + 1) for _ in range(N + 1)]
dp[0][S] = True

for i in range(1, N + 1):
    for j in range(M + 1):
        if dp[i - 1][j]:
            if j + volumes[i - 1] <= M:
                dp[i][j + volumes[i - 1]] = True
            if j - volumes[i - 1] >= 0:
                dp[i][j - volumes[i - 1]] = True

max_volume = -1
for j in range(M + 1):
    if dp[N][j]:
        max_volume = j

print(max_volume)
