# data_in = {1: {'Спартак': 9,
#                'Зенит': 10},
#            2: {'Локомотив': 12,
#                'Зенит': 3},
#            3: {'Спартак': 8,
#                'Локомотив': 15}}

data_in = {}
input_list = []
for i in range(int(input())):
    input_list.append(input().strip().split(';'))
    data_in.setdefault(i, {})
for i, m in data_in.items():
    for inner_list in input_list:
        if i == input_list.index(inner_list):
            for j, k in enumerate(inner_list):
                if j % 2 == 0:
                    m[k] = int(inner_list[j + 1])

# print(input_list)
# print(data_in)
data_out = {}

for teams in data_in.values():
    for team in teams:
        data_out.setdefault(team, [0, 0, 0, 0, 0])

for teams in data_in.values():
    for team, goals in teams.items():
        if team in teams:
            data_out[team][0] += 1
        if len(set(int(i) for i in teams.values())) == 1:
            data_out[team][2] += 1
        else:
            if int(goals) == max(teams.values()):
                data_out[team][1] += 1
            else:
                data_out[team][3] += 1
        data_out[team][-1] = data_out[team][1] * 3 + data_out[team][2]

for k, v in data_out.items():
    print(f'{k}:', *v)
