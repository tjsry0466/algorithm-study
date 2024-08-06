# A, E, I O U만을 사용해서 만들 수 있는 길이 5이하의 모든 단어가 수록
# 사전에서 첫 번쨰 단어는 A, 그 다음은 AA, 마지막 단어는 UUUUU

# 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번쨰 단어인지 return

# 접근 방법
# 직저 순서대로 하나씩 해보면서 몇 번째 단어인지 구해야 한다.
# 사전순으로 생성했을 때 어떤식으로 생성되는지?
# 조합을 1개, 2개, 3개, 4개, 5개로 구해서 배열에 넣고 정렬한 뒤에 찾으면 나오지 안을까 싶음.

import itertools


def solution(word):
    jaum = ['a', 'e', 'i', 'o', 'u']
    arr = []
    for i in range(1, len(jaum)+1):
        texts = list(map(lambda x: "".join(x), itertools.product(jaum, repeat = i)))
        arr += texts

    arr.sort()
    
    for idx, i in enumerate(arr):
        print(i, word)
        if (i.upper() == word):
            return idx + 1