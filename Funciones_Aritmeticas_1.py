from math import gcd

n = int(input("Ingrese el n que desee evaluar: "))

def obtener_coprimos(n):
    return [coprimo for coprimo in range(1, n) if gcd(n, coprimo) == 1]

def obtener_phi(n):
    return len(obtener_coprimos(n))

def sumar_coprimos(n):
    return sum(obtener_coprimos(n))

def sumar_mitad_coprimos(n):
    mitad_coprimos = [obtener_coprimos(n)[i] for i in range(int(obtener_phi(n)/2))]
    return sum(mitad_coprimos)

def crear_ns(n):
    return list(range(3, n+1))

def crear_sumas(n):
    return [sumar_coprimos(i) for i in crear_ns(n)]

def crear_medio_sumas(n):
    return [sumar_mitad_coprimos(i) for i in crear_ns(n)]

def mostrar_resultado(n):
    print(f"\nEl resultado de la sumatoria de {n} es {sumar_coprimos(n)}")
    print(f"El resultado con phi(n)/2 es {sumar_mitad_coprimos(n)}\n")

mostrar_resultado(n)