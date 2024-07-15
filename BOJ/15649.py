N, M = map(int, input().split())

s = []

def dfs(x):
  global arr
  if (x >= M):
    print(" ".join(list(map(str, s))))
    return
  else:
    for i in range(1, N+1):
      if i not in s:
        s.append(i)
        dfs(x+1)
        s.pop()

dfs(0)