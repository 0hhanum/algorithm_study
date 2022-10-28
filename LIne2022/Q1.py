from typing import List
import math

def solution(queries: List[List[int]]) -> int:
    answer = 0
    arrays = {}
    for target, add_num in queries:
        if arrays.get(target):
            array_len, array_num = arrays[target]
            added_num = array_num + add_num
            if array_len < array_num + add_num:
                nearest = 2 ** math.ceil(math.log2(added_num))
                arrays[target] = nearest, added_num
                answer += array_num
            else:
                arrays[target][1] = added_num
        else:
            nearest = 2 ** math.ceil(math.log2(add_num))
            arrays[target] = [nearest, add_num]
    return answer