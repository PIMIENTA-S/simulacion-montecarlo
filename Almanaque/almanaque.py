import random as r
import numpy as np

def demanda():
  vendido = 0
  cara = r.random()
  if cara <= 0.3:
    vendido = 100
  elif cara <= 0.5:
    vendido = 150
  elif cara <= 0.8:
    vendido = 200
  elif cara <= 0.95:
    vendido = 250
  elif cara <= 1:
    vendido = 300
  return vendido

# Valor esperado / varianza (variable discreta)
almanaqueVendido = [100,150,200,250,300]
probabilidadVenta = [0.3,0.2,0.3,0.15,0.05]
def valorEsperado():
  valor = 0
  for i in range(5):
    valor += (almanaqueVendido[i]*probabilidadVenta[i])
  return valor
# Varianza = E[x**2] - (E[x])**2

def main():
  simulado = demanda()
  # x = int(input("Ingrese el numero de almanaques a comprar: "))
  cantidad_importar = 100
  while simulado > cantidad_importar:
    simulado = demanda()
  precio_simulado = (0.5 * r.random())+1.5
  no_vendidos = cantidad_importar - simulado
  utilidad_unitaria = 4.5 - precio_simulado

  utilidad_maxima = utilidad_unitaria * cantidad_importar + no_vendidos * 0.75

  return utilidad_maxima


utilidad_100 = []

for i in range(10000):
  m = main()
  utilidad_100.append(m)

desviacion_estandar = np.std(utilidad_100)
print('Desviación estandar', desviacion_estandar)









main()

