K, L, N = list(map(int, input().split()))
arr = list(map(int, list(input()))) + ([0] * L)

answer = []

flush = False
flush_time = 0
count = 0

time = 0
for i in arr:
    time += 1
    if flush:
        if (i == 1):
          count = 0
        else:
            if count + 1 == L:
              answer.append(time)
              flush = False
              count = 0
            else:
              count += 1
    else:
        if i == 1:
            if count + 1 == K:
                count = 0
                flush = True
            else:
                count += 1
        else:
            count = 0


if not flush and len(answer) == 0:
  print('NIKAD')
else:
  for i in answer:
      print(i)