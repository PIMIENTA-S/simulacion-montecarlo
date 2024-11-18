import random
import math

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

#Practica 3

def triangular(ei,moda,ed):
  a=ei
  b=ed
  c=moda
  r=random.random()
  r1=(c-a)/(b-a)
  if r <=r1:
    obs=a+math.sqrt(r*(b-a)*(c-a))
  else :
    obs=b-math.sqrt((1-r)*(b-a)*(b-c))
  return(obs)

def calcularN(sd, D):
    z = 1.96
    n = ((z**2) * (sd**2)) / (D**2)
    return n

def intervalo_confianza(media, desviacion_estandar, n, nivel_confianza=0.95):
    # Calcular el valor crítico Z para el nivel de confianza dado
    z = norm.ppf(1 - (1 - nivel_confianza) / 2)

    # Calcular el margen de error
    margen_error = z * (desviacion_estandar / np.sqrt(n))

    # Calcular los límites del intervalo de confianza
    intervalo_inferior = media - margen_error
    intervalo_superior = media + margen_error

    return intervalo_inferior, intervalo_superior

def calcular_vpn(inversion_inicial, flujos_efectivo, tasa_descuento):
    vpn = -inversion_inicial

    for t, flujo in enumerate(flujos_efectivo, start=1):
        vpn += flujo / ((1 + tasa_descuento) ** t)

    return vpn

#simular demanda de ventas del carro
def simulacion():
  flujos_efectivo = []

  demanda_simulada = triangular(50000,75000,85000)
  costo_desarrollo = triangular(600000000,650000000,850000000)
  #costo_desarrollo = 700000000
  depreciacion = costo_desarrollo / 5
  margen_unidad = 4000

  for i in range(5):
    # Para cada año la tendencia a que la demanda cambie varia
    tendencia_demanda = triangular(0.05, 0.08, 0.1)

    contribucion = demanda_simulada * margen_unidad
    utilidad_sin_impuestos = contribucion - depreciacion
    utilidad_neta = utilidad_sin_impuestos * (1 - 0.4)
    flujo_caja = depreciacion + utilidad_neta

    # print("Año", i + 1)
    # print("Demanda simulada:", demanda_simulada)
    # print("Costo de desarrollo:", costo_desarrollo)
    # print("Depreciacion:", depreciacion)
    # print("Margen de utilidad:", margen_unidad)
    # print("Flujo de caja:", flujo_caja)
    # print()

    flujos_efectivo.append(flujo_caja)

    #Actualizacion de datos
    demanda_simulada = demanda_simulada * (1 - tendencia_demanda)
    margen_unidad = margen_unidad * ( 1 - 0.04)

  vpn = calcular_vpn(costo_desarrollo, flujos_efectivo, 0.1)
  return vpn

media_triangular = (600000000 + 650000000 + 850000000)/3
n_simulaciones = 12000
vpns = []

for i in range(n_simulaciones):
   vpns.append(simulacion())

desviacion_estandar = np.std(vpns)
media = np.mean(vpns)
n = calcularN(desviacion_estandar, 1000000)
intervalo_inferior, intervalo_superior = intervalo_confianza(media, desviacion_estandar, n_simulaciones)

print(f"La media de la distribucion triangular es: {media}")
print(f"El numero de simulaciones necesarias es: {n}")
print("Intervalo de confianza del 95% para la ganancia:")
print(f"({intervalo_inferior:.2f}, {intervalo_superior:.2f})")

# Crear el histograma
plt.hist(vpns, bins=30, edgecolor='black')  # bins define el número de barras

# Agregar etiquetas y título
plt.title('Histograma de una distribución normal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

# Mostrar el histograma
plt.show()