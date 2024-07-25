# https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=python3
# 모든 단어의 첫 문자가 대문자. 그 외의 알파벳은 소문자인 문자열
# 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됨.
# 문자열이 주어졌을 때 위 조건으로 바꾼 문자열 리턴

def solution(s):
	s = s.lower()
	answer = ""
	cursor = 0
	
	isNum = False
	isString = False
	

	for i in range(len(s)):
		if (s[i] == " "):
			answer += " "
			isNum = False
			isString = False
		elif (s[i].isnumeric()):
			isNum = True
			answer += s[i]
		else:
			if (isNum):
				answer += s[i]
			else:
				if (isString):
					answer += s[i]
				else:
					answer += s[i].upper()
					isString = True
	return answer
            
print(solution("3people unFollowed me"))