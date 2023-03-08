while (total_de_tentativas>0):
    total_de_tentativas = 3

    numero_secreto = 40
    chute_str = input ("digite o numero: ")
    print("voce digitou", chute_str)

    chute_str = int(chute_str)

    if (numero_secreto == chute_str):
        print("voce acertou")

    else:
        if (chute_str > numero_secreto):
            print("errou! seu numero é MAIOR que o numero secreto")
        elif (chute_str < numero_secreto):
            print("errou! seu numero é MENOR que o numero secreto")

    print("FIM DE JOGO")