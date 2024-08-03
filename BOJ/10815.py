# https://www.acmicpc.net/problem/10815

# 숫자 카드 N개
# 정수 M개
# 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지 구하는 프로그램

# 첫째줄에는 상근이가 가지고 있는 수자 카드의 개수 N (50만 이하)
# 둘째줄에는 숫자 카드에 적혀 있는 정수
# 숫자 카드에 적혀 있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
# 두 숫자 카드에 같은 수가 적혀있는 경우는 없음
# 셋째줄에는 1이상 50만 이하의 M
# 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지 구해야할 M개의 정수. -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

N = int(input())
numCards = list(map(int, input().split()))

M = int(input())
numbers = list(map(int, input().split()))

dict = dict()
for i in numCards:
	dict[i] = True

answer = []
for i in numbers:
	answer.append("1" if dict.get(i) == True else "0")

print(" ".join(answer))


	