# Código para testar os métodos

from metodos import *

# Cria uma agência bancária
agencia = AgenciaBancaria(int(input("Digite o número da sua agência: ")))

# Cria uma conta e adiciona à lista de contas da agência
contasAgencia = Conta(input("Digite o número da sua conta: "), input("Digite o nome do titular: "), 0.0)
agencia.addConta(contasAgencia)
print("--------------------------------------------------------")

# Verifica se a conta foi adicionadas corretamente
print(agencia.listContas())
print("--------------------------------------------------------")

# Realiza depósitos e retiradas na conta
contasAgencia.depositar(float(input("Digite um valor a ser depositado: ")))
print("Valor em conta:", contasAgencia.saldo, "\n")
contasAgencia.retirar(float(input("Digite um valor a ser retirado: ")))
print("Valor em conta:", contasAgencia.saldo)
