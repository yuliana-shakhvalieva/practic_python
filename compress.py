def compress(array):
    result, unique_elem = [], []

    for el in array:
        if el not in unique_elem:
            unique_elem.append(el)

    for el in unique_elem:
        result.append(el)
        count = array.count(el)
        if count != 1:
            result.append(count)
            
    return ''.join(map(str, result))