import random as r
import matplotlib.pyplot as plt


def genXi():
  a = 0
  b = 4
  c = 2.5
  listaXi = []
  listaCi = []
  for i in range(1000):
    u1 = r.random()
    u2 = r.random()
    listaXi.append( a + (b - a) * u1)
    listaCi.append( a + (c - a) * u2)
  return listaXi, listaCi



def funtion(x):
  return (x + ((x + (x**0.5))**0.5))**0.5

def genFuncion():
  ejeX = []
  ejeY = []
  for i in range(41):
    ejeX.append(i/10)
    ejeY.append(funtion(i/10))
  # print(ejeX, ejeY)
  return ejeX, ejeY



ejeX, ejeY = genFuncion()
listaXi, listaCi = genXi()


# Graficar
plt.plot(ejeX, ejeY, label="function(x)")

# Graficar los puntos Xi y Ci
plt.scatter(listaXi, listaCi, color="red", label="Puntos Xi y Ci", zorder=5)


plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráfica de la función")
plt.legend()
plt.grid(True)
plt.show()