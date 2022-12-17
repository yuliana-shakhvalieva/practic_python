# title Count sum of diagonals in matrix

# description Суммирование элементов на главной и побочной диагоналях квадратной матрицы

# ---end---

def diagonalSum(mat):
    result = 0
    for i in range(len(mat)):
        if mat[i][i] == mat[i][len(mat) - i - 1]:
            result += mat[i][i]
        else:
            result += mat[i][i] + mat[i][len(mat) - i - 1]

    return result