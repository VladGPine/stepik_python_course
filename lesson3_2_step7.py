# function f(x) already exist
a = {}

i = int(input())

while i != 0:
    b = int(input())
    if b not in a:
        a.setdefault(b, f(b))
        print(a[b])
    else:
        print(a.get(b))
    i -= 1
