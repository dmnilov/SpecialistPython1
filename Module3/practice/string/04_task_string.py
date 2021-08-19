# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

# TODO: your code here
text = "И темен город. Мороз узором дорог не мети lf."

new_text = text.lower().replace(" ", "").replace(".", "")
rew_text = new_text[::-1]
if new_text == rew_text:
    print("yes")
else:
    print("no")
