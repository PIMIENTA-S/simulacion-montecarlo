import random as r


def resul():
  ficha = 0
  cara = r.random()
  if cara <= 1/6:
    ficha = 1
  elif cara <= 2/6:
    ficha = 2
  elif cara <= 3/6:
    ficha = 3
  elif cara <= 4/6:
    ficha = 4
  elif cara <= 5/6:
    ficha = 5
  return ficha


def atacante():
  ataqueList = []
  for i in range(3):
    ataqueList.append(resul())
  return ataqueList

def defensa():
  defensaList = []
  for i in range(2):
    defensaList.append(resul())
  return defensaList


def main(x):
  ataqueGlobal = 0
  for i in range(x):
    numAtacante = 4
    numDefensa = 3

    a = atacante()
    b = defensa()
    a.sort(reverse=True)
    b.sort(reverse=True)

    ganaAtaque = 0
    ganaDefensa = 0

    for i in range(2):
      if a[i] > b[i]:
        ganaAtaque += 1
      else:
        ganaDefensa += 1

    if ganaAtaque > ganaDefensa:
      ataqueGlobal += 1


  print("La proporción en la cual el atacante gana es: ", ataqueGlobal/x)
  print("La proporción en la cual el defensor gana es: ", 1-(ataqueGlobal/x))



main(int(input("Escriba el numero de batallas a simular: ")))

