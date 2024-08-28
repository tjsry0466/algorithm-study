# 특정 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번쨰로 실행되는지 알아내기
# 1. 실행 대기 큐에서 대기중인 프로세스 하나 꺼내기
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣기
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 종료

# 접근 방법
# priorities의 최대의 길이가 100이므로 브루트포스로 풀이
# 처리할 프로세스의 위치(location)와 현재까지 처리된 프로세스의 수(count)를 증가시키며 처리할 프로세스를 처리했을때 정답 반환

from collections import deque

def solution(priorities, location):
    count = 0
    q = deque(priorities)
    
    while len(q) > 0:
        item = q.popleft()
        location -=1
        
        if max(q) > item:
            if (location == -1):
                location = len(q)
            q.append(item)
        else:
            count +=1
            if (location == -1):
                return count
            
        if len(q) == 1:
            return count+1