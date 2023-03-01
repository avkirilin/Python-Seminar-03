# Задан рандомный список чисел из N элементов. Создайте новый
# список где исключены повторяющиеся элементы первого списка

import random
lenght_list = int(input("Введите длину списка: "))
my_list = [random.randint(0,10) for _ in range(lenght_list)]
print(my_list)
# new_list = []                                                   # решение простым перебором. сравнение каждого значения с 
# for i in range(lenght_list):                                    # последующими. И если есть одинаковые, то их пропускаем,
#     count = 0                                                   # если нет - то добавляем в новый список
#     for j in range(lenght_list):
#         if my_list[i] == my_list[j]:
#             count += 1
#     if count < 2:
#         new_list.append(my_list[i])
# print(new_list)


my_dict = {}                                                  # Решение через словари. Сначала создаем пустой словарь
for item in my_list:                                          # Далее делаем цикл for, который проходится по значениям
    my_dict[item] = my_dict.get(item, 0) + 1                  # списка и показываем сколько раз каждое уникальное значение
print (my_dict)                                               # встречалось в этом списке. Далее создаем пустой список
new_list = []                                                 # делаем новый цикл for, который проходится по ключам (key) и
for key, value in my_dict.items():                            # их значениям (value) словаря my_dict. Проверяется условие 
    if value == 1:                                            # если ключ встречается в списке только один раз, то добавляем
        new_list.append(key)                                  # его в новый список. Метод items() перебирает и ключи и значения
print(new_list)                                               # одновременно

# new_list = []                                                   # Решение спомощью встроенного метода count языка python. Идет
# for item in my_list:                                            # подсчет одинаковых элементов списка. На добавление в новый
#     if my_list.count(item) == 1:                                # список идут только те значения, которые встречаются только один
#         new_list.append(item)                                   # раз и затем выводим на печать
# print(new_list)