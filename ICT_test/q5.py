def countCompanies(friends_nodes, friends_from, friends_to, friends_weight):
    # Write your code here
    table = {i + 1: [] for i in range(friends_nodes)}
    # print(friends_nodes, friends_from, friends_to, friends_weight)
    for i in range(len(friends_from)):
        company = friends_weight[i]
        fr, to = friends_from[i], friends_to[i]

    maximum = 0
    for i in map(lambda x: len(table[x]), table):
        if i > maximum:
            maximum = i
    maxValue = 0
    for i in (key for key, value in table.items() if len(table[key]) == maximum):
        print(i)
        group = table[i]
        print(group)
        m1 = max(group)
        group.remove(m1)
        m2 = max(group)
        if m1 * m2 > maxValue:
            maxValue = m1 * m2
    return maxValue
