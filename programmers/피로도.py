# https://school.programmers.co.kr/learn/courses/30/lessons/87946

# 탐험을 시작할 때 필요한 최소필요 필요도
# 탐험을 마쳤을 떄 소모되는 소모 피로도
# 던전을 최대한 많이 참여할 수 있는 최대 던전 수

# K 는 5천 이하
# 던전은 8 이하

# 모든 순열에 대한 피로도를 구하면될듯.

import itertools


def solution(k, dungeons):
    answer = 0
    for i in list(itertools.permutations(dungeons, len(dungeons))):
        current = k
        current_answer = 0
        for j in i:
            require, use = j
            if current >= require and current >= use:
                current -= use
                current_answer += 1

        answer = max(answer, current_answer)
    return answer
