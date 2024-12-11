import pandas as pd
import numpy as py

archivo = 'Prueba_Aleatoriedad/loteriaBOG.csv'

# 2216 Total de datos
df = pd.read_csv(archivo, header=None)

df = df.rename(columns={0: 'Datos'})

impar = []
par = []
for i in df['Datos']:
  if i % 2 != 0:
    impar.append(i)
  else:
    par.append(i)

# ei = n /m (2216/2)
# h0 = la cantidad de pares e impares es igual
# h1 = lo contrario

ei = 2216/2
oi_1 = len(impar)
oi_2 = len(par)
estadistico = (((oi_1 - ei)**2)/ei) + (((oi_2 - ei)**2)/ei)

# Usando la tabla de chi cuadrado
valor_critico = 3.8415


print()
print(estadistico)
print(f'Numero Impar: {oi_1}, Numero par: {oi_2}')



# ---------------------------------punto 2 --------------------------

oi0_999 = 0
oi1_1999 = 0
oi2_2999 = 0
oi3_3999 = 0
oi4_4999 = 0
oi5_5999 = 0
oi6_6999 = 0
oi7_7999 = 0
oi8_8999 = 0
oi9_9999 = 0

for i in df['Datos']:
  if 0 <= i <= 999:
    oi0_999 += 1
  elif 1000 <= i <= 1999:
    oi1_1999 += 1
  elif 2000 <= i <= 2999:
    oi2_2999 += 1
  elif 3000 <= i <= 3999:
    oi3_3999 += 1
  elif 4000 <= i <= 4999:
    oi4_4999 += 1
  elif 5000 <= i <= 5999:
    oi5_5999 += 1
  elif 6000 <= i <= 6999:
    oi6_6999 += 1
  elif 7000 <= i <= 7999:
    oi7_7999 += 1
  elif 8000 <= i <= 8999:
    oi8_8999 += 1
  elif 9000 <= i <= 9999:
    oi9_9999 += 1

ois = [oi0_999,oi1_1999, oi2_2999,oi3_3999,oi4_4999,oi5_5999,oi6_6999,oi7_7999,oi8_8999,oi9_9999]

def chiCuadrado(ois):
  ei = 2216/10
  estadistico_1 = 0
  for oi in ois:
    estadistico_1 += (((oi - ei)**2)/ei)
  return estadistico_1

# Ho = los datos se distribuyen uniformemente
# H1 = lo contrario

# 16.9190

# Como el estadistico es menor al valor critico, se acepta la Ho

print(chiCuadrado(ois))


# -------------------------punto 3-------------------------------

# Ho las obsevaciones sucesivas son independientes
# H1 lo contrario

ascendente = 1
descendente = 0
racha = True

lista_datos = [i for i in df['Datos']]
for i in range(len(lista_datos)):
  if lista_datos[i] > lista_datos[i-1]:
    if racha!= True:
      ascendente += 1
      racha = True
    # else:
  elif lista_datos[i] < lista_datos[i-1]:
      if racha!= False:
        descendente += 1
        racha = False

ua = (2*len(lista_datos)-1)/3
varianza = (16*len(lista_datos)-29)/90
a = ascendente + descendente
z = (a-ua)/((varianza)**0.5)



print(ascendente, descendente)
print(z)

#--------------------------------punto 4--------------------------------

# Ho = Los números están distribuidos aleatoriamente por encima y por debajo de la media

# H1 = lo contrario

media = py.mean(lista_datos)
superior_media = 0
inferior_media = 2216 - superior_media

racha_1 = True
racha_superior = 1
racha_inferior = 0

for i in range(len(lista_datos)):
  if lista_datos[i] > media:
    superior_media += 1
    if racha_1!= True:
      racha_superior += 1
      racha_1 = True
    # else:
  elif lista_datos[i] < lista_datos[i-1]:
      if racha_1!= False:
        racha_inferior += 1
        racha_1 = False

print(racha_superior, racha_inferior)