def geraPrimeiroDigito(cpf):
    # receber valor como 123.456.789-09
    cpf_sd = cpf[0:11]
    mult = 10
    soma = 0
    for i in range(len(cpf_sd)):
        if (cpf_sd[i] != "."):
            aux = int(cpf_sd[i]) * mult
            mult = mult - 1
            soma = soma + aux
    resto = soma % 11
    digito1 = 11 - resto
    if digito1 >= 10:
        digito1 = 0
    return digito1

def geraSegundoDigito(cpf):
    # receber valor como 123.456.789-09
    cpf_sd = cpf[0:13]
    mult = 11
    soma = 0
    for i in range(len(cpf_sd)):
        if cpf_sd[i] != "." and cpf_sd[i] != "-":
            aux = int(cpf_sd[i]) * mult
            mult = mult - 1
            soma = soma + aux
    resto = soma % 11
    digito2 = 11 - resto
    if digito2 >= 10:
        digito2 = 0
    return digito2

def validaCPF(cpf):
    # recebeu valor como 123.456.789-09
    digito1 = geraPrimeiroDigito(cpf)
    digito2 = geraSegundoDigito(cpf)

    if digito1 == int(cpf[12]) and digito2 == int(cpf[13]):
        return True
    return False

def geraDigitos(cpf_sd):
    digito1 = geraPrimeiroDigito(cpf_sd)
    cpf_p = cpf_sd + "-" + str(digito1)
    digito2 = geraSegundoDigito(cpf_p)
    cpf = cpf_p + str(digito2)
    return cpf

#principal
print("Programa para gerar CPF")
cpf_sd = input("Digite os primeiros digitos do CPF:")

cpf = geraDigitos(cpf_sd)
print("O CPF completo é: ", end="")
print(cpf)



#print("Exercicio Validar CPF")
#cpf = input("Digite o CPF a ser verificado:")
#cpf = "111.112.111-11"

#print("CPF a ser verificado:")
#print(cpf)
#if (validaCPF(cpf)):
#    print("CPF válido!!!!")
#else:
#    print("CPF inválido ...")