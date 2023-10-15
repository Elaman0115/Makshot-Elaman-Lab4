# "Task 1.1"
# a = input()
# a = list(a)
# print(a)
#

# "task 1.2"
# a = ['T','h','e','B','a','i','t','e','r','e','k']
# a = ''.join(a)
# print(a)

# task 1.3
# a = (1, 2, 3, 4, 5, 6, 7)
# b = (5, 6, 7, 9, 10, 1, 8, 8)
# a1 = len(b)//2
# b1 = len(b)//2
# con = a[:a1] + b[b1:]
# print(con)
# print('here', a[:a1], 'the first half of a')
# print('here', b[:b1], 'the second half of b')

# task 1.4
# input_tuple = ('55', '6', '777', 54, 6, 7777, 9, 777, 6)
# element_counts = {}
# for element in input_tuple:
#     if element in element_counts:
#         element_counts[element] += 1
#     else:
#         element_counts[element] = 1
# output_tuple = tuple((key, value) for key, value in element_counts.items())
# print("Elements and their occurrences:")
# print(output_tuple)

# task 1.5
# input_data = (55, 6, 777, 70.0, '7', 'A')
# tuple1 = (input_data[0], input_data[1], input_data[2])
# tuple2 = (input_data[3],)
# tuple3 = (input_data[4], input_data[5])
# print(tuple1)
# print(tuple2)
# print(tuple3)

# task 2.1
# a = input()
# while ' ' in a:
#     print("Ошибка!")
#     a = input()
# b = set(a)
# print(b)

# task 2.2
# s1 = {1, 2, 3, 4, 5}
# s2 = {2, 3, 5, 6, 4, 7}
# dif = s1 ^ s2
# print(dif)

# task 2.3
# set_1 = {1, 2, 3, 4, 5}
# set_2 = {5, 7, 8, 9, 2, 10}
# conclusion = set_1 - set_2
# print(conclusion)

# task 2.4
# set_A = {1, 2, 3, 4, 7}
# set_B = {8, 7, 9, 4, 2, 0, 10}
# set_C = {4, 0, 1}
# for element in set_A.copy():
#     if element in set_C:
#         set_A.remove(element)
#         set_B.add(element)
# set_C.update(set_A, set_B)
# print("Updated set_C =", set_C)
#
# # task 2.5
# A = {1, 2, 3, 4, 5, 6}
# n = 3
# m = 5
# list_of_sets = []
# for i in A:
#     for j in A:
#         for k in A:
#             if i != j and i != k and j != k:
#                 combination = {i, j, k}
#                 if combination not in list_of_sets:
#                     list_of_sets.append(combination)
#                 if len(list_of_sets) == m:
#                     break
#             if len(list_of_sets) == m:
#                 break
#         if len(list_of_sets) == m:
#             break
# print(list_of_sets)

# task 3.1
# cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]
# manufacturer_dict = {}
# for manufacturer, model in cars_list:
#     if manufacturer in manufacturer_dict:
#         manufacturer_dict[manufacturer].append(model)
#     else:
#         manufacturer_dict[manufacturer] = [model]
# for manufacturer, models in manufacturer_dict.items():
#     print(f'{manufacturer} {len(models)}')
#     for model in models:
#         print(f'- {model}')
#
