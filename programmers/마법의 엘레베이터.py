# 층 이동은 -1, +1, -10, +10, -100 +100 과 같이 존재
# 0층이 제일 아래층

# 버튼 한 번당 마법의 돌 한개
# 마법의 돌을 최소한으로 사용해서 이동하고 싶음.
# 현재 층이 몇층에 있는지 주어졌을 때 몇번 이동해야하는지 횟수를 묻는 문제

# 해설 참고: https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Programmers-%EB%A7%88%EB%B2%95%EC%9D%98-%EC%97%98%EB%A6%AC%EB%B2%A0%EC%9D%B4%ED%84%B0-Python

import math

def solution(storey):
    
    answer = 0

    while storey:
        remainder = storey % 10
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder
        # 5
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10

    return answer