with open('../dataset_3380_5.txt', 'r') as data_in, open('../dataset_3380_5_output.txt', 'w') as data_out:
    a = {}
    output_dict = {}
    for line in data_in:
        student_list_data = line.strip().split('\t')
        class_number = int(student_list_data[0])
        last_name = student_list_data[1]
        height = int(student_list_data[2])
        a.setdefault(class_number, {})
        a[class_number][last_name] = height
        output_dict.setdefault(class_number, 0)

    absolute_set = {i for i in range(1, 12)}

    for k, v in a.items():
        for v_dict in v.values():
            output_dict[k] += v_dict / len(v)

    for i in absolute_set:
        if i not in output_dict.keys():
            output_dict[i] = '-'
        data_out.write(f'{i} {output_dict[i]}\n')
    data_out.close()
