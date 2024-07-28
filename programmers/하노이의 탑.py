# https://school.programmers.co.kr/learn/courses/30/lessons/12946
# 1. 원반이 한 개일 때 (n=1)
#     시작 지점에서 끝 지점으로 바로 이동 합니다.
# 2. 원반이 n 개일 때
#     1) 1번 기둥에 있는 n개 원반 중 n-1 개를 2번 기둥으로 옮깁니다.
#     2) 1번 기둥에 남아 있는 가장 큰 원반을 3번 기둥으로 옮깁니다.
#     3) 2번 기둥에 남아 있는 n-1 개의 원반을 3번 기둥으로 옮깁니다.

def solution(n):
	answer = []
	
	def hanoi(n, start, end, via):
		if n == 1:
			answer.append([start, end])
			return
		
		hanoi(n-1, start, via, end)
		
		answer.append([start, end])
		
		hanoi(n-1, via, end, start)
			
	hanoi(n, 1, 3, 2)
	return answer