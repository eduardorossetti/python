from method import *

#testando os métodos

horario = Horario(12, 15)

print('Horário escolhido: ', horario, horario.am_pm())

print('-------------------------------')

horario.incrementar_hora()
print('Hora incrementada: ', horario, horario.am_pm())

print('-------------------------------')

horario.incrementar_minuto()
print('Minuto incrementado: ', horario, horario.am_pm())

print('-------------------------------')

horario.decrementar_hora()
print('Hora decrementado: ', horario, horario.am_pm())

print('-------------------------------')

horario.decrementar_minuto()
print('Minuto decrementado: ', horario, horario.am_pm())