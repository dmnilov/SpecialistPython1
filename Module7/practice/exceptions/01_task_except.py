# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.
while True:
    try:
        S = input("введите размер прямоугольника формата AxB: ")
        line = S.split("x")
        n = int(line[0])
        m = int(line[1])
        break
    except ValueError:
        print("некорректные данные")
num_of_sqare = n//m
print(int(num_of_sqare))
