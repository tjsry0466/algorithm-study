# https://www.acmicpc.net/problem/9184

# 아래와 같은 재귀함수가 있다.
# if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
#     1

# if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
#     w(20, 20, 20)

# if a < b and b < c, then w(a, b, c) returns:
#     w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

# otherwise it returns:
#     w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

# 위 함수로 값을 구하면 오래걸린다. ex) a=15, b=15, c=15
# a, b, c가 주어졌을 때 w(a, b, c)를 구하는 문제

from collections import defaultdict

dict = defaultdict(int)

def w(a, b, c):
	if (a <= 0 or b <= 0 or c <= 0):
		return 1
	
	if ( a > 20 or b > 20 or c > 20):
		return w(20, 20, 20)
	
	key = f"{a}|{b}|{c}"
	value = dict.get(key)
	if (value):
		return value
	
	if (a < b and b < c):
		v =  w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
		dict[key] = v
		return v
	else:
		v = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
		dict[key] = v
		return v

while True:
	a, b, c = map(int, input().split())
	if (a == -1 and b == -1 and c == -1):
		exit()
	print(f"w({a}, {b}, {c}) = {w(a, b, c)}")


	
print(w(1, 1, 1)) # 2
print(w(2, 2, 2)) # 4
print(w(10, 4, 6)) # 523
print(w(50, 50, 50)) # 1048576
print(w(-1, 7, 18)) # 1