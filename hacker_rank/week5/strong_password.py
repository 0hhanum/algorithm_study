def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    result = [0, 1, 2, 3]
    for i in password:
        for j in result:
            tmp = False
            if j == 0:
                tmp = i.isnumeric()
            elif j == 1:
                tmp = i.islower()
            elif j == 2:
                tmp = i.isupper()
            else:
                tmp = not (i.isnumeric() or i.islower() or i.isupper())
            if tmp:
                result.remove(j)
                break

    result = len(result)
    if n + result < 6:
        result += 6 - (n + result)
    return result
