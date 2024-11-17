# Función que genera una observación de la distribución triangular
# triang(a,b,c) parámetros a: mín, c: moda, b: máx
# método usado: inversión

import random
import math
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



def disminucion_por_años():
   return 1-(triangular(5,8,10)/100)


def flujo_caja():
  tasa_descuento = 0.10
  impuestos = 0.40
  margen_inicial = 4000
  depreciacion = 700/5



def main():
  año_1 = triangular(50,75,85) * 1000


  año_2 = disminucion_por_años() * año_1
  año_3 = disminucion_por_años() * año_2

  print('Primer año:', año_1)
  print('Segundo año:', año_2)
  print('Tercer año:', año_3)

main()
