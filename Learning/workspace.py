def descending_order(num):
    num_str = str(num)
    num_list = []
    for char in num_str:
        num_list.append(char)
    num_list.sort(reverse=True)
    str_num = ''
    for element in num_list:
        str_num += element
    return int(str_num)
