def bigSorting(unsorted):
    # Write your code here
    result = [unsorted[0]]
    for i in unsorted[1:]:
        tmp = int(i)
        toggle = True
        for j in range(len(result)):

            if int(result[j]) >= tmp:
                result.insert(j, i)
                toggle = False
                break
        if toggle:
            result.append(i)
    return result


bigSorting([
    31415926535897932384626433832795,
    1,
    3,
    10,
    3,
    5,
])
a = [1, 2, 3]
a.insert(1, 1)
import bisect

print(bisect.bisect_left(a, 1))
print(a)
