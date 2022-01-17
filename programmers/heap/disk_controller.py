import heapq


def solution(jobs):
    answer = 0
    is_working = False
    waiting = []
    time = 0
    work_flow = 0
    length = len(jobs)

    while jobs or is_working:
        if work_flow == 0:
            is_working = False
        if not is_working and not waiting and jobs:
            job = jobs.pop(0)
            work_flow = job[1]
            is_working = True
            answer += work_flow
        elif not is_working and waiting:
            is_working = True
            work = heapq.heappop(waiting)
            print(work, "aaa")
            work_flow = work[0]
            answer += work_flow + work[1]
        elif is_working and jobs:
            if jobs[0][0] >= time:
                work = jobs.pop(0)[1]
                heapq.heappush(waiting, [work, 0])
        if waiting:
            for i, _ in enumerate(waiting):
                waiting[i][1] += 1
        time += 1
        work_flow -= 1
        print(waiting)
        print(work_flow)
    return int(answer / length)


print(solution([[0, 3], [1, 9], [2, 6]]))
