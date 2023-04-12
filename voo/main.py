from method import *

#Código para testar métodos

voo1 = Voo('ABC2020', '12:35')
ocupados = [2, 4, 7, 8, 13, 24, 27, 32, 33, 38, 49, 63, 74] #Já defini os assentos ocupados, conforme exemplo da atividade.
for i in ocupados:
    voo1.ocupar(i)

print("Bem-vindo ao Voo", voo1.getVoo())
print("Horário previsto:", voo1.getHoraVoo())
print("-------------------------")
print("Acentos ocupados:")
print(voo1.getMapaAssentos())
print("Acento mais próximo disponível: ", voo1.getProximoAssento())
print("Vagas disponíveis:", voo1.getVagas())
print("------------------------------------")

assento_desejado = int(input("Digite o assento desejado: "))
print("Verificando se o assento está ocupado...", voo1.verificarAssento(assento_desejado))
print("Ocupando o assento...", voo1.ocupar(assento_desejado))
print("--------------------------------------------------")
print(voo1.getMapaAssentos())