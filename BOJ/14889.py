# https://www.acmicpc.net/problem/14889

# 모인사람은 총 N명, N은 짝수
# N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.
# 사람에게 번호를 1부터 N까지로 배정.
# 같이 팀 했을때 부여되는 능력치를 나열함.

# N은 최대 20.
# S(i,j)는 1보다 크거나 같고 100보다 작거나 같은 정수

# 접근 방법
# 우선 완전탐색으로 접근해봐야할 것 같다.
# N/2명 중 한명을 고르고 다음 사람을 고르거나, 고르지 않거나 선택한다.
# 사람을 4명 넘게 골랐거나 4명을 충분히 고르지 않은 상태에서 8명을 다 패스했다면 종료 조건.
# 정답 변수를 두고 4명을 골랐을때 차이를 검사한다. 
# 0이면 이보다 작은 최소값은 없으니 종료하고 0이 아니라면 정답과 비교해서 최소값을 정답에 할당한다.

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
sumBoard = sum([sum(i) for i in board])

members = []
answer = 999999999

def dfs(x): 
	global answer
	if (len(members) > N//2 or x > N):
		return

	if (len(members) == N//2):
			sum = 0
			not_sum = 0

			not_members = []
			for i in range(N):
				if (not i in members):
					not_members.append(i)

			for i in range(len(members) - 1):
				for j in range(i+1, len(members)):
					sum += board[members[i]][members[j]]
					sum += board[members[j]][members[i]]

			for i in range(len(not_members) - 1):
				for j in range(i+1, len(not_members)):
					not_sum += board[not_members[i]][not_members[j]]
					not_sum += board[not_members[j]][not_members[i]]

			answer = min(answer, abs(sum - not_sum))
	
	members.append(x)
	dfs(x+1)
	members.pop()
	dfs(x+1)


dfs(0)
print(answer)