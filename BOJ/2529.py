# https://www.acmicpc.net/problem/2529

# 두 종류의 부등호 기호와 k개의 나열된 순서열 A
# 부등호 앞뒤에 서로 다른 한 자리수 숫자를 넣어서 모든 부등호 관계를 만족시키는 문제
# 선택된 숫자는 모두 달라야하고, 최대값과 최소값을 구하면 된다.

# DFS + 백트래킹 활용
# 값을 모두 선택했을 때 최고값이랑 최저값을 지정.

from itertools import permutations

def check_valid(sequence, signs):
    for i in range(len(signs)):
        if signs[i] == '<' and sequence[i] >= sequence[i+1]:
            return False
        if signs[i] == '>' and sequence[i] <= sequence[i+1]:
            return False
    return True

def find_min_max(N, signs):
    numbers = range(10)
    min_value = None
    max_value = None
    
    for perm in permutations(numbers, N+1):
        if check_valid(perm, signs):
            value = ''.join(map(str, perm))
            if min_value is None or value < min_value:
                min_value = value
            if max_value is None or value > max_value:
                max_value = value
                
    return min_value, max_value

N = int(input())
signs = input().split()
min_value, max_value = find_min_max(N, signs)
print(max_value)
print(min_value)
