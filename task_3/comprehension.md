+ [Task 1](#Task-1)
+ [Task 2](#Task-2)
+ [Task 3](#Task-3)
+ [Task 4](#Task-4)
+ [Task 5](#Task-5)
+ [Task 6](#Task-6)
+ [Task 7](#Task-7)
+ [Task 8](#Task-8)
+ [Task 9](#Task-9)
+ [Task 10](#Task-10)
+ [Task 11](#Task-11)
+ [Task 12](#Task-12)
+ [Task 13](#Task-13)
+ [Task 14](#Task-14)
+ [Task 15](#Task-15)
+ [Task 16](#Task-16)

## Task 1

Найти все числа от 1 до 1000, которые делятся на 17
```python
result = [digit for digit in range(1, 1001) if digit % 17 == 0]
```

## Task 2

Найти все числа от 1 до 1000, которые содержат в себе цифру 2
```python
result = [digit for digit in range(1, 1001) if '2' in str(digit)]
```

## Task 3

Найти все числа от 1 до 10000, которые являются палиндромом
```python
result = [digit for digit in range(1, 10001) if str(digit) == str(digit)[::-1]]

```

## Task 4

Посчитать количество пробелов в строке
```python
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"

result = string.count(' ')
result = len([sign for sign in string if sign == ' '])
```

## Task 5

Есть любая последовательность непробельных символов латинского алфавита, удалить все гласные из этого слова
```python
word = 'eyrtYuD'

result = ''.join([letter for letter in word if letter.lower() not in 'aeiouy'])
```

## Task 6

 На входе строка со словами, разделенными через 1 пробел. Найти все слова, длина которых не больше 5
```python
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"

result = [word for word in string.split() if len(word) <= 5]
```

## Task 7

На входе строка со словами, разделенными через 1 пробел. Получить словарь, где в качестве ключа используется само слово, а в значении длина этого слова.
```python
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"

result = {word: len(word) for word in string.split()}
```

## Task 8

На входе предложение со всеми пробельными и непробельными символами латинского алфавита. Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.
```python
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"

result = list(set([letter for letter in list(string) if letter in [chr(i) for i in range(97, 123)]]))
result = list(dict.fromkeys([letter for letter in list(string) if letter in [chr(i) for i in range(97, 123)]]).keys())
```

## Task 9

На входе список чисел, получить список квадратов этих чисел / use map
```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list(map(lambda x: x * x, digits))
```

## Task 10

На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2. 
На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0)
```python
points = [(1, 1), (1, 3), (5, 3)]

result = {point: (point[0] ** 2 + point[1] ** 2) ** (1/2) for point in points if point[1] == 5 * point[0] - 2}
```

## Task 11

Возвести в квадрат все четные числа от 2 до 27. На выходе список.
```python
result = [digit ** 2 for digit in range(2, 28, 2)]
```

## Task 12

На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат (0, 0) в первой четверти 
```python
points = [(1, 1), (1, 3), (5, 3)]

result = max([(point[0] ** 2 + point[1] ** 2) ** (1/2) for point in points if point[0] > 0 and point[1] > 0])
```

## Task 13

На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. Получить пары сумм и разниц, [(3, -1), (6, -2), ...]
```python
nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]

result = [(digit_first + digit_second, digit_first - digit_second) for digit_first, digit_second in zip(nums_first, nums_second)]
```

## Task 14

На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты этих чисел. Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты.
```python
digits_str = ['43141', '32441', '431', '4154', '43121']

result = [str(int(digit) ** 2) for digit in digits_str if (int(digit) ** 2) % 2 == 0]
```

## Task 15

Менеджер как обычно придумал свое представление данных, а нам оно не подходит. Мы хотим получить нормальную таблицу, чтобы импортировать в csv.

```python
input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""

result = [{row.split(',')[0]: row.split(',')[i] for row in input_str.split('\n')} for i in range(1, len(input_str.split('\n')[0].split(',')))]

```

## Task 16

Получить сумму по столбцам у двумерного списка
```python
a = [[11.9, 12.2, 12.9],
    [15.3, 15.1, 15.1],
    [16.3, 16.5, 16.5],
    [17.7, 17.5, 18.1]]
    
result = [sum([row[i] for row in a]) for i in range(len(a[0]))]
result = list(map(sum, zip(*a)))
```
