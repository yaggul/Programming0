print()
print("Welcome to test grade system!")
lb=0
ub=100
score=int(input("Моля въведете общия брой точки от теста 0-100:"))
if score in range(lb,51):
    print()
    print("Слаб 2")
    print()
elif score in range(51,61):
    print()
    print("Среден 3")
    print()
elif score in range(61,71):
    print()
    print("Добър 4")
    print()
elif score in range(71,81):
    print()
    print("Много добър 5")
    print()
elif score in range(81,101):
    print()
    print("Отличен 6")
    print()
elif score>100:
    print()
    print("Много отличен 6")
    print()
    