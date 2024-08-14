# https://www.acmicpc.net/problem/2096

# N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있음.
# 내려가기 게임을 하고 있는데 첫줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이임

# 내려갈때에는 바로 아래의 수로 넘어가거나 바로 아래와 붙어있는 수로만 이동할 수 있다.

# 점화식
# 최소값
# 0인 경우
# dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + board[i][0]
# 1인 경우
# dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + board[i][1]
# 2인 경우
# dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + board[i][2]

# 최대값
# 0인 경우
# dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + board[i][0]
# 1인 경우
# dp[i][1] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + board[i][1]
# 2인 경우
# dp[i][2] = max(dp[i-1][1], dp[i-1][2]) + board[i][2]

N = int(input())

# 첫 번째 줄 입력 받아 초기화
first_line = list(map(int, input().split()))
max_dp = first_line[:]  # 첫 줄의 값을 그대로 사용
min_dp = first_line[:]  # 첫 줄의 값을 그대로 사용

for i in range(1, N):
		board = list(map(int, input().split()))

		# 이전 상태를 저장해두기 위해 복사
		previous_max = max_dp[:]
		previous_min = min_dp[:]

		# 최대값 계산
		max_dp[0] = max(previous_max[0], previous_max[1]) + board[0]
		max_dp[1] = max(previous_max[0], previous_max[1], previous_max[2]) + board[1]
		max_dp[2] = max(previous_max[1], previous_max[2]) + board[2]

    # 최소값 계산
		min_dp[0] = min(previous_min[0], previous_min[1]) + board[0]
		min_dp[1] = min(previous_min[0], previous_min[1], previous_min[2]) + board[1]
		min_dp[2] = min(previous_min[1], previous_min[2]) + board[2]

# 최종 결과 출력
print(max(max_dp), min(min_dp))