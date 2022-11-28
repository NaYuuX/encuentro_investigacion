import matplotlib.pyplot as plt

u1 = float(input("Ingrese u1: "))
u2 = float(input("Ingrese u2: "))
n = int(input("Ingrese el n: "))

orden1 = [u1, u2]
orden2 = [u2, u1]
sucesiones = []

def numerador(orden1, orden2):
    pares = list(zip(orden1, orden2))
    multiplicar = [(par[0]*par[1]) for par in pares]
    return sum(multiplicar)

def sucesion(n): 
    aux = 3
    while aux <= n:
        u_n = numerador(orden1, orden2)/(aux-1)
        orden1.append(u_n)
        orden2.insert(0, u_n)
        sucesiones.append(u_n)
        aux += 1
    return u_n

def graficar(sucesiones):
    sucesion(n)
    plt.figure(figsize=(10,5))
    plt.plot(range(3, n+1), sucesiones)
    plt.grid(True)

def mostrar_resultados():
    for i, resultado in enumerate(sucesiones):
        print(f"u_{i+3} = {resultado}")

graficar(sucesiones)
plt.show()
#Para ver los valores de cada u_n, elimine el primer # de la siguiente línea
#mostrar_resultados() 