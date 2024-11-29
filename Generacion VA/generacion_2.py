import random as r
import math
def boxmuller(media, ds):

  # Genera dos números aleatorios uniformemente distribuidos en el intervalo (0, 1)
  u1 = r.random()
  u2 = r.random()

  # Aplica la transformación de Box-Muller
  z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
  #z2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)

  #Desestandarizacion
  x1 = ds*z1 + media
  #x2 = ds*z2 + media

  return x1


n = 10000

resultados_jornada = []
horas_extra = 0
intervalo_ruta = 0

semana_con_horas_Extra = 0

for i in range(n):
  organizar_correo = boxmuller(90, math.sqrt(25))
  viaje_inicial = boxmuller(10, math.sqrt(4))
  regreso_final = boxmuller(15, math.sqrt(4))
  labores_administrativas = boxmuller(30, math.sqrt(9))

  # segmentos de ruta
  plaza_luces = boxmuller(38, 4) # sqrt(16)
  carabobo = boxmuller(99, math.sqrt(29))
  shanghai = boxmuller(73, math.sqrt(20))
  la_cascada = boxmuller(52, math.sqrt(12))
  japon = boxmuller(85,5) # sqrt(25)

  jornada = (
    organizar_correo +
    viaje_inicial +
    regreso_final +
    labores_administrativas +
    plaza_luces +
    carabobo +
    shanghai +
    la_cascada +
    japon)
  
  resultados_jornada.append(jornada)

  if jornada > 480:
    horas_extra += 1
  
  if 456 <= jornada <= 504:
    intervalo_ruta += 1

  dias_con_horas_extra = 0

  for j in range(6):
    organizar_correo = boxmuller(90, math.sqrt(25))
    viaje_inicial = boxmuller(10, math.sqrt(4))
    regreso_final = boxmuller(15, math.sqrt(4))
    labores_administrativas = boxmuller(30, math.sqrt(9))

    plaza_luces = boxmuller(38, 4)
    carabobo = boxmuller(99, math.sqrt(29))
    shanghai = boxmuller(73, math.sqrt(20))
    la_cascada = boxmuller(52, math.sqrt(12))
    japon = boxmuller(85, 5)

    jornada_semanal = (
        organizar_correo +
        viaje_inicial +
        regreso_final +
        labores_administrativas +
        plaza_luces +
        carabobo +
        shanghai +
        la_cascada +
        japon
    )
    if jornada_semanal > 480:
      dias_con_horas_extra += 1
  
  if dias_con_horas_extra >= 2:
    semana_con_horas_Extra += 1
  
    


def main():
  duracion_esperada = sum(resultados_jornada)/n
  probabilidad_horas_extra = (horas_extra/n)*100
  probalidad_en_intervalo = (intervalo_ruta/n)*100
  probabilidad_repartir_horas_extra = (semana_con_horas_Extra/n)*100


  print(f'La duración esperada de la ruta es: {duracion_esperada:.4f}')
  print(f'La probabilidad de hacer horas extra es: {probabilidad_horas_extra:.2f}%')
  # print(f'Duración mínima de la jornada: {min(resultados_jornada):.2f}')
  # print(f'Duración máxima de la jornada: {max(resultados_jornada):.2f}')
  print(f'La probabilidad de repartir con horas extra(2+): {probabilidad_repartir_horas_extra:.2f}%')
  print(f'La probabilidad completar la ruta en 8h±24min: {probalidad_en_intervalo:.2f}%')



main()
# print(resultados_jornada)