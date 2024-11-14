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

almanaqueVendido = [100,150,200,250,300]
probabilidadVenta = [0.3,0.2,0.3,0.15,0.05]


def calcularN(sigma):
  n = ((1.96**2) * (sigma ** 2) ) / 100
  return n


def main(n):
  simulado = demanda()
  cantidad_importar = n
  precio_simulado = (0.5 * r.random())+1.5
  while simulado > cantidad_importar:
    simulado = demanda()
  no_vendidos = cantidad_importar - simulado

  utilidad_maxima = (4.5 * simulado + no_vendidos * 0.75)-precio_simulado * cantidad_importar

  return utilidad_maxima


def main_secction(n):
  utilidad = []
  for i in range(10000):
    ganancia = main(n)
    utilidad.append(ganancia)
  desviacion_muestral = np.std(utilidad)
  print(f"Desviacion estandar con un importe {n} en muestra de 10000: {desviacion_muestral}")
  n = calcularN(desviacion_muestral)
  return int(n)


def master():
  # ideal = [main_secction(100), main_secction(150), main_secction(200), main_secction(250), main_secction(300) ]
  for i in almanaqueVendido:
    ideal = main_secction(i)
    utilidad_ideal = []
    for j in range(ideal):
      utilidad_ideal.append(main(i))
    desviacion_ideal = np.std(utilidad_ideal)
    media_ideal_ganancias = np.mean(utilidad_ideal)
    print(f"Desviacion_ideal: {desviacion_ideal} \nMedia ideal (X): {media_ideal_ganancias}\n")
    utilidad_ideal = []



master()

# iteracion_ideal = main_secction(250)

# print(iteracion_ideal)
# utilidad_ideal = []
# for i in range(int(iteracion_ideal)):
#   utilidad_ideal.append(main(250))

# print(np.std(utilidad_ideal))









# utilidad_all = []

# for i in almanaqueVendido:
#   lista_utilidades = []
#   for j in range(10000):
#       m = main(i)
#       lista_utilidades.append(m)

#   sigma = np.std(lista_utilidades)
#   utilidad_all.append(sigma)


# for i in utilidad_all:
#   print(calcularN(i))






# desviacion_estandar = np.std(utilidad_all)
# intervalo_confianza = (1.96 * desviacion_estandar)/np.sqrt(10000)
# print('Desviación estandar', desviacion_estandar)
# print('Media:', media)


# print(f"Intervalo de confianza {media} +/- {intervalo_confianza}")
# print('Ensayos requeridos', n)
