import matplotlib.pyplot as plt
from numpy import linspace, sin, cos, tan

n_iterado = float(input("Ingresar el valor x para iterar: "))
iteraciones = int(input("Ingresar cantidad de iteraciones: "))

def formula(num):
    return (num)

def crear_xs():
    return linspace(0, 10, 1000)

def obtener_ys():
    return [formula(y) for y in crear_xs()]

def iterar_y():
    aux = 0
    x = n_iterado
    iterados = [n_iterado]
    y = []
    while aux < iteraciones:
        x = formula(x)
        iterados.append(x)
        y.append(x)
        aux += 1
    return [iterados, y]

def hacer_grafica():
    plt.plot(crear_xs(), obtener_ys())
    plt.hlines(y=0, xmin=0, xmax=10, color='darkgray', linestyle='dashed')
    plt.vlines(x=0, ymin=0, ymax=10, color='darkgray', linestyle='dashed')
    plt.grid(True)

def iterar_x():
    x = iterar_y()[0]
    x.pop()
    return x

def graficar_iteraciones():
    plt.plot(iterar_x(), iterar_y()[1], "o")

grafica = plt.figure(figsize=(10,5))
hacer_grafica()
graficar_iteraciones()
plt.show()