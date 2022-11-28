a = int(input("\nIngrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
n = int(input("Ingrese el valor de n: "))

def crear_xs(n):
    return list(range(1, n))

def crear_ys(n):
    return list(range(1, n))

def buscar_pares(a, b, n):
    x_y = []
    for x in crear_xs(n):
        for y in crear_ys(n):
            if a*x + b*y == n:
                x_y.append((x, y))
                print(f"{a}*{x} + {b}*{y} = {a*x + b*y}")
    return x_y

def contar_pares(a, b, n):
    return len(buscar_pares(a, b, n))

print(f"La cantidad de (x,y) es {contar_pares(a, b, n)}")




