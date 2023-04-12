class Contribuinte: #contem os atributos comuns a outras classes (nome, renda bruta e documento)
    def __init__(self, nome, documento, renda_bruta):
        self.nome = nome
        self.documento = documento
        self.renda_bruta = renda_bruta

    def calculoImposto(self): #método que será executado nas outras classes
        pass

class PessoaFisica(Contribuinte): #subclasse de Contribuinte
    def __init__(self, nome, documento, renda_bruta, sexo):
        super().__init__(nome, documento, renda_bruta)
        self.sexo = sexo #adicionado um atributo extra: sexo

    def calculoImposto(self): #redefine o método calculoImposto() e calcula o imposto com base nas instruções do exercício proposto, com as alíquotas propostas
        if self.renda_bruta <= 1400:
            imposto = 0
        elif self.renda_bruta <= 2100:
            imposto = self.renda_bruta * 0.1 - 100
        elif self.renda_bruta <= 2800:
            imposto = self.renda_bruta * 0.15 - 270
        elif self.renda_bruta <= 3600:
            imposto = self.renda_bruta * 0.25 - 500
        else:
            imposto = self.renda_bruta * 0.3 - 700
        return imposto

class PessoaJuridica(Contribuinte): #Subclasse de Contribuinte
    def __init__(self, nome, documento, renda_bruta, ano_de_fundacao):
        super().__init__(nome, documento, renda_bruta)
        self.ano_de_fundacao = ano_de_fundacao #adicionado um atributo extra: ano de fundação

    def calculoImposto(self): #redefine o método calculoImposto() e calcula novamente o imposto conforme instruções do exercício
        return self.renda_bruta * 0.1

class GrupoDeContribuintes: #cria uma lista de contribuintes
    def __init__(self):
        self.contribuintes = []

    def addContribuinte(self, contribuinte):
        self.contribuintes.append(contribuinte) #adiciona o contribuinte à lista

    def getTotalImposto(self): 
        total = 0
        for contribuinte in self.contribuintes:
            total += contribuinte.calculoImposto()
        return total #retorna a quantidade total de imposto devido (somatório do imposto devido por cada contribuinte)

    def getPorcentagemContribuintesFeminino(self): #retorna a porcentagem de contribuintes do sexo feminino mantidas na coleção
        if not self.contribuintes:
            return 0
        total_feminino = 0
        for contribuinte in self.contribuintes:
            if isinstance(contribuinte, PessoaFisica) and contribuinte.sexo == 'F':
                total_feminino += 1
        return (total_feminino / len(self.contribuintes)) * 100
