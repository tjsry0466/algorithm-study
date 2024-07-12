def recursion(arr):
    arr_length = len(arr)
    if (arr_length == 1):
        return '-'
    elif (arr_length == 3):
        return '- -'
    
    divide_3_length = arr_length // 3

    return recursion(arr[0:divide_3_length]) + (divide_3_length * ' ') + recursion(arr[divide_3_length * 2:arr_length])
    

while True:
    try:
        N = int(input())
        arr = '-' * (3 ** N)
        print(recursion(arr))
    except:
        break
    