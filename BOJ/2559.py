A, B = map(int, input().split())
arr = list(map(int,input().split()))

prefix = [0 for _ in range(A+1)]

# prefix 구하기
for i in range(A):
	prefix[i + 1] = prefix[i] + arr[i]
	
# 특정 위치에서 B를 뺀 위치의 값을 빼서 특정 위치에서의 값을 구한다.
for k in range(B, A+1):
	answer.append(prefix[k] - prefix[k-B])
	
print(max(answer))