N = int(input())
size_list = map(int, input().split())
T, P = map(int, input().split())

mookeum = N // P
jaru = N % P

tshirt = 0
for i in size_list:
  if (i % T == 0):
    tshirt += i // T
  else:
    tshirt += i // T + 1

print(tshirt)
print(mookeum, jaru)
