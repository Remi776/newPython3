import random as r

n = int(input('Enter the len of list: '))

my_list = [r.randint(-10, 10) for i in range(n)]
x_num = int(input('Enter the number from -10 to 10: '))

def find_the_nearest_value(list, item):
    empty_list = []
    for i in range(len(list)):
        empty_list.append(abs(item - list[i]))
    return list[empty_list.index(min(empty_list))]

print(f'list = {my_list}')
print(f'Number = {x_num}')
print(f'Nearest value to {x_num} = {find_the_nearest_value(my_list, x_num)}')



