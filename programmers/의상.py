# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 매일 다른 옷을 조합해 입음
# 각 종류별로 최대 1가지만 착용 가능
# 착용한 의상의 일부가 겹치더라도 추가로 착용한 경우에는 다른 옷을 착용한 것임.
# 최소 하루 한개는 입음.
# 의상목록이 주어질 때 서로 다른 옷의 조합의 수를 리턴
# 의상은 총 30개 이하 -> 구현만 하면 앵간하면 통과할듯.

# 접근 방법
# NM: N과 M을 모두 사용하는 경우
# N: N만 사용하는 경우
# M: M만 사용하는 경우
# 1: 모두 사용하지 않는 경우 

# 모두 사용하지 않는 경우를 고려해
# (N+1) * (M+1)로 모든 경우의수를 구할 수 있다.


from collections import defaultdict
from functools import reduce


def solution(clothes):
    dict = defaultdict(list)
    for i in clothes:
        name, type = i
        dict[type].append(dict)
    
    # A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수 (N+1)(M+1)
    answer = 1
    for _, value in dict.items():
        answer *= (len(value) + 1)
        
    return answer -1