# https://school.programmers.co.kr/learn/courses/30/lessons/172927#

# 다이아몬드/철/돌 곡괭이로 광물을 캘때 소모되는 피로도가 정해져 있다.
# 각곡괭이는 최대 5번만 광물을 캘 수 있다.
# 다음과 같은 규칙을 지키면서 최소한의 피로도로 광물을 캐려고 한다.
# - 사용할 수 있는 곡괭이중 아무거나 하나를 선택
# - 한 번 사용하기 시작한 곡괭이는 사용할 수 없을 때까지 사용
# - 광물은 주어진 순서대로만 캘 수 있음
# - 광산에 있는 모든 광물을 캐거나, 더 사용할 곡괭이가 없을 때까지 캠

# 곡괭이의 개수 picks [dia, iron, stone]
# 광물 목록 minerals [diamond, iron, stone]

# 한번 선택한 곡괭이는 5번을 무조건 사용해야한다.
# 5개씩 보고 최적의 곡괭이를 선택해야한다.
# 각 곡괭이를 선택했을때 소모되는 피로도를 미리 구할 수 있다.
# 곡괭이의 총 개수 * 5개까지만 고려하면 된다 (미리 잘라도 괜찮음)

# 5개씩 그룹화했을때 다이아몬드 수가 많은 순, 철이 많은 순, 나머지로 좋은 곡괭이를 쓰면 된다.
# 순서가 정해지면 순서대로 다이아,철,돌 곡괭이를 적용했을때의 피로도를 구하면 된다.

# 1. 5개씩 그룹화한다.
# 2. 그룹별로 다이아,철,돌의 개수를 구한다.
# 3. 정렬한다.
# 4. 정렬된 순서에서 남아있는 곡괭이중 다이아/철/돌 순서대로 적용했을때의 피로도를 구한다.

# 최적화 하는 방법
# picks는 다이아, 철, 돌 순서대로 정렬되어 있다.

# 그룹에 다이아, 철, 돌의 개수와 곡괭이가 주어졌을 때 총 얼만큼 피로도가 드는지 구하는 함수를 만든다.
# 총 피로도를 구한다.


# 내가 짠 코드
def solution(picks, minerals):
    group_count = (len(minerals) // 5) + 1
    minerals = minerals[: sum(picks) * 5]
    groups = [[] for _ in range(group_count)]

    for i in range(group_count):
        base = 5 * i
        diamond = 0
        iron = 0
        stone = 0
        for j in range(5):
            if base + j < len(minerals):
                if minerals[base + j] == "diamond":
                    diamond += 1
                elif minerals[base + j] == "iron":
                    iron += 1
                elif minerals[base + j] == "stone":
                    stone += 1
        groups[i] = [diamond, iron, stone]

    groups.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    answer = 0
    diamond = picks[0]
    iron = picks[1]
    stone = picks[2]
    for group in groups:
        if diamond > 0:
            answer += sum(group)
            diamond -= 1
        elif iron > 0:
            answer += group[0] * 5
            answer += group[1] * 1
            answer += group[2] * 1
            iron -= 1
        elif stone > 0:
            answer += group[0] * 25
            answer += group[1] * 5
            answer += group[2] * 1
            stone -= 1

    return answer


# 지피티가 짠 코드
def solution(picks, minerals):
    def calculate_fatigue(group, pick_type):
        if pick_type == "diamond":
            return sum(group)
        elif pick_type == "iron":
            return group[0] * 5 + group[1] * 1 + group[2] * 1
        elif pick_type == "stone":
            return group[0] * 25 + group[1] * 5 + group[2] * 1

    # 1. minerals를 5개씩 그룹화
    max_minerals = sum(picks) * 5
    minerals = minerals[:max_minerals]
    groups = []

    for i in range(0, len(minerals), 5):
        group = minerals[i : i + 5]
        diamond = group.count("diamond")
        iron = group.count("iron")
        stone = group.count("stone")
        groups.append([diamond, iron, stone])

    # 2. 그룹별로 다이아, 철, 돌의 개수를 기준으로 정렬
    groups.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    # 3. 정렬된 그룹에 대해 다이아, 철, 돌 순서로 피로도 계산
    answer = 0
    pick_types = ["diamond", "iron", "stone"]
    for group in groups:
        for pick_type, count in zip(pick_types, picks):
            if count > 0:
                answer += calculate_fatigue(group, pick_type)
                picks[pick_types.index(pick_type)] -= 1
                break

    return answer


# 코드를 짠 후에 최적화 할 수 있는 방법을 고민하는 시간을 가져야겠다.
