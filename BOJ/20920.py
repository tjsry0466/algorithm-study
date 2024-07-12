n, m = list(map(int, input().split()))

arr = [input() for _ in range(n)]
filteredArr = list(filter(lambda x: len(x) >= m, arr))

dict = {}
for i in filteredArr:
	if (i in dict):
		dict[i] +=1
	else:
		dict[i] = 1

def _sort(x):
  name, count = x
  return [-count, len(name), name]

a = sorted(dict.items(), key = _sort)

for i,count in a:
	print(i)