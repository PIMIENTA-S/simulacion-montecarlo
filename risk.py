import random as r
# Se importa la biblioteca random para simular el lanzamiento de los dados

def resul():
  ficha = 0
  cara = r.random()
  # NOTA: r.random da un numero que se encuentra entre 0-1

  # Dependiento del resultado de r.radom() es asignado a uno de las cara del dado
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
# Es devuelto el numero que por probabilidad haya salido


def atacante():
  # esta lista tiene como función almacenar los resultados en orden de los lanzamientos
  ataqueList = []
  # por reglas del juego, el atacante siempre tendrá 3 intentos
  for i in range(3):
    # Se agregan a la lista los resultados
    ataqueList.append(resul())
  return ataqueList

def defensa():
  # De la misma manera los defesores tiene una lista para almacenar sus intentos
  defensaList = []
  # En este caso tiene derecho a dos lanzamientos de dados 
  for i in range(2):
    defensaList.append(resul())
  return defensaList


def main(x):
  # Para llevar el conteo de las veces que se gana en el ataque, se crea una variable que se actualizará constantemente  
  ataqueGlobal = 0
  for i in range(x):
    # Por las reglas del juego el numero de soldados que atacan son 4 frente a los 3 que defienden
    numAtacante = 4
    numDefensa = 3

    # Para que traer los resultados de cada batalla son llamadas las funciones atacante y defensa
    a = atacante()
    b = defensa()
    # Una vez conseguidas las listas son ordenadas de manera descendente 
    a.sort(reverse=True)
    b.sort(reverse=True)


    # Estas variables son utilizadas para llevar un conteo por partida de cada una de las partidas
    ganaAtaque = 0
    ganaDefensa = 0

    # este ciclo es utilizado para comparar de manera eficiente ambas listas
    # el rango es dos para que en cada lista se tome solo los dos primeros numeros que simbolizan los dados obtenidos por cada parte
    for i in range(2):
      # la lista a hace referencia a los atacantes por que si son mayores estos ganan
      if a[i] > b[i]:
        # Se le suma una victoria al ataque
        ganaAtaque += 1
      else:
        # Por otra parte en cualquiera de los demas casos la victoria es para la defensa
        # Esto es debido a las reglas del juego las cuales en caso de un empate la victoria es para la defensa como tambien cuando estan tienen el numero mayor
        ganaDefensa += 1

    # Se compara las variables que llevan el conteo de las batallas ganadas para ambas partes
    # Por lo tanto como se expresó antes para que el ataque gane debe ser estrictamente mayor
    if ganaAtaque > ganaDefensa:
      # Se hace la correspondiente actualizacion de la variable global
      ataqueGlobal += 1
  
  # Se imprime cada una de las probabilidades para ambas partes
  print("La proporción en la cual el atacante gana es: ", ataqueGlobal/x)
  print("La proporción en la cual el defensor gana es: ", 1-(ataqueGlobal/x))


# Se hace el llamado de la funcion pricipal la cual a su vez hará el llamado subfunciones
main(int(input("Escriba el numero de batallas a simular: ")))

