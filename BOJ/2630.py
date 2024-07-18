# https://seonkyo.notion.site/BOJ-2630-ee956dcaef6b4102959640bc834e6594?pvs=74

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

zero_area_count = 0
one_area_count = 0

def dfs(sub_board, N):
  global one_area_count
  global zero_area_count
  
  listSum = sum([sum(i) for i in sub_board])

  if (N == 2): # 종료 조건
    if (listSum == 4):
      one_area_count += 1
    elif (listSum == 0):
      zero_area_count += 1
    else:
      one_area_count += listSum
      zero_area_count += (4 - listSum)
    return

  if (listSum == N*N):
    one_area_count += 1
    return
	
  if (listSum == 0):
    zero_area_count += 1
    return 
	
	
  # 4등분해서 각각 호출
  
  half = N // 2
  dfs([row[:half] for row in sub_board[:half]], half)
  dfs([row[half:] for row in sub_board[:half]], half) 
  dfs([row[:half] for row in sub_board[half:]], half)
  dfs([row[half:] for row in sub_board[half:]], half)

dfs(board, N)

print(zero_area_count)
print(one_area_count)