import matplotlib.pyplot as plt

cant = int(input("Ingresar la cantidad de triángulos: "))

vertice_a = [xa, ya]
vertice_b = [xb, yb]
vertice_c = [xc, yc]

def vertice_xa(xa,ya,xb,yb,xc,yc):
    nume = ((yc-yb)**2)*xc + ((xc-xb)**2)*xa + (xc-xb)*(yc-yb)*(ya-yc)
    return nume/(((yc-yb)**2) + (xc-xb)**2)
def vertice_ya(xa,ya,xb,yb,xc,yc):
    nume = ((yc-yb)**2)*ya + ((xc-xb)**2)*yc + (xc-xb)*(yc-yb)*(xa-xc)
    return nume/(((yc-yb)**2) + (xc-xb)**2)

def vertice_xb(xa,ya,xb,yb,xc,yc):
    nume = ((yc-ya)**2)*xc + ((xc-xa)**2)*xb + (xc-xa)*(yc-ya)*(yb-yc)
    return nume/(((yc-ya)**2) + (xc-xa)**2)
def vertice_yb(xa,ya,xb,yb,xc,yc):
    nume = ((yc-ya)**2)*yb + ((xc-xa)**2)*yc + (xc-xa)*(yc-ya)*(xb-xc)
    return nume/(((yc-ya)**2) + (xc-xa)**2)

def vertice_xc(xa,ya,xb,yb,xc,yc):
    nume = ((ya-yb)**2)*xa + ((xa-xb)**2)*xc + (xa-xb)*(ya-yb)*(yc-ya)
    return nume/(((ya-yb)**2) + (xa-xb)**2)
def vertice_yc(xa,ya,xb,yb,xc,yc):
    nume = ((ya-yb)**2)*yc + ((xa-xb)**2)*ya + (xa-xb)*(ya-yb)*(xc-xa)
    return nume/(((ya-yb)**2) + (xa-xb)**2)

xa, ya = vertice_a[0], vertice_a[1]
xb, yb = vertice_b[0], vertice_b[1]
xc, yc = vertice_c[0], vertice_c[1]
a_, b_, c_ = [], [], []

aux = 0
while aux < cant:
    xa_, ya_ = vertice_xa(xa,ya,xb,yb,xc,yc), vertice_ya(xa,ya,xb,yb,xc,yc)
    xb_, yb_ = vertice_xb(xa,ya,xb,yb,xc,yc), vertice_yb(xa,ya,xb,yb,xc,yc)
    xc_, yc_ = vertice_xc(xa,ya,xb,yb,xc,yc), vertice_yc(xa,ya,xb,yb,xc,yc)
    a_.append([xa_, ya_])
    b_.append([xb_, yb_])
    c_.append([xc_, yc_])
    xa, ya, xb, yb, xc, yc = xa_, ya_, xb_, yb_, xc_, yc_
    aux += 1

def graficar_caso_base():
    a1, b1, c1 = vertice_a, vertice_b, vertice_c
    abcs = [a1, b1, c1, a1]
    xy = list(zip(*abcs))
    plt.plot(xy[0], xy[1])
    plt.grid(True)

def graficar_casos(a_, b_, c_, i):
    a, b, c = a_[i], b_[i], c_[i]
    abcs = [a, b, c, a]
    xy = list(zip(*abcs))
    plt.plot(xy[0], xy[1])
    plt.grid(True)

graficar_caso_base()
for caso in range(cant):
    graficar_casos(a_, b_, c_, caso)

plt.show()