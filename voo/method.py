class Voo:
    def __init__(self, numero_voo, horario_voo):
        self.numero_voo = numero_voo
        self.horario_voo = horario_voo
        self.assentos_ocupados = []

    def getProximoAssento(self): #retorna o número do assento livre mais próximo, a partir do assento número 1.
        for i in range(1, 101):
            if i not in self.assentos_ocupados:
                return i
        return None

    def verificarAssento(self, numero_assento): #verifica se o número do assento recebido como parâmetro está ocupado.
        return numero_assento in self.assentos_ocupados

    def ocupar(self, numero_assento): #ocupa determinado assento do voo cujo número é recebido como parâmetro.
        if numero_assento in self.assentos_ocupados:
            return False #retorna False se o assento estiver ocupado.
        else:
            self.assentos_ocupados.append(numero_assento)
            return True #retorna True se o assento estiver livre.

    def getVagas(self): #retorna o número de assentos vagos disponíveis no voo.
        return 100 - len(self.assentos_ocupados)

    def getVoo(self): #retorna o número do voo.
        return self.numero_voo

    def getHoraVoo(self): #retorna a data do voo.
        return self.horario_voo

    def getMapaAssentos(self): #retorna uma string representando todos os 100 assentos do avião.
        mapa_assentos = ""
        for i in range(1, 101):
            if i in self.assentos_ocupados:
                mapa_assentos += 'x' #os assentos ocupados serão representados por x.
            else:
                mapa_assentos += '-' #os assentos vagos serão representados por -.
            if i % 25 == 0: #condição para quebra de linha.
                mapa_assentos += '\n'
            else:
                mapa_assentos += ' ' #espaços entre os assentos.
        return mapa_assentos