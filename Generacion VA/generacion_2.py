import random
import math
def boxmuller(media, ds):

  # Genera dos números aleatorios uniformemente distribuidos en el intervalo (0, 1)
  u1 = random()
  u2 = random()

  # Aplica la transformación de Box-Muller
  z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
  #z2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)

  #Desestandarizacion
  x1 = ds*z1 + media
  #x2 = ds*z2 + media

  return x1

