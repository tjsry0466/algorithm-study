# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하는 문제

# 숫자 numbers와 제거할 수의 개수 k. 최대 백만

# 큰수를 만드려면 앞에 위치한 수가 뒤에 위치한 수보다 커야한다.
# 인덱스별로 탐색하면서 앞에있는 수가 크도록 하면 된다.

# 내가 풀 풀이 (실패)
# def solution(number, k):
#     answer = []

#     number = list(number)

#     i = 1
#     while (i < len(number) and k > 0):
#         if (number[i-1] < number[i]):
#             number.pop(i-1)
#             k-=1
#             continue

#         if (i != len(number)-1 and number[i+1] > number[i]):
#             number.pop(i)
#             k-=1
#             continue

#         i+=1

#     return "".join(number[:len(number)-k])


def solution(number, k):
    stack = []

    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # 만약 제거 횟수가 남아있는 경우 뒤에서 부터 제거
    if k > 0:
        stack = stack[:-k]

    return "".join(stack)
