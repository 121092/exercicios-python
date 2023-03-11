#exemplo de dicionario:
# usuario = {
#     "chave-1": 5,
#     "chave-list": ["morango", "melancia", "limao"],
#     "chave-dicionario": {
#         "chave-interna": 1
#     }
# }
# print(usuario["chave-list"])

#cadastro de informações de um único produto (bolsa)
#o programa deve executar em loop até você escrever a palavra SAIR
#caso contrario, o programa deve solicitar outras características do produto
#antes de finalizar o programa, as informações devem ser printadsa

bolsa = {}
print("para finalizar digitar SAIR")

while True:
    informacoes = input("informacoes: ")

    if informacoes == "sair":
        break

    
    caracteristica = input("valor: ")
    
    if bolsa.get(informacoes, False):
        if type(bolsa[informacoes]) == list:
            bolsa[informacoes].append(caracteristica)
            continue
        
        else:
            grupo = [caracteristica, bolsa[informacoes] ]
            #grupo.append(caracteristica)
            #grupo.append(bolsa[informacoes])
            caracteristica = grupo
            
    bolsa[informacoes] = caracteristica

    

print(bolsa)