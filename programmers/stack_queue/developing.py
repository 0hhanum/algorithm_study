def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        tmp = 0
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            tmp += 1
            if len(progresses) == 0:
                break
        if tmp != 0:
            answer.append(tmp)
    return answer
