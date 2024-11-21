# Función que genera una observación de la distribución triangular
# triang(a,b,c) parámetros a: mín, c: moda, b: máx
# método usado: inversión

import random
import math
import numpy as np
def triangular(ei,moda,ed):
  a=ei
  b=ed
  c=moda
  r=random.random()
  #para x entre a y c, r=(x-a)^2/(b-a)(c-a)
  #si x=a, r=0
  #si x=c, r=(c-a)/(b-a)
  r1=(c-a)/(b-a)
  #print(r)
  if r <=r1:
    obs=a+math.sqrt(r*(b-a)*(c-a))
  else :
    obs=b-math.sqrt((1-r)*(b-a)*(b-c))
  return(obs)

def calcularN(sigma,d):
  n = ((1.96**2) * (sigma ** 2) ) / d**2
  return n

def intervalo_confianza(mean, sigma, n):
  limite_1 = mean + (1.96*(sigma/np.sqrt(n)))
  limite_2 = mean - (1.96*(sigma/np.sqrt(n)))

  return [int(limite_2), int(limite_1)]

def simular(n):
  costo_fijo = 700000000
  # costo_fijo_desarrollo = triangular(600,650,850) * 1000000 una distinta para cada 5 años
  vpn_lista = []
  for i in range(n):
    vpn = 0
    valor_1 = 50000
    valor_2 = 75000
    valor_3 = 85000
    margen = 4000
    for j in range(5):
      # costo_fijo = triangular(600,650,850) * 1000000
      if j != 0:
        disminucion_ventas = triangular(0.05,0.08,0.10)
        valor_1 = valor_1 * (1-disminucion_ventas)
        valor_2 = valor_2 * (1-disminucion_ventas)
        valor_3 = valor_3 * (1-disminucion_ventas)
        margen = margen * 0.96

      ventas_anio = triangular(valor_1,valor_2,valor_3)

      contribucion = margen * ventas_anio
      depreciacion = costo_fijo / 5
      utilidad_antes_impuestos = contribucion - depreciacion
      utilidad_despues_impuestos = utilidad_antes_impuestos * 0.60
      flujo_caja_final = utilidad_despues_impuestos + depreciacion
      vpn += flujo_caja_final /((0.1+1)**(j+1))
    vpn_lista.append(vpn)
  return [np.mean(vpn_lista),np.std(vpn_lista)]

resultado = simular(10000)
print(resultado)
n = calcularN(resultado[1], 1000000)
print(n)
resultado_1 = simular(int(n))

intervalos = intervalo_confianza(resultado[0], resultado[1], n)
intervalos_1 = intervalo_confianza(resultado_1[0], resultado_1[1], n)
print(intervalos)
print("IC con N")
print(intervalos_1)

