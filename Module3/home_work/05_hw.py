# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
max_len = " "

for i in names:
    if len(max_len) < len(i):
        max_len = i

print(max_len)
