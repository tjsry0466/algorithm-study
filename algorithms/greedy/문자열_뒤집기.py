# 문자열이 주어지면 0이랑 1의 묶음 수를 세고 작은쪽이 정답

str = input()

countZero = 0
countOne = 0

# 0 묶음 수 세기
init = 1
for i in range(len(str)):
    if init == 1 and str[i] == "0":
        countZero += 1
        init = 0
    elif init == 0 and str[i] == "0":
        continue
    elif init == 0 and str[i] == "1":
        init = 1

# 1 묶음 수 세기
init = 1
for i in range(len(str)):
    if init == 1 and str[i] == "1":
        countOne += 1
        init = 0
    elif init == 0 and str[i] == "1":
        continue
    elif init == 0 and str[i] == "0":
        init = 1

print(min(countZero, countOne))
