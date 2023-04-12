import random
from time import sleep

# Gera uma matriz [0]
def gerarMatriz(lin, col):
    matriz = [0] * lin
    for i in range(lin):
        matriz[i] = [0] * col
    return matriz

# Completa a matriz gerar anteriormente com valores aleatórios
def completarMatriz(mat, lin, col):
    for l in range(0, lin):
        for c in range(0, col):
            mat[l][c] = random.randint(10, 99)

# Exibe a matriz gerada e já preenchida com os números aleatórios            
def exibirMatriz(mat, lin, col):
    for l in range(0, lin):
        for c in range(0, col):
            print(f'[{mat[l][c]:^2}]', end='')
        print()

# Gera um vetor com números pares e ímpares, respectivamente
def retornaVetor(lin, col, mat):
    pares = []
    impares = []
    for l in range(lin):
        for c in range(col):
            if mat[l][c] % 2 == 0:
                pares.append(mat[l][c])
            else:
                impares.append(mat[l][c])
    vetor = sorted(pares) + sorted(impares)
    return vetor

# Exibe o percentual de ímpares e pares em cada uma das linhas da matriz
def exibirPercentual(mat):
    for l in range(len(mat)):
        pares = []
        impares = []
        for c in range(len(mat[l])):
            if mat[l][c] % 2 == 0:
                pares.append(mat[l][c])
            else:
                impares.append(mat[l][c])
        percPares = len(pares) * 100 / len(mat[l])
        percImpares = len(impares) * 100 / len(mat[l])
        print("linha %d: %d%% de pares e %d%% de ímpares" %(l, percPares, percImpares))
        sleep(1)

print('---------------------------------------')
print('Atividade 1: Laboratório de Programação')
print('---------------------------------------')
sleep(1)
    
if __name__ == "__main__":
    lin = int(input(f'Digite o número de linhas: '))
    col = int(input(f'Digite o número de colunas: '))
    print()
    sleep(1)
    mat = gerarMatriz(lin, col)
    completarMatriz(mat, lin, col)
    exibirMatriz(mat, lin, col)
    print()
    sleep(1)
    exibirPercentual(mat)
    print(retornaVetor(lin, col, mat))
    print('---------------------------------------')