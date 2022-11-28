from math import gcd
from sympy.ntheory import factorint

n = int(input("\nIngrese el valor de n: "))
mostrar = int(input("\nPara ver los valores de las tuplas, ingrese: 1\nPara no ver los valores de las tuplas, ingrese: 0\nIngresar opción: "))

def crear_lista(n):
    return [i for i in range(1, n+1)]

def obtener_cant_primos(n):
    return len(factorint(n))

def encontrar_divs(n):
    return [num for num in range(1, n+1) if n % num == 0]

def crear_zs(n):
    return [int(n/div) for div in encontrar_divs(n)]

def obtener_cant_y_z(n):
    return len(encontrar_divs(n))

def obtener_xs(n, mostrar):
    xs = []
    for i in range(obtener_cant_y_z(n)):
        for x in range(crear_zs(n)[i]):
            if gcd(x, crear_zs(n)[i], encontrar_divs(n)[i]) == 1:
                xs.append(x)
                if mostrar:
                    print(f"({x}, {crear_zs(n)[i]}, {encontrar_divs(n)[i]})")
    return xs

def obtener_cant_tuplas(n, mostrar):
    return len(obtener_xs(n, mostrar))

def mostrar_resultados(n, mostrar):
    print(f"\nLos divisores de {n} son {encontrar_divs(n)}")
    print(f"La factorización prima de {n} es {factorint(n)}")
    print(f"La cantidad de factores primos distintos que tiene es {obtener_cant_primos(n)}")
    print(f"La cantidad de 3-tuplas posibles de ψ({n}) es {obtener_cant_tuplas(n, mostrar)}\n")

mostrar_resultados(n, mostrar)

