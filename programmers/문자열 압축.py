# https://school.programmers.co.kr/learn/courses/30/lessons/60057

answer = 999999999
def recr(s, x):
    global answer
    
    if (len(s) == 1):
        answer = 1
        return
    
    if (len(s) // 2 < x):
        return
    
    word_length = 0
    previousWord = s[:x]
    count = 1
    
    for i in range(x, len(s), x):
        
        current = s[i:i+x]
        if (previousWord == current):
            count+=1
        else:
            if (count > 1):
                word_length += len(str(count)+previousWord)
                
                if (word_length > answer):
                    break
            else:
                word_length += len(previousWord)
                
            previousWord = current
            count = 1
    if (count != 1):
        word_length += len(str(count) + previousWord)
    else:
        word_length += len(previousWord)
    
    answer = min(word_length, answer)
    
    recr(s, x+1)
    
def solution(s):
    recr(s, 1)
    return answer
# print(solution('aabbaccc'))                 # 7
print(solution('a'))                 # 1
# print(solution('ababcdcdababcdcd'))         # 9
# print(solution('abcabcdede'))               # 8
# print(solution('abcabcabcabcdededededede')) # 14
# print(solution('xababcdcdababcdcd'))        # 17
# print(solution('aaaaaaaaaa'))        # 5
# print(solution('abcabcab'))        # 6