import math


def is_primenum(x):
  if (x< 2):
    return False
  for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
        return False
  return True
                    
n = int(input())
arr = map(int, input().split())
answer = 0
for i in arr:
  if is_primenum(i):
    answer += 1 
    
print(answer)