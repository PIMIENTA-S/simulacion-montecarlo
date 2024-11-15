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


def main_section(n):
  utilidad = []
  for i in range(10000):
    ganancia = main(n)
    utilidad.append(ganancia)
  desviacion_muestral = np.std(utilidad)
  print(f"Desviacion estandar con un importe de {n} en muestra de 10000: {desviacion_muestral}")
  n = calcularN(desviacion_muestral)
  print(f"Con dicha desviación se calcula la cantidad optima(N): {int(n)}")
  return int(n)


def intervalo_confianza(mean, sigma, n):
  limite_1 = mean + (1.96*(sigma/np.sqrt(n)))
  limite_2 = mean - (1.96*(sigma/np.sqrt(n)))

  return [int(limite_2), int(limite_1)]



def master():
  for i in almanaqueVendido:
    ideal = main_section(i)
    utilidad_ideal = []
    for j in range(ideal):
      utilidad_ideal.append(main(i))
    desviacion_ideal = np.std(utilidad_ideal)
    media_ideal_ganancias = np.mean(utilidad_ideal)
    confianza = intervalo_confianza(media_ideal_ganancias, desviacion_ideal, ideal)
    print(f"Desviacion_ideal: {desviacion_ideal} \nMedia ideal (X): {media_ideal_ganancias}")
    print(f"Con un intervalo de confianza de {confianza}\n")
    utilidad_ideal = []

master()