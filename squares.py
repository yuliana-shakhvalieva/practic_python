def merge(first, second):
    result = []
    count_el = len(first) + len(second)
    for i in range(count_el):
        if first != [] and second != []:
            if first[0] <= second[0]:
                result.append(first.pop(0))
            else:
                result.append(second.pop(0))
        elif not first:
            result.append(second.pop(0))
        elif not second:
            result.append(first.pop(0))
    return result


def squares(s):
    n = len(s)
    if s[0] >= 0 and s[n-1] >= 0:
        return [el**2 for el in s]
    elif s[0] <= 0 and s[n-1] <= 0:
        return [s[i]**2 for i in range(n-1, -1, -1)]
    else:
        i = 0
        while s[i] <= 0:
            i += 1
        pivot = i
        left = s[:pivot]
        right = s[pivot:]
        left_square = [left[i]**2 for i in range(pivot-1, -1, -1)]
        right_square = [right[i]**2 for i in range(n-pivot)]
        return merge(left_square, right_square)