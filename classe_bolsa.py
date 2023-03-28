class Produto():
    preco = 0
    produto_vendido = False

    def dar_desconto(self, desconto):
        self.preco = self.preco - desconto

    def notificar_venda(self):
        self.produto_vendido = True


class Bolsa(Produto):

    def __init__(self, marca, preco, cor, tamanho, acessorio={}):
        self.marca = marca
        self.preco = preco
        self.cor = cor
        self.tamanho = tamanho
        self.acessorio = acessorio

Bag1 = Bolsa(
    marca="schutz",
    preco=500,
    cor="azul",
    tamanho="pequena",
    acessorio={
        "chaveiro": "logo da marca, pompom",
        "carteira": "pequena, acompanha logo da marca, cor azul"
    }
)


print(Bag1.preco)

Bag1.dar_desconto(desconto=100)
print(Bag1.preco)

print(Bag1.produto_vendido)
print("a bolsa foi vendida!")
Bag1.notificar_venda()
print(Bag1.produto_vendido)