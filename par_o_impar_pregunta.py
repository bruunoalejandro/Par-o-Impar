print("Ingrese un numero")
x = int(input())
if x % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
print("Deseas ingresar otro numero?")
res = input()
while res == 'si':
    x = int(input("Ingrese el numero que deseas: "))
    if x % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
    print("Deseas ingresar otro numero?")
    res = input()
print("Hasta luego.")