cow = int(input("число для подсчета коров: "))
if cow%10 == 1:
    text_2 = "корова"
elif cow%10 <= 5 and cow%10 != 0:
    text_2 = "коровы"
else:
    text_2 = "коров"
print("На лугу пасется", cow, text_2)
