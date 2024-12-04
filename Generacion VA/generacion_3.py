import math
import random as r


def g(x):
    return ((1/32)* 8-x**3)/0.5 # M = 0.5
n = 1000

def main():
    aceptar = 0
    rechazo = 0
    while aceptar < n:
        r1 = r.random()
        r2 = r.random()

        calcular_x = 4*r1 -2

        if r2 <= g(calcular_x):
            aceptar += 1
        else:
            rechazo += 1
    
    print(f'Para que se acepten 1000 observaciones hay que rechazar {rechazo}.')

main()