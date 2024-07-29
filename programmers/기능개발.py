# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 진도가 100%일 때 서비스에 반영

# 뒤에 있는 기능이 먼저 개발된다면 앞에 있는 기능이 배포될 때 함께 배포
# 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses
# 각 작업의 개발 속도가 적힌 정수 배열 speeds
# 각 배포마다 몇개의 기능이 배포되는지 배열로 반환

# 작업의 개수는 100 이하 O(N^4)까지 가능

# 접근 방법
# 7, 3, 9와 같이 작업을 완료하는데 걸리는 시간을 배열에 정리해두고
# 앞에서부터 탐색하면서 숫자가 증가하기 직전까지 하나의 배포 단위로 묶음.
# 7, 3, 9 같은 경우에는 [7, 3]가 같이 배포될 수 있음.


def solution(progresses, speeds):
    answer = []
    
    done = []
    
    for i in range(len(speeds)):
        for j in range(1, 101):
            if (progresses[i]+speeds[i]*j >= 100):
                done.append(j)
                break
    
    current_day = done[0]
    count = 1
    for i in range(1, len(done)):
        if (current_day < done[i]):
            answer.append(count)
            current_day = done[i]
            count = 1
        else:
            count += 1
            
    answer.append(count)
    
    return answer