def primo(n): # essa função recebe um número e verifica se ele é primo
    divisores = 0
    # Ex: verificar se o 6 é primo, como fazer isso?
    # dividir o 6 por 1, por 2, 3, 4, 5, até chegar nele mesmo
    # caso o resto da divisão entre 6/num seja 0, significa que a divisão é exata, e o número é um divisor
    # para o número ser considerado primo, o número de divisores deve ser igual a 2
    # ex. 3 possui dois divisores 1 e 3, é primo;
    # 11: dois divisores 1 e 11, primo;
    # 8: quatro divisores 1, 2, 4 e 8, não primo

    for i in range(1, n + 1): # nesse for (laço de repetição) vamos dividir o número recebido como parâmetro por todos os números inteiros antecessores
        if n % i == 0: # o operador "%" representa o resto da divisão
            divisores += 1

    if divisores == 2:
        return True # nesse caso, o retorno True indica que o número é primo

    else:
        return False # nesse caso, o retorno False indica que o número não é primo


def principal():
    numero = int(input("\nInforme um número inteiro: "))
    lista = []
    #contador = 1  >> alternativa caso seja usado o while

    for i in range(1, numero + 1): # esse for foi criado para preencher uma lista que vai de 1 até o número informado pelo usuário
        lista.append(i)

    #while contador < numero + 1:    >> essa é uma forma alternativa ao for, em que a repetição é feita usando o while
    #    lista.append(contador)
    #    contador += 1

    print(lista)

    for i in range(1, numero + 1):
        if primo(i): # essa é uma forma de escrever "if primo(i) == True:",
                    # conforme definimos na nossa função primo(), o retorno True significa que o número é primo
            print(i, "é um número primo") # caso o número seja primo, ele entrará no "if" e será exibido na tela

# esse trecho a seguir do código existe apenas para executar várias vezes o programa,
# a fim de conseguirmos testá-lo várias vezes de forma mais prática
while True:
    principal()