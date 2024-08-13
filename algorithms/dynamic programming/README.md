# 다이나믹 프로그래밍이란?

반복되는 연산을 기억한 뒤 재사용해 처리 속도를 개선하는 알고리즘
메모이제이션이라고도 불림

# DP를 적용할 때 사용하는 두가지 방법

하향식(Top-down)과 상향식(Bottom-up) 방법

## 하향식이란?

재귀호출을 이용해 큰 문제를 작은 하위 문제로 해결하는 방법

## 상향식이란?

작은 하위문제들부터 시작해 결과를 저장하고, 이를 이용해 점진적으로 큰 문제의 해를 구하는 방법

# DP를 적용할 수 있는 조건

## 중복되는 부분 문제 (Overlapping Subproblems)

DP는 기본적으로 문제를 나누고 그 문제의 결과 값을 재활용해서 전체 답을 구한다.
그래서 동일한 작은 문제들이 반복하여 나타나는 경우에 사용 가능하다.

## 최적 부분 구조(Optimal Substructure)

부분 문제의 최적 결과 값을 사용해 전체 문제의 최적 결과를 낼 수 있는 경우 사용 가능하다.

## 알고리즘 문제 유형

- 구간 합
  - 1차원 누적합도 있지만 2차원으로 누적합을 구해야 하는 문제도 있음.
  - [구간 합 구하기](https://github.com/tjsry0466/algorithm-study/blob/main/BOJ/11660.py)
  - [퇴사 2](https://github.com/tjsry0466/algorithm-study/blob/main/BOJ/15486.py)
- 최장 증가 부분 수열
  - 전깃줄이 교차하지 않게 하는 문제는 대부분 최장 증가 부분 수열 접근법으로 해결 가능함
  - [전깃줄](https://github.com/tjsry0466/algorithm-study/blob/main/BOJ/2565.py)
- 배낭 문제
  - 크기를 가진 가방과 가치가 다른 물건들을 가방에 최대로 담아 최대 가치를 구하는 문제
  - [배낭 문제](https://github.com/tjsry0466/algorithm-study/blob/main/BOJ/9084.py)
  - [카드 구매하기](https://github.com/tjsry0466/algorithm-study/blob/main/BOJ/11052.py)
- 기타
  - VIP석을 기준으로 DP구간을 여러개로 쪼개서 경우의 수를 구하는 문제 ([극장 좌석](https://github.com/tjsry0466/algorithm-study/blob/main/BOJ/11660.py))
