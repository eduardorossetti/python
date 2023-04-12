class AgenciaBancaria: # Classe
    def __init__(self, codigo): # Contrutor
        # Atributos
        self.contas = [] # Lista vazia de contas da agência
        self.codigo = codigo # Código da agência

    def addConta(self, conta): # Método que adiciona uma conta à lista de contas da agência
        self.contas.append(conta)

    def getConta(self, num): # Método que verifica a conta e retorna
        for conta in self.contas:
            if conta.num == num:
                return conta
        return None

    def listContas(self): # Método que retorna uma string com o nome do titular, o número da conta e o saldo atual
        lista = ""
        for conta in self.contas:
            lista += f"Nome do titular: {conta.titular} | Número da Conta: {conta.num} | Saldo Atual: R${conta.saldo:.2f}"
        return lista


class Conta: # Classe
    def __init__(self, num, titular, saldo = 0.0): # Construtor
        # Atributos
        self.num = num # Número da conta
        self.titular = titular # Nome do titular
        self.saldo = saldo # Saldo atual

    def depositar(self, valor): # Método que deposita um valor ao saldo da conta
        self.saldo += valor

    def retirar(self, valor): # Método que retira um determinado valor do saldo da conta
        if self.saldo >= valor:
            self.saldo -= valor
            return valor
        else:
            return 0.0