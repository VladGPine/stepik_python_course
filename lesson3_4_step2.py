with open('../dataset_3363_2.txt', 'r') as file_in, open('../dataset_out.txt', 'w') as file_out:
    str_in = file_in.readline().strip()

    alphas_list = []
    digits_list = []
    for element in str_in:
        next_element = str_in[str_in.index(element) + 1]
        if element.isalpha():
            if element == ' ':
                continue
            else:
                alphas_list.append(element)
                str_before_element = str_in[:str_in.index(element)]
                str_after_element = str_in[str_in.index(element) + 1:]
                str_in = f'{str_before_element} {str_after_element}'

    digits_list.extend(f'{str_before_element} {str_after_element}'.strip().split(' '))

    digits_list = [int(j) for j in digits_list]

    for i, elem in enumerate(alphas_list):
        alphas_list[i] = elem * digits_list[i]

    str_in = ''.join(alphas_list)
    file_out.write(f'{str_in}')

with open('../dataset_out.txt', 'r') as file_out:
    print(file_out.readline().strip())
