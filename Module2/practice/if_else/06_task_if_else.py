if year%400 == 0:
    print("366 days")
elif year%4 == 0 and year%100 != 0:
    print("366 days")
else:
    print("365 days")
