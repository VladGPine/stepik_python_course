"""
Вычислить среднее арифметическое чисел в диапазоне [a, b],
если эти числа кратны 3
"""

a, b = (int(i) for i in input().split())
c = [i for i in range(a, b + 1) if i % 3 == 0]
print(sum(c) / len(c))
