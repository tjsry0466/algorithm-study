N, M = map(int, input().split())

s = []

def is_promising(s, x):
  for i in s:
    if (x <= i):
      return False
  return True

def dfs(x):
  if (x == M):
    print(" ".join(list(map(str, s))))
  else:
    for i in range(1, N+1):
      if (is_promising(s, i)):
        s.append(i)
        dfs(x+1)
        s.pop()

dfs(0)