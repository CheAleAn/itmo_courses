#print("введите номер месяца")
a = int(input())
if a == 1 or a == 2 or a == 12:
    print("winter")
elif a > 2 and a < 6:
    print("spring")
elif a > 5 and a < 9:
    print("summer")
elif a > 8 and a < 12:
    print("autumn")
