# https://school.programmers.co.kr/learn/courses/30/lessons/12915
# 문자열 리스트 strings, 정수 n
# 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬

def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n], x))