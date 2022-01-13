def countingValleys(steps, paths):
    # Write your code here
    height = 1 if paths[0] == "U" else -1
    direction = "up" if height == 1 else "down"
    result = 0
    for path in paths[1:]:
        if height == 0:
            if direction == "down" and path == "U":
                direction = "up"
                result += 1
            elif direction == "down" and path == "D":
                result += 1
            elif direction == "up" and path == "D":
                direction = "down"
        height += 1 if path == "U" else (-1)
    if height == 0 and direction == "down":
        result += 1

    return result
