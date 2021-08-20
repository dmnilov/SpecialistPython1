# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
summ = 0
numbers = []
n = 15
for i in range(n):
    numbers.append(random.randint(-100, 100))
for k in numbers:
    if k > 0 and k%2 == 0:
        summ += k

print(summ)

