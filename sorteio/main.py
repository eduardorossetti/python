import random

def geraAposta(qtda): #módulo para gerar uma aposta de qtda de números
    aposta = []
    for i in range(qtda):
        while True:
            numSorteado = random.randint(1, 60)
            if numSorteado not in aposta:
                aposta.append(numSorteado)
                break
    return sorted(aposta)

def gerarMegaSena():
    megasena = []
    for i in range(6):
        while True:
            numero = random.randint(1, 60)
            if numero not in megasena:
                megasena.append(numero)
                break
    return sorted(megasena)

def verificaAposta(aposta, numMegaSena):
    numerosAcertos = []
    for i in range(len(aposta)):
        if aposta[i] in numMegaSena:
            numerosAcertos.append(aposta[i])
    return numerosAcertos

# Código para tester geraAposta
print('Esta é sua aposta: ')
aposta1 = geraAposta(6)
print(aposta1)
print('-------------------------------------------------------------------')

# Código para testar megaSena
print('Este são os números sorteados: ')
numerosMegaSena = gerarMegaSena()
print(numerosMegaSena)
print('-------------------------------------------------------------------')

numerosAcertos = verificaAposta(aposta1, numerosMegaSena)
if (len(numerosAcertos) > 0):
    print('Muito bem, bixo! Você acertou o(s) número(s): ')
    print(numerosAcertos)
else:
    print('Desculpe, você é muito azarado!')