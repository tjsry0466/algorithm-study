# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    def dfs(x, v):
        nonlocal answer
        
        numPlus = v+numbers[x]
        numMinus = v-numbers[x]
        
        if (x == len(numbers)-1): 
            if (numPlus == target or numMinus == target):
                answer += 1
            return
    
        if (x+1 < len(numbers)):
            dfs(x+1, numPlus)
            dfs(x+1, numMinus)
    answer = 0   
    dfs(0, 0)
    
    return answer