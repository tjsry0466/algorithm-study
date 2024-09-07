# https://school.programmers.co.kr/learn/courses/30/lessons/1845

# 최대한 많은 종류의 포켓몬을 포함해서 N/2마리를 선택
# 최대한 다양한 포켓몬을 가지도록 선택

from collections import defaultdict


def solution(nums):

    count = len(nums) // 2

    dict = defaultdict(int)

    for i in nums:
        dict[i] += 1

    a = len(sorted(list(dict.items()), key=lambda x: -x[1]))
    b = count

    return min(a, b)
