# Задача 3. Таблица стоимости
# Одна единица некоторого товара стоит x рублей. Напечатайте таблицу стоимости 2, 3, ..., 20 единиц этого товара.
# Формат входных данных
# Вводится одно положительное вещественное число x, которое не превосходит 105 и задано с двумя знаками после запятой.

# пример:
# Входные данные
# 9.99

price = float(input("стоимость товара: "))

a = 1

while a <= 20:

    print("#", a, round(price * a, 2), "Rub")

    a += 1
#все равно не могу понять как тут заставить его правильно отображать количество знаков после запятой. простой метод price*a выдает периодически такие длинные результаты 
#(к примеру при цене 1.11
#в этом варианте тоже не все замечательно, если вторым знаком будет ноль, то он все равно сократит.
