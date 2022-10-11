+ [Count sum of diagonals in matrix](#count-sum-of-diagonals-in-matrix)

## Count sum of diagonals in matrix

Суммирование элементов на главной и побочной диагоналях квадратной матрицы
```python
def diagonalSum(mat):
    result = 0
    for i in range(len(mat)):
        if mat[i][i] == mat[i][len(mat) - i - 1]:
            result += mat[i][i]
        else:
            result += mat[i][i] + mat[i][len(mat) - i - 1]

    return result
```