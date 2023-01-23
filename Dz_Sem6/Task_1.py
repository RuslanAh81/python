
"""Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
 стоящих на позиции с нечетным индексом.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12"""

# s = 0
# a = [2, -30, 5, 9, 3]
# for i in range(len(a)):
#     if i % 2 != 0:
#         s += a[i]
#         print(a[i])
# print(f"Сумма равна: {s}")

my_list = [2, 3, 5, 9, 3]
new_lst = [num for i, num in enumerate(my_list) if i % 2]
print(sum(new_lst))