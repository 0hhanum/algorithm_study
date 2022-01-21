def pageCount(n, p):
    # Write your code here
    end_page = n // 2
    target = p // 2
    if target > end_page - target:
        return end_page - target
    else:
        return target
