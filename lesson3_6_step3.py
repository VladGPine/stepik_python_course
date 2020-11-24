import requests
a = []
with open('../dataset_3378_3.txt', 'r') as line_in:
	line = line_in.read().strip()
	res = requests.get(line)
	a.append(res.text)

for i in a:
	if not a[-1].startswith('We'):
		a.append(requests.get(f'https://stepic.org/media/attachments/course67/3.6.3/{i}').text)
		print(i)

print(a[-1])
