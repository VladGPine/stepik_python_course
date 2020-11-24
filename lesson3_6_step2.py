import requests
url = ''
with open('../dataset_3378_2.txt', 'r') as file_in:
	url = file_in.read().strip()

res = requests.get(url).text.splitlines()
print(len(res))
