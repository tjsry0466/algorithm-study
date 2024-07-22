import sys

L, C = map(int, input().split())
arr = sorted(input().split())

def dfs(s, x):
  if (x > C or len(s) > L):
    return
  
  if (len(s) == L):
    require_words = ["a", "e", "i", "o", "u"]
    jaum_count = sum([True for i in s if i in require_words])
    
    if (jaum_count > 0 and L - jaum_count > 1):
      print("".join(s))
    return
	
  if (x != C):
    s.append(arr[x])
    dfs(s, x+1)
    s.pop()
    dfs(s, x+1)
  

dfs([], 0)