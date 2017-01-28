def my_sort(list_numbers):
    e_list = []
    o_list = []
    for x in list_numbers:
        if x % 2 == 0:
            e_list.append(x)
        else:
            o_list.append(x)
    o_list.sort()
    e_list.sort()
    return o_list + e_list
