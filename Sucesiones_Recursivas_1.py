import matplotlib.pyplot as plt

u1 = float(input("Ingrese u1: "))
u2 = float(input("Ingrese u2: "))
n = int(input("Ingrese el n: "))

sucesiones = []
sucesion = (u1**2 + u2**2)/ 2
suma = u1**2 + u2**2

aux = 3
while aux <= n:
    suma += sucesion**2
    sucesion = suma / aux
    sucesiones.append(sucesion)
    #Para ver los valores de cada u_n, elimine el primer # de la siguiente línea
    #print(f"u_{aux} = {sucesion}") 
    aux += 1

def graficar():
    plt.figure(figsize=(10,5))
    plt.plot(range(3, n+1), sucesiones)
    plt.grid(True)

graficar()
plt.show()