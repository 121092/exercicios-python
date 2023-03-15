class Conta():

    def __init__(self, saldo, dono, cpf=None):
        self.saldo = saldo
        self.dono = dono
        self.cpf = cpf
        
    
    def enviar_dinheiro(self, conta_destino, valor):
        self.saldo = self.saldo - valor
        conta_destino.saldo = conta_destino.saldo + valor 
        
    
    def cadastrar_cpf(self, numero_cpf):
        if not self.cpf == None:
            pass

        else:
            self.cpf = numero_cpf

    


usuario = Conta(saldo=10, dono="lis", cpf="01286566541")
usuario2 = Conta(saldo=5, dono="eva")

print(usuario.saldo)
print(usuario2.saldo)
print("lis está mandando dinheiro para eva")

usuario.enviar_dinheiro(usuario2, 5)

print(usuario.saldo)
print(usuario2.saldo)

print("mostrando o cpf das contas")
print(usuario.cpf)
print(usuario2.cpf)

print("cadastrando o cpf para eva")
usuario2.cadastrar_cpf("82364893")
print(usuario.cpf)
print(usuario2.cpf)



