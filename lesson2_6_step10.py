"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся
строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов
первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится
с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
"""
stopper = 'end'
a = []  # [[2, 2], [3, 5], [-1, 7], [0, 1], 'end']  # [[9, 5, 3], [0, 7, -1], [-5, 2, 9], 'end']
b = []

while len(a) >= 0:
    user_input = [i for i in input().split()]
    a.append(user_input)
    for el in a:
        for j in range(len(el)):
            if stopper not in el:
                el[j] = int(el[j])
    if stopper in user_input:
        a[-1] = stopper
        break


a = a[:-1]
c = []

for i in range(len(a)):
    for j in range(len(a[i])):
        if len(a) == 1:
            res = 0
            if len(a[i]) == 1:
                res = int(a[i][j] + a[i][j] + a[i][j] + a[i][j])
            elif len(a[i]) > 1:
                if j == len(a[i]) - 1:
                    res = int(a[i][j] + a[i][j] + a[i][j - 1] + a[i][0])
                else:
                    res = int(a[i][j] + a[i][j] + a[i][j - 1] + a[i][j + 1])
            c.append(res)
        else:
            if len(a[i]) == 1:
                if i == len(a) - 1:
                    res = int(a[i - 1][0] + a[0][0] + a[i][0] + a[i][0])
                else:
                    res = int(a[i - 1][0] + a[i + 1][0] + a[i][0] + a[i][0])
                c.append(res)
            else:
                if i == len(a) - 1:
                    if j == len(a[i]) - 1:
                        res = int(a[i - 1][j] + a[0][j] + a[i][j - 1] + a[i][0])
                    else:
                        res = int(a[i - 1][j] + a[0][j] + a[i][j - 1] + a[i][j + 1])
                else:
                    if j == len(a[i]) - 1:
                        res = int(a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][0])
                    else:
                        res = int(a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][j + 1])
                c.append(res)
    b.append(c)
    c = []
for i in range(len(b)):
    if i == len(b) - 1:
        print(*b[i], end='')
    else:
        print(*b[i])
