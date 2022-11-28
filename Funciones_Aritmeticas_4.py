from math import gcd as mcd

n = int(input("Ingrese el valor de n: "))

def crear_aes(n):
    return list(range(1, n))

def crear_bes(n):
    return list(range(1, n))

def crear_xs(n):
    return list(range(1, n))

def crear_ys(n):
    return list(range(1, n))

def comparar_ab(n):
    posibles_ab = []
    for a in crear_aes(n):
        for b in crear_bes(n):
            if (a < b) and (mcd(a, b) == 1):
                posibles_ab.append((a, b))
    return posibles_ab

def comparar_xy(n):
    posibles_xy = []
    for x in crear_xs(n):
        for y in crear_ys(n):
            if mcd(x, y) == 1:
                posibles_xy.append((x, y))
    return posibles_xy

def comparar_pares(n):
    funcionan = []
    for ab in comparar_ab(n):
        for xy in comparar_xy(n):
            if ab[0]*xy[0] + ab[1]*xy[1] == n:
                funcionan.append((ab[0], ab[1], xy[0], xy[1]))
                #Para ver los valores de cada 4-tupla, elimine el primer # de la siguiente línea
                #print(f"({ab[0]}, {ab[1]}, {xy[0]}, {xy[1]})")
    return funcionan

print(f"g({n}) = {len(comparar_pares(n))}")