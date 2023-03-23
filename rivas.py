#desafio do dia: escrever um programa que receba um numero com antecessosr e sucessor
#saída: "O numero que voce digitou foi o x. Seu sucessor é x e seu antecessor é x"

#numero_escolhido = input ("digite o número: ")
#print("O numero que voce digitou foi", numero_escolhido)

#numero_escolhido = int (numero_escolhido)
#sucessor = numero_escolhido +1
#print("Seu sucessor é", sucessor)
#antecessor = numero_escolhido -1
#print("Seu antecessor é", antecessor )



def antecessor (numero_escolhido):
    antecessor = numero_escolhido -1
    return antecessor

def sucessor (numero_escolhido):
    sucessor = numero_escolhido +1
    return sucessor



numero_escolhido = int(input ("digite o número: "))
print("O numero que voce digitou foi", numero_escolhido)

depois = antecessor(numero_escolhido)
print(depois)

antes = sucessor(numero_escolhido) 
print(antes)

#numero_antecessor = int(input ("qual o antecessor do número? "))
#if(numero_antecessor == numero_escolhido -1):
    #print(True)
    

#else:
    #print(False)


#numero_sucessor = int(input("qual o sucessor do número? "))
#if(numero_sucessor == numero_escolhido +1):
    #print(True)
    
#else:
    #print(False)