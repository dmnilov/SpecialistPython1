n = int(input("число для подсчета первой стороны шоколадки: "))
m = int(input("число для подсчета второй стороны шоколадки: "))
k= int(input("число долек: "))

if n*m%k == 0 and n*m != k:
    print("yes")
else:
    print("no")
