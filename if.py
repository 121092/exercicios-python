
def verifica_tamanho_telefone(telefone):
    tamanho = len(telefone)
    #print(tamanho)
    return tamanho

continuar = True
while continuar:
    numero = input("telefone: ")

    if numero[0] == "9" and numero[1] == "9":
        tamanho = verifica_tamanho_telefone(numero)
        if tamanho >= 5:
            print("valido")
            continuar = False

        else:
            print("invalido")
    else:
        print("invalido")