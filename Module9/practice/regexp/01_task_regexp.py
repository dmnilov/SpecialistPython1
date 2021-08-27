# Дано произвольное предложение. Слова разделены пробелами. Предложение содержит знаки препинания.
# Найдите:
# 1) первое слово из строки
# 2) первые два символа каждого слова
# 3) все слова начинающиеся на гласную букву
# 4) все слова начинающиеся на согласную букву
# 5) все уникальные(без дубликатов) знаки препинания


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, Proin ut diam Varius, molestie sem Porta, rutrum dolor! Curabitur elementum suscipit?"

import re

template1 = r"^\w*"
template2 = r"\b\w{2}"
template3 = r"\b[A-Z]"
template4 = r"\b[BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxZz]"
template_5 = r"\W"

res1 = re.findall(template1, text)
res2 = re.findall(template2, text)
res3 = re.findall(template3, text)
res4 = re.findall(template4, text)
res5 = re.findall(template5, text)


print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
