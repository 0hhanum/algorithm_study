table = {}
location = set()


def check_changable(a, b):
    i = 0
    for idx, _ in enumerate(a):
        if a[idx] != b[idx]:
            i += 1
    if i == 1:
        return True
    else:
        return False


def find_location(begin, target, words, move):
    global table
    global location
    tmp_list = []
    for word in words:
        if check_changable(begin, word) and word != begin:
            tmp_list.append(word)
    for word in tmp_list:
        if word == target:
            location.add(move + 1)
            return
        if word not in table:
            table[word] = 0
            find_location(word, target, words, move + 1)


def solution(begin, target, words):
    answer = 0
    find_location(begin, target, words, 0)
    print(location)
    if location:
        return min(location)
    else:
        return answer
