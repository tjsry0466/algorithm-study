# https://www.acmicpc.net/problem/1620

# 가지고 있는 도감에서 포켓몬의 이름을 보면 포켓몬의 번호를 말하기
# 혹은 포켓몬 번호를 보면 포켓몬의 이름을 말하기

# 입력
# 첫째줄에는 도감에 수록되어 있는 포켓몬의 개수 N, 내가 맞춰야 하는 문제의 개수 M
# N과 M은 1보다 크거나 갈고 10만보다 작거나 같은 자연수
# 둘째 줄부터 N개의 포켓몬의 번호.
# 문제가 알파벳으로만 들어오면 포켓몬 번호 출력
# 숫자로만 들어오면 포켓번 번호에 해당하는 문자 출력

# 예제 입력
# 26 5 // 내가 맞춰야 하는 문제 개수 5개
# Bulbasaur
# Ivysaur
# Venusaur
# Charmander
# Charmeleon
# Charizard
# Squirtle
# Wartortle
# Blastoise
# Caterpie
# Metapod
# Butterfree
# Weedle
# Kakuna
# Beedrill
# Pidgey
# Pidgeotto
# Pidgeot
# Rattata
# Raticate
# Spearow
# Fearow
# Ekans
# Arbok
# Pikachu
# Raichu // 여기까지가 포켓몬
# 25
# Raichu
# 3
# Pidgey
# Kakuna

# 예제 출력
# Pikachu // 25번째는 피카츄
# 26 // Raichu는 26번째
# Venusaur // 3번째는 Venusaur
# 16 // pidgey는 16번째
# 14 // Kakuna는 14번째

N, M = map(int, input().split())

pokemons = [input() for _ in range(N)]
questions = [input() for _ in range(M)]

numberToString = dict()
stringToNumber = dict()

for index, pokemon in enumerate(pokemons):
    numberToString[index + 1] = pokemon
    stringToNumber[pokemon] = index + 1

# print(numberToString)
# print(stringToNumber)

for question in questions:
    if question.isnumeric():
        print(numberToString.get(int(question)))
    else:
        print(stringToNumber.get(question))
