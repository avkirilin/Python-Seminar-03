# Дан список чисел. Определите, сколько в нем встречается различных чисел.
import random
my_list = [random.randint(0,10) for _ in range(20)]
# print(my_list)
# new_list = []
# for item in my_list:
#     if item not in new_list:
#         new_list.append(item)
# print(new_list)
# print(len(new_list))
print(my_list)
print(len(set(my_list)))