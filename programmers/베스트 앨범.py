# https://school.programmers.co.kr/learn/courses/30/lessons/42579

# 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
# 노래는 고유 번호로 구분
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록

# 장르별로 재생 횟수를 사전에 담기
# 장르별로 두개씩.
# 재생된 순서가 많은 순서대로.
# 재생 횟수가 같다면 고유 번호(인덱스)가 낮은 노래

# 1. 사전에 장르별 재생시간의 합 담기
# 2. 제일 많이 담겨져있는 장르 알아내기.
# 3. 인덱스, genres랑 plays랑 같이 담고 plays를 내림차순으로 정렬해두기
# 4. 장르순으로 가장 먼저 등장하는 인덱스를 출력하기.
from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    dict = defaultdict(int)
    arr = []
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        arr.append((idx, genre, play))
        dict[genre] += play
        
    arr = sorted(arr, key = lambda x: (-x[2], x[0]))
    ordered_genres = sorted(dict.items(), key=lambda x: -x[1])
    for [key, _] in ordered_genres:
        count = 2
        for item in arr:
            if (item[1] == key and count > 0):
                answer.append(item[0])
                count -= 1
    
    return answer