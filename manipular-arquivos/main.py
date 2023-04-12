from time import sleep

def cinconotas():
    arquivo = open("arquivo.dat", 'r')
    nome = []
    lin = arquivo.readlines()
    print("Analisando arquivo, aguarde...")
    sleep(0.8)
    for alunos in lin:
        alunos = alunos.split()
        if (len(alunos) > 6):
            nome.append(alunos[0])
            print(alunos[0], "tem mais de 5 notas!")
            sleep(0.5)
        arquivo.close()

def medianotas():
    arquivo = open("arquivo.dat", 'r')
    print("Calculando a média, aguarde...")
    sleep(0.8)
    for lin in arquivo:
        dados = lin.split()
        notas = dados[1:]
        soma = 0
        for valor in notas:
            soma += float(valor)    
        media = soma/len(notas)
        print("O aluno %s obteve de média: %.1f" % (dados[0], media))
        sleep(0.5)
    arquivo.close()
    
def notamaior():
    arquivo = open("arquivo.dat", 'r')
    print("Carregando a maior nota de cada aluno...")
    sleep(0.8)
    for linha in arquivo:
        alunos = linha.split()
        for i in range(len(alunos[1:])):
            alunos[i+1] = int(alunos[i+1])
        print("A nota maior de", alunos[0], "foi:", max(alunos[1:]))
        sleep(0.5)
    arquivo.close()

def main():
    try:
        arquivo = open("arquivo.dat", 'r')
        cinconotas()
        print("-------------------------------------")
        medianotas()
        print("-------------------------------------")
        notamaior()
        print("-------------------------------------") 
        arquivo.close()
    except:
        print("Não foi possível ler o arquivo!")

if __name__ == '__main__':
    print("-------------------------------------")
    print("Atividade 4 - Manipulação de Arquivos")
    print("-------------------------------------")
    sleep(0.5)
    main()
    print("Obrigado :)")