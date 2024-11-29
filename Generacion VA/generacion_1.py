import random
import math

def circunferencia(alfa, beta, v):
  r = random.random()
  return (alfa*(-math.log(1-r))**(1/beta))+v

circunferencias = []

ite = 100000

for i in range(ite):
  circunferencias.append(circunferencia(0.005, 1/3, 3.25))

mayor_3_4 = sum([1 for c in circunferencias if c > 3.4])/ite    # 4% aprox

desecho = sum([1 for c in circunferencias if c > 3.5 or c < 3.3])/ite    # 90% apro

print(mayor_3_4, desecho)