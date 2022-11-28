import matplotlib.pyplot as plt

n = int(input("Ingrese la cantidad de sucesiones que desea: "))
u1 = float(input("Ingrese u1: "))
u2 = float(input("Ingrese u2: "))
u3 = float(input("Ingrese u3: "))
u4 = float(input("Ingrese u4: "))
uns = [u1, u2, u3, u4]

def sumatoria(uns, n):
    s = [(uns[i] * uns[-i]) for i in range(1,int(n/2))]
    return sum(s)

def corolario(uns, n, par):
    if par:
        return (n*uns[-1] - 2*sumatoria(uns, n)) / 2*u1
    return (n*uns[-1] - 2*sumatoria(uns, n) - uns[int(n/2)]**2) / 2*u1

aux = 5
sucesiones = []
while aux <= n:
    if aux%2 == 0:
        un_ = corolario(uns, aux, True)
    else:
        un_ = corolario(uns, aux, False)
    sucesiones.append(un_)
    uns.append(un_)
    #Para ver los valores de cada u_n, elimine el primer # de la siguiente línea
    #print(f"u_{aux} = {un_}")
    aux += 1

def graficar(sucesiones):
    plt.figure(figsize=(10,5))
    plt.plot(range(5, n+1), sucesiones)
    plt.grid(True)

graficar(sucesiones)
plt.show()
