words = ['champions', 'we', 'are', 'Stepik']
strings = ['We are the champignons', 'We Are The Champions', 'Stepic']

print(words, strings)

mid_result = [list(set(i.lower().split()).difference({j.lower() for j in words})) for i in strings]

print(*{j for i in mid_result for j in i}, sep='\n')
