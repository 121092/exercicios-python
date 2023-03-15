lista = [53, 4, 2, 1, 5]
#print(lista)
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

lista.append(53)
lista.sort()
print(lista)

lista.pop(2)
print(lista)

lista.remove(53)
print(lista)

soma = sum(lista)
print(soma)