from itertools import permutations


def check_prime(x):
    if x == 1 or x == 0:
        return False
    if x == 2:
        return True

    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    str_numbers = [s for s in numbers]
    permutation_list = []
    answer = 0
    for i, _ in enumerate(numbers):
        i = i + 1
        permutation_list += list(permutations(str_numbers, i))

    table = {}
    for item in permutation_list:
        num = int("".join(item))
        if num not in table:
            table[num] = 0
            if check_prime(num):
                answer += 1
    return answer
