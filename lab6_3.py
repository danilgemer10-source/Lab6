import math

a = float(input("Введіть початок діапазону a: "))
b = float(input("Введіть кінець діапазону b: "))
h = float(input("Введіть крок h: "))

result = []

if h <= 0:
    print('Крок h має бути додатнім!')

elif a > b:
    print("Початок діапазону (a) має бути більшим за (b)!")

else:
    print("\n3:") 

    x = a

    while x <= b:
        f_x = (1 / (x**2 + 1)) + 1
        result.append([x, f_x])
        x = x + h
    print("x    f(x)")
    for row in result:
        print(row)

    max_row = max(result, key=lambda row: row[1])
    print("Рядок із найбільшим значенням функції:", max_row)

