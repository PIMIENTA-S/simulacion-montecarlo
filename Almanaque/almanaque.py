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


utilidad_all = []

for i in almanaqueVendido:
  print(i)
  lista_utilidades = []
  for j in range(10000):
      m = main()
      lista_utilidades.append(m)
  media = np.std(lista_utilidades)
  utilidad_all.append(media)

# for i in range(10000):

for i in utilidad_all:
  print(i)

# desviacion_estandar = np.std(utilidad_100)
# intervalo_confianza = (1.96 * desviacion_estandar)/np.sqrt(10000)
# print('Desviación estandar', desviacion_estandar)
# print('Media:', media)


# print(f"Intervalo de confianza {media} +/- {intervalo_confianza}")



# n = ((1.96**2) * (desviacion_estandar ** 2) ) / 100
# print('Ensayos requeridos', n)
