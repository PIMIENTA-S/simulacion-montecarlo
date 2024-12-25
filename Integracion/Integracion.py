import random as r
import matplotlib.pyplot as plt


def genXi():
  a = 0
  b = 4
  c = 2.6

  listaXi = []
  listaCi = []

  aceptados_x = []
  aceptados_y = []
  for i in range(100000):
    u1 = a + (b - a) * r.random()
    u2 = a + (c - a) * r.random()

    #Evaluar x en funcion
    funcion_en_x = funtion(u1)
    if u2 <= funcion_en_x:
      aceptados_x.append(u1)
      aceptados_y.append(u2)
    else:
      listaXi.append(u1)
      listaCi.append(u2)


  return listaXi, listaCi, aceptados_x, aceptados_y



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

it 
ejeX, ejeY = genFuncion()
listaXi, listaCi, aceptadosX, aceptadosY = genXi()

# Calcular integral
punto_aceptados = len(aceptadosX)

estimacion = 2.6 * (punto_aceptados/ 100000) * 4

print(estimacion)



# Graficar
plt.plot(ejeX, ejeY, label="function(x)")

# Graficar los puntos Xi y Ci
plt.scatter(listaXi, listaCi, color="red", label="Puntos rechazados", zorder=5, s=10)
plt.scatter(aceptadosX, aceptadosY, color="blue", label="Puntos aceptados", zorder=5, s=10)


plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráfica de la función")
plt.legend()
plt.grid(True)
plt.show()