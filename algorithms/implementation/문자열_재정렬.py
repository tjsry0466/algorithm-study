# 문자열부터 오름차순으로 정렬하고 그 뒤에 숫자를 더한값을 붙여서 출력

input_str = input()

str_list = []
num = 0

for i in input_str:
    if i.isalpha():
        str_list.append(i)
    else:
        num += int(i)

str_list.sort()
print("".join(str_list) + str(num))
