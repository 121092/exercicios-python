def lista(inteiro):
    try:
        print(inteiro[4])
    except IndexError:
        print("a posicao 4 nao existe")


lista([8, 3, 4, 5])