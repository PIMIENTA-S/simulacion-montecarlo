import random as r

def resul():
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
  # max = y(demanda) * pu(4.5) - x * cu(result())
  y = resul()
  pu = 4.5
  x = int(input("Ingrese el numero de almanaques a comprar: "))
  while y > x:
    y = resul()
  ra = r.random()
  cu = (((2-1.5)*ra)+1.5)

  max = y*pu - x*cu
  netas = (y*4.5 + ((x-y)*0.75)) - x*cu
  print("Utilidad maxima:", (y*4.5 + ((x-y)*0.75)))
  print("Inversion:", x*cu)
  print("Ganancias netas:", netas)
  print("Almanaques vendidos:", y)
  print("Costo unitario:", cu)


main()

