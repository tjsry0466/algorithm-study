# https://www.acmicpc.net/problem/31416

# 숙련 연구원은 A, B 둘다 검증 가능
# 신입 연구원은 차량 A만 가능
# 한번에 하나의 가상 검증만 수행 가능

# 첫번째줄에는 테스트 케이스 수 Q
# 두번쨰줄에는
# 차종 A, B의 가상 검증 시물레이션을 1회 수행하는데 걸리는 시간 tA, tB
# 가상 검증 시물레이션을 수행해야 하는 항목의 수 vA, vB
# tA, tB, vA, vB는 최대 100

# 각 케이스별로 검증 업무를 완료하는 데 걸리는 시간의 최솟값을 구하는 문제

# 접근 방법

# A의 검증 항목을 0개부터 V_A개까지 처리했을 때의 결과를 직접 계산해보면서
# 그중 최대값이 작업 시간
# 작업시간이 최소가 되는 답을 구함


def minimum_time_for_simulation(Q, test_cases):
    results = []

    for case in test_cases:
        T_A, T_B, V_A, V_B = case

        # 최소 시간을 무한대 값으로 설정
        min_time = float("inf")

        # 신입 연구원은 A의 검증 항목을 0개부터 V_A개까지 처리할 수 있으므로, 이 경우들을 모두 시뮬레이션
        for x in range(V_A + 1):
            # 신입 연구원은 x개의 A 검증을 하고, 숙련 연구원은 나머지 A와 B를 처리
            time_old = (V_A - x) * T_A + V_B * T_B
            time_new = x * T_A

            # 두 시간 중 큰 값이 전체 완료 시간
            max_time = max(time_old, time_new)

            # 최소 시간을 갱신
            min_time = min(min_time, max_time)

        results.append(min_time)

    return results


# 입력 예시
Q = int(input())
test_cases = [list(map(int, input().split())) for _ in range(Q)]

# 결과 출력
results = minimum_time_for_simulation(Q, test_cases)
for result in results:
    print(result)
