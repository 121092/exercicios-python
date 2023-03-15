# Exercicio: Implementar a função sort de forma que passando-se uma lista
# retorne uma lista ordenada em ordem crescente.
#
# OBS: Parâmetros podem ser adicionados ao metodo livremente.
# OBS: O objetivo é colocar a lista em ordem crescente sem usar a função sort que existe no python
#
numero = [7, 9, 3, 2, 5, 1]

def sort(ordemcrescente): #Função sort a ser implementada
    numero2 = []
    for indice in range(len(ordemcrescente)):
        inicio = 0
        for lista in ordemcrescente:
            if lista > inicio:
                inicio = lista
        numero2.insert(0, inicio)
        ordemcrescente.remove(inicio)
    return numero2

resultado = sort(numero) #chamada da função sort
print(resultado)
#print(sort(numero))

