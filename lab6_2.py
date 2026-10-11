import math

a = float(input("Введіть початок діапазону a: "))
b = float(input("Введіть кінець діапазону b: "))
h = float(input("Введіть крок h: "))

if h <= 0:
    print('Крок h має бути додатнім!')

elif a > b:
    print("Початок діапазону (a) має бути більшим за (b)!")

else:
    print("\n2. Табулювання циклом із передумовою:") 

    x = a

    while x <= b:
        f_x = (1 / (x**2 + 1)) + 1
        print(f"x = {x:.4f} -> f(x) = {f_x:.4f}") 
        x = x + h
        