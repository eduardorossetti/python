def iniciais(entrada):
    conectores = ["e", "do", "da", "dos", "das", "de", "di", "du"]
    iniciais = ""
    nome = entrada.split()
    for i in nome:
        if i not in conectores:
            iniciais += i[0]
    print(f"{entrada} -> {iniciais}")
    return

def contador(texto):
    palavras = len(texto.split())
    print(f"No seu textos há {str(palavras)} palavras e {len(texto)} caracteres!") 
    return

if __name__ == "__main__":
    print("--------------------------------------")
    print("ATIVIDADE - LABORATÓRIO DE PROGRAMAÇÃO")
    print("--------------------------------------")
    entrada = input(str("Digite um nome completo: "))
    print()
    iniciais(entrada)
    print("--------------------------------------")
    texto = input("Digite um texto: ")
    print()
    contador(texto)
    print("--------------------------------------")