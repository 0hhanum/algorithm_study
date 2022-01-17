answer = []


##### for 문으로 recursion 돌릴때 변수 주의해야함!!!!!!!!

def solution(tickets):
    global answer

    def find_route(ts, current, route):
        global answer
        if not ts:
            answer += [route]
            return
        available = list(filter(lambda x: x[0] == current, ts))
        if not available:  # 갈 수 있는 곳이 없으면 종료.
            return
        for ticket in available:
            tmp = ts.copy()
            rt = route.copy()
            tmp.remove(ticket)
            rt.append(ticket[1])
            find_route(tmp, ticket[1], rt)

    find_route(tickets, "ICN", [])

    result = min(answer)

    result.insert(0, "ICN")
    return result


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
