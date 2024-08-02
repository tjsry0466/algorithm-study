# https://school.programmers.co.kr/learn/courses/30/lessons/42747#

# H-Index는 과학자의 생산성과 영향력을 나타내는 지표
# 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index

# 제한사항
# 과학자가 발표한 논문의 수는 1편 이상 1000편 이하
# 논문별 인용 횟수는 0회 이상 10000회 이하

def solution(citations):
    citations.sort()
    max_length = len(citations)
    
    answer = 0
    for i in range(max_length):
        if (citations[i] >= len(citations)- i):
            answer = max(answer, len(citations)- i)
    
    return answer