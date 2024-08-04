# https://www.acmicpc.net/problem/10816

# 숫자 카드 2

# 숫자 카드 N개. 정수 M개가 주어졌을 때
# 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램 작성

# 첫째 줄에 상근이가 가지고 있는 수자 카드의 개수 N (1 이상 500,000 이하)
# 둘째 줄에는 숫자 카드가 적혀 있는 정수
# 셋째 줄에는 M(1 이상 500,000 이하)
# 넷째 줄에는 상근이가 몇 개 가지고 있는 숮자 카드인지 구해야 할 M개의 정수 (-10,000,000 이상 10,000,000 이하)

# 해시에 개수를 저장해서 푼다.

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

from collections import defaultdict

dict = defaultdict(int)

for i in cards:
	dict[str(i)] += 1

answer = []
for i in numbers:
	found = dict.get(str(i))
	answer.append(found if found else 0)

print(" ".join(map(str, answer)))