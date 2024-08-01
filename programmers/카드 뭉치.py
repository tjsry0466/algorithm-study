# 카드에 적힌 단어들을 사용해 원하는 순서의 단어 배열을 만들 수 있는지 알고 싶음.

# 조건
# 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용
# 한번 사용한 카드는 다시 사용할 수 없음
# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없음
# 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없음

# 문자열로 이루어진 배열 cards1, cards2와 원하는 단어 배열 goal을 만들 수 있다면 Yes, 없다면 No

def solution(cards1, cards2, goal):
    idx = 0
    cursor1 = 0
    cursor2 = 0
    while True:
        if (cursor1 == len(cards1) and cursor2 == len(cards2)):
            break
            
        if (cursor1 < len(cards1) and goal[idx] == cards1[cursor1]):
            cursor1 += 1
            idx += 1
            continue
            
        if (cursor2 < len(cards2) and goal[idx] == cards2[cursor2]):
            cursor2 += 1
            idx += 1
        else:
            return "No"
        
        if (len(goal) == idx):
            break
    
    return "Yes"