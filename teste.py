class Cliente():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

clientes = []

for i in range(5):
    clientes.append(Cliente(nome = i, cpf = i*2))

p = Cliente(8,16)

for i in clientes:
    if p.cpf == i.cpf:print(False)
    else:print(True)