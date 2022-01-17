import heapq


def solution(jobs):
    waiting = []  # 대기 Heap => [소요시간, 대기시간] 형태로 들어감
    num_of_jobs = len(jobs)
    answer = 0
    time = 0  # 현재 시점
    heapq.heapify(jobs)  # 정렬

    while jobs or waiting:  # jobs, waiting 둘 다 비면 종료.
        job = 0
        if not waiting:  # Heap 비어있으면 바로 jobs 에서 꺼내서 실행.
            starting_point, job = heapq.heappop(jobs)
            answer += job
            time = starting_point + job  # 시점이동

        else:
            job, time_for_wait = heapq.heappop(waiting)  # 힙에서 최소값 꺼내기
            answer += job + time_for_wait  # 대기시간 + 소요시간
            time += job  # 시점 업데이트

        for idx, _ in enumerate(waiting):  # 대기 힙에 있는 작업들 대기시간 업데이트
            waiting[idx][1] += job

        # 대기 들어가야 할 것들 처리
        while jobs and jobs[0][0] < time:
            starting_point, job = heapq.heappop(jobs)
            heapq.heappush(waiting, [job, time - starting_point])  # 소요시간, 대기시간
    return int(answer / num_of_jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))
