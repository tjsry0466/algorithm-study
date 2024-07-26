# https://school.programmers.co.kr/learn/courses/30/lessons/42577#qna
# 한 번호가 다른 번호의 접두어인 경우가 있는지 확인
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false, 그렇지 않으면 true 리턴

def solution(phone_book):
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
            prev = phone_book[i]
            next = phone_book[i+1]
            if (next.startswith(prev)):
                return False
    
    return True