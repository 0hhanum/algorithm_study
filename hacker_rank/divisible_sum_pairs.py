def divisibleSumPairs(n, k, ar):
    # Write your code here
    result = 0
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                result += 1
                print(ar[i], ar[j])
    return result


divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])
