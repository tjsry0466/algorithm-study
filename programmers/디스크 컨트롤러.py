# 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담을 2차원 배열 job가 주어짐
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 어떻게 되는지 작성
# 소수점 이하는 버린다.

# 아무일을 하고 있지 않는 시점에는 할일을 받고 가장 처리가 빨리되는 상품을 찾아서 처리한다.
# 최소힙 사용

import heapq


def solution(jobs):
    # 작업을 요청 시간 순으로 오름차순 정렬
    # 각 작업은 [요청 시간, 소요 시간] 형식으로 주어짐
    jobs.sort(key=lambda x: x[0])

    heap = []  # 힙을 사용하여 작업을 처리할 순서를 정할 리스트
    current_time = 0  # 현재 시간 (작업을 처리하면서 증가)
    total_wait_time = 0  # 총 대기 시간 (각 작업의 시작 시간 - 요청 시간 누적)
    job_index = 0  # jobs 리스트에서 현재 처리할 작업의 인덱스
    job_count = len(jobs)  # 작업의 총 개수

    # 작업이 남아 있거나 힙에 처리할 작업이 있을 동안 반복
    while job_index < job_count or heap:
        # 현재 시간까지 요청된 작업을 힙에 추가
        while job_index < job_count and jobs[job_index][0] <= current_time:
            # 힙에 작업을 넣을 때 소요 시간을 기준으로 정렬하기 위해 (소요 시간, 요청 시간) 형식으로 삽입
            heapq.heappush(heap, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1

        # 힙에 처리할 작업이 있을 경우
        if heap:
            # 소요 시간이 가장 짧은 작업을 힙에서 꺼내 처리
            duration, start = heapq.heappop(heap)
            current_time += duration  # 현재 시간을 작업 소요 시간만큼 증가
            # 대기 시간 = 작업이 끝난 시간 - 요청 시간
            total_wait_time += current_time - start

        else:
            # 힙이 비어 있고 처리할 작업이 남아 있는 경우
            # 다음 작업의 요청 시간이 현재 시간보다 이후일 경우, 현재 시간을 그 요청 시간으로 맞춤
            if job_index < job_count:
                current_time = jobs[job_index][0]

    # 총 대기 시간을 작업의 개수로 나눠서 평균 대기 시간을 반환
    return total_wait_time // job_count
