a = [int(i) for i in input().split()]
a.sort()
b = []

for i, el in enumerate(a):
    if i < len(a) - 1 and el == a[i + 1] and el not in b:
        b.append(el)
print(*b, end=' ')
