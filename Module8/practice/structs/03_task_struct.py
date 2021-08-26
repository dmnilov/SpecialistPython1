# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random
numbers = []
n = 100
for _ in range (n):
    numbers.append(random.randint(-100, 100))
#считает все элементы количество которых больше 10шт
less_10 = [el for el in numbers if numbers.count(el) <= 10]
print(len(less_10))

less_10_v2 = [el for el in numbers if el <= 10]
print(len(less_10_v2))

sum_plus = [el for el in numbers if el > 0]
print(sum(sum_plus))

sr_arif = [el for el in numbers if el % 2 == 0]
mean_even = sum(sr_arif)/len(sr_arif)
print(mean_even)
