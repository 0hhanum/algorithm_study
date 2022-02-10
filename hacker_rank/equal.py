def equal(arr):
    # Write your code here
    counter = 0
    maximum = max(arr)
    minimum = min(arr)
    while maximum != minimum:
        difference = maximum - minimum
        tmp = maximum
        if difference >= 5:
            difference = 5
        elif difference >= 2:
            difference = 2
        else:
            difference = 1
        toggle = True

        for idx, i in enumerate(arr):
            if i == maximum and toggle:
                toggle = False
                continue
            else:
                arr[idx] += difference
                value = arr[idx]
                if value > tmp:
                    tmp = value
        counter += 1

        minimum += difference
        maximum = tmp
    return counter


##
def equal(arr):
    # Write your code here
    memo = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 1}
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr1[arr1.index(max(arr1))] -= 5
    arr2[arr1.index(max(arr1))] -= 2
    arr3[arr1.index(max(arr1))] -= 1

    m = min(arr)
    arr = list(map(lambda x: x - m, arr))
    m1 = min(arr1)
    arr1 = list(map(lambda x: x - m1, arr1))
    m2 = min(arr2)
    arr2 = list(map(lambda x: x - m2, arr2))
    m3 = min(arr3)
    arr3 = list(map(lambda x: x - m3, arr3))

    print(arr, arr1, arr2, arr3)
    result = [0, 1, 1, 1]

    def f(x):
        if x in memo:
            return memo[x]
        else:
            remainder = x % 5
            quotient = x // 5
            memo[x] = quotient + memo[remainder]
            return memo[x]

    for i in range(len(arr)):
        result[0] += f(arr[i])
        result[1] += f(arr1[i])
        result[2] += f(arr2[i])
        result[3] += f(arr3[i])
    print(result)
    return min(result)


equal([1, 5, 5, 10, 10])
