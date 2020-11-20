s = ''

with open('../dataset_3363_3.txt', 'r') as file_in:
    for el in file_in:
        s += el.strip()

s = s.lower().split()
b = set(s)
a = {}

for element in b:
    a.setdefault(element, s.count(element))

max_key = max([k for k, v in a.items() if v == max([i for i in a.values()])])
max_value = max([i for i in a.values()])

print(max_key, max_value)
