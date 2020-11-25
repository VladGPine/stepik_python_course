data_in = []
for i in range(4):
	data_in.append(input())

str_out_crypt = ''.join([data_in[1][data_in[0].index(i)] for i in data_in[2] if i in data_in[0]])
str_out_decrypt = ''.join([data_in[0][data_in[1].index(i)] for i in data_in[3] if i in data_in[1]])

print(str_out_crypt)
print(str_out_decrypt)