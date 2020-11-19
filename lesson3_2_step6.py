def dict_counting(str_arg):
    l = str_arg.lower().split()
    print(l)
    d = {}
    for i in l:
        d.setdefault(i, l.count(i))
    for i in d:
        print(i, d[i])

a = 'a aa abC aa ac abc bcd a'
dict_counting(a)