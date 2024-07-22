# https://school.programmers.co.kr/learn/courses/30/lessons/87390?language=python3

def solution(n, left, right):
    flatten_arr =[]

    for i in range(left // n, right // n + 1):
        for j in range(n):
            flatten_arr.append(max(i, j)+1)
    
    start = left % n
    gap = right - left
    return flatten_arr[left % n:start+gap+1]
result = solution(4, 7, 14)
print(result)