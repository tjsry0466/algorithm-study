# https://school.programmers.co.kr/learn/courses/30/lessons/12954
# 정수 x와 자연수 n을 입력받아 
# x부터 시작해 x씩 증가하는 숫자를 
# n개 지니는 리스트 리턴

def solution(x, n):
    return [x + (i*x) for i in range(n)]