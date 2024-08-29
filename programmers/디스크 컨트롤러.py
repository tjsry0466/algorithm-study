# 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담을 2차원 배열 job가 주어짐
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 어떻게 되는지 작성
# 소수점 이하는 버린다.

# 아무일을 하고 있지 않는 시점에는 할일을 받고 가장 처리가 빨리되는 상품을 찾아서 처리한다.
# 최소힙 사용

import heapq


def solution(jobs):
    # 작업을 요청 시간 순으로 정렬
    jobs.sort(key=lambda x: x[0])

    heap = []
    current_time = 0
    total_wait_time = 0
    job_index = 0
    job_count = len(jobs)

    while job_index < job_count or heap:
        while job_index < job_count and jobs[job_index][0] <= current_time:
            heapq.heappush(heap, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1

        if heap:
            duration, start = heapq.heappop(heap)
            current_time += duration
            total_wait_time += current_time - start
        else:
            if job_index < job_count:
                current_time = jobs[job_index][0]

    return total_wait_time // job_count
