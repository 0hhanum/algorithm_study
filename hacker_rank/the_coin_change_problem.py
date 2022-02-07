counter = 0


def getWays(n, c):
    global counter
    # Write your code here
    memo = []
    length = len(c)
    state = {coin: 0 for coin in c}

    def rec(n, state):
        global counter
        state = state.copy()
        if n == 0:
            if state not in memo:
                memo.append(state)
                counter += 1
            else:
                return
        elif n > 0:
            for coin in c:
                state[coin] += 1
                rec(n - coin, state)
        else:
            return

    rec(n, state)
    return len(memo)


def getWays(n, c):
    dp = [1] + [0] * n
    for i in c:
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
            print(dp)
            print(i, j)
    return dp[n]
