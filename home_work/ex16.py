import random as r

# VAR//1
# n = int(input('Enter the len of list: '))
# list_1 = [r.randint(-5, 5) for i in range(n)]
# num = int(input('Enter the num from -5 to 5: '))
#
# def duplicateNum():
#     count = 0
#     for i in range(n):
#         if list_1[i] == num:
#             count += 1
#     return count
#
# print(list_1)
# print(f'The count of {num} in the list = {duplicateNum()}')

# VAR//2
list_1 = list(map(int, input('Fill in the list: ').split()))
print([list_1.count(int(input(f'Enter a num from the {list_1}: ')))])




