steps = []

for i in range(int(input())):
    coords = {}
    coord_list = input().split()
    coords.setdefault(coord_list[0], int(coord_list[1]))
    steps.append(coords)

print(steps)


def final_coordinates(route: list):
    x, y = 0, 0
    for i in route:
        for k, v in i.items():
            if k == 'север':
                y += v
            elif k == 'юг':
                y -= v
            elif k == 'запад':
                x -= v
            elif k == 'восток':
                x += v
    print(x, y)


final_coordinates(steps)
