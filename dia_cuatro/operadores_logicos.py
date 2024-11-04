mi_and = 4 > 5 and 5 < 6
mi_or = 4 > 5 or 5 < 6
mi_not = not 'a' == 'a'





num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
    if num2 > num1:
        print(f"{num2} es mayor que {num1}")
    else:
            print(f"{num1} y {num2} son iguales")