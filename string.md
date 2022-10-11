+ [Compress list of strings](#compress-list-of-strings)

## Compress list of strings

Сжатие исходного массива следующим образом: ["a", "b", "b", "c", "c", "c"] --> "ab2c3"
```python
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
```