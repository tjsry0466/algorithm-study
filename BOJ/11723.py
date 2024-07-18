# https://seonkyo.notion.site/Python-0d3378bbb1704111ba34d02ff89f2d29?pvs=4

import sys

m = int(sys.stdin.readline())
s = set()

for _ in range(m):
  temp = sys.stdin.readline().strip().split()

  if len(temp) == 1:
    if temp[0] == "all":
      S = set([i for i in range(1, 21)])
    else:
      # empty
      S = set()

  else:
    func, x = temp[0], int(temp[1])

    if func == 'add':
      S.add(x)
    elif func == "remove":
      S.discard(x)
    elif func == 'check':
      print(1 if x in S else 0)
    elif func == 'toggle':
      if x in S:
        S.discard(x)
      else:
        S.add(x)