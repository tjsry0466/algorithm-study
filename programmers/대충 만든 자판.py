# https://school.programmers.co.kr/learn/courses/30/lessons/160586#

# 하나의 키에 여러개의 문자가 할당될 수 있음.
# 여러 문자가 할당된 경우 동일한 키를 연속해서 빠르게 누르면 할당된 순서대로 문자가 바뀜
# 최소 몇번을 클릭해야 입력할 수 있는지 계산하는 문제

# 멋대로 키가 할당되어 있음
# 키의 개수가 최대 100개
# 같은 문자가 자판 전체에 여러번 할당
# 같은 키에도 여러번 할당
# 아예 할당되지 않은 경우도 존재

def solution(keymap, targets):
    # 키에 할당된 최소 클릭 수를 저장하는 딕셔너리
    min_clicks = {}

    # keymap에서 각 문자에 대해 최소 클릭 수를 저장
    for keys in keymap:
        for index, char in enumerate(keys):
            if char in min_clicks:
                min_clicks[char] = min(min_clicks[char], index + 1)
            else:
                min_clicks[char] = index + 1

    # 각 target 문자열에 대해 클릭 수 계산
    answer = []
    for target in targets:
        total_clicks = 0
        for char in target:
            if char in min_clicks:
                total_clicks += min_clicks[char]
            else:
                total_clicks = -1
                break
        answer.append(total_clicks)

    return answer
