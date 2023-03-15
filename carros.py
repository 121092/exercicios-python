quantidade_passageiros = [1, 1, 1]
soma_passageiros = sum (quantidade_passageiros)
print(soma_passageiros)

lista_capacidade_carro = [1, 1, 53]
soma_carro = sum (lista_capacidade_carro)
print(soma_carro)

lista_capacidade_carro.sort(reverse=True)
print(lista_capacidade_carro)

assentos = 0
lista_resultado = []
for capacidade_carro in lista_capacidade_carro:
    if assentos + capacidade_carro <= soma_passageiros:
        assentos = assentos + capacidade_carro
        lista_resultado.append(capacidade_carro)
    elif lista_capacidade_carro[0] >= soma_passageiros:
        print(f"Serao necessarios 1 carro(s)")
        break
    else:
        tamanho = len(lista_resultado)
        print(f"Serao necessarios {tamanho} carros com {lista_resultado} assentos cada")
        break



