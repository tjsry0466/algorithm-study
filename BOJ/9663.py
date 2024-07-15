# -*- coding: utf-8 -*-
n = int(input())

ans = 0
# 퀸을 i, j 위치 위치하기 위해 배열 생성
# 퀸 특성상 같은 행/렬에는 다른 퀸을 못놓는 점을 활용
row = [0] * n

def is_promising(x):
    # 앞에서부터 순차적으로 퀸을 놓고 있어 이전까지만 조사.
    for i in range(x):
        # 앞선 부분에서는 같은 열에 있는지 조사
        # 뒷 부분에서는 대각선에 있는지 조사
        # 행당 하나만 놓고 있기 때문에 같은 행에 대해서는 조사하지 않음.
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # 퀸을 i, j 위치에 놓겠다는 의미
            row[x] = i 
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)