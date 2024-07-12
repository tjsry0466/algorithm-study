from collections import defaultdict

n = int(input())

meet = defaultdict(set)

visited = set()
chong = 'ChongChong'
visited.add(chong)
flag = False
for _ in range(n):
  A, B = input().split()
  if (flag == True or chong == A or chong == B):
    flag = True
    if (A in visited or B in visited):
      visited.add(A) 
      visited.add(B)


print(len(visited))
    
