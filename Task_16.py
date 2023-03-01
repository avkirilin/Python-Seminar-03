# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
import random
lenght_list = 10        #int(input("Введите длину списка: "))
move_right_list = 5      #int(input("Введите на сколько элементов вправо необходимо сдвинуть наш список: "))
my_list = [random.randint(0, 10) for _ in range(lenght_list)]
print(my_list)
print(len(my_list))
new_list = []
for item in range(lenght_list):
    if item + move_right_list <= lenght_list:
        new_list[item] = my_list[move_right_list + item]
    else:
        new_list[item] = my_list[move_right_list + item - lenght_list]
print(new_list)


# for i in range(move_left_list):                                               #Решение с помощью цикла, где берется последний элемент списка и переносится в его начало
#     my_list.insert(0, my_list.pop(-1))                                        #Цикл повторяется столько раз, на сколько нам нужно сдвинуть список
# print(my_list)



# new_list = my_list[move_left_list:lenght_list] + my_list[0:move_left_list]    #Решение спомощью срезов. Разделили список на два и поменяли части местами
# print(new_list)