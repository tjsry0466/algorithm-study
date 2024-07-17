N, M = map(int, input().split())

answer = 99999999999

home = []
chick = []

for i in range(N):
  row = list(map(int, input().split()))

  for j in range(N):
    if row[j] == 1:
      home.append((i, j))
    elif row[j] == 2:
      chick.append((i, j))

visited = [False] * len(chick)

def dfs(idx, cnt):
  global answer

  if (cnt == M):
    ans = 0
    
    for i in home:
      distance = 999999999
      for j in range(len(visited)):
        if (visited[j]):
          check_num = abs(i[0]-chick[j][0])+abs(i[1]-chick[j][1])
          distance = min(distance, check_num)
      ans += distance
    answer = min(ans, answer)

    return
  
  for i in range(idx, len(chick)):
    if not visited[i]:
      visited[i] = True
      dfs(i+1, cnt+1)
      visited[i] = False

dfs(0, 0)

print(answer)