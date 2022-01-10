def gradingStudents(grades):
    # Write your code here
    result = []
    for i in grades:
        if i < 38:
            result.append(i)
        else:
            mod = i % 5
            if mod > 2:
                result.append(i + (5 - mod))
            else:
                result.append(i)
    return result
