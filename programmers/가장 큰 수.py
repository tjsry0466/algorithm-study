# https://school.programmers.co.kr/learn/courses/30/lessons/42746

# 정렬이지만 그리디 알고리즘으로 최적의 요소를 찾는 문제
# 각 값에 곱하기 3을 해서 구함으로써 문자열간에 비교로 큰 수를 찾을 수 있게 된다.


def solution(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(key=lambda x: x * 3, reverse=True)

    answer = "".join(numbers)

    return "0" if answer[0] == "0" else answer
