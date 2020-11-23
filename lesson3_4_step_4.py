file_in_list = []

with open('../dataset_3363_4.txt', 'r') as file_in:
    for line in file_in:
        file_in_list.append(line.strip().split(';'))

print(file_in_list)
mid_list = [0, 0, 0]

for line in file_in_list:
    mid_list[0] += int(line[1])
    mid_list[1] += int(line[2])
    mid_list[2] += int(line[3])

mid_list = [i / len(file_in_list) for i in mid_list]

file_out_list = [str((int(i[1]) + int(i[2]) + int(i[3])) / 3) for i in file_in_list]
file_out_list.append(' '.join([str(i) for i in mid_list]))

with open('../dataset_out.txt', 'w') as file_out:
    [file_out.write(f'{i}\n') for i in file_out_list]




