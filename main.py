import sys
class Conta():
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0
        self.extrato = []    
        self.quant_saques = 0
    
    def deposito(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"\nDepósito efetuado no valor de R$ {valor:.2f}")
        print(f"O saldo atual é R$ {self.saldo:.2f}")
    
    def saque(self, valor):
        if self.quant_saques < 3:
            if valor <= 500 and valor > 0:
                if self.saldo - valor > 0:
                    self.saldo -= valor
                    self.extrato.append(f"Saque: R$ -{valor:.2f}")
                    self.quant_saques += 1
                    print(f"Saque efetuado no valor de R$ {valor:.2f}")
                    print(f"O saldo atual é R$ {self.saldo:.2f}")
                else: print("Você não tem saldo suficiente para esta operação.")
            else: print("O valor do saque deve ser maior do que 0 e menor ou igual a 500.")
        else: print("Você excedeu o limite de 3 saques.")

    def mostra_extrato(self):
        if self.extrato:
            print("\n---Extrato---")
            for i in self.extrato:
                print(i)
            print("---Fim---\n")
        else: print("\nSem movimentação.")
    
    def mostra_saldo(self):
        print("---Saldo---")
        print(f"R$ {self.saldo:.2f}")

class Cliente():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []
clientes = []
cli_sel = False
conta_sel = False
sequencial = 1
def f_clientes():
    global clientes
    global cli_sel
    while True:
        print("\ndigite:\n1 para cadastrar um cliente\n2 para selecionar um cliente\n3 para sair\n")
        try:
            escolha = int(input("Escolha uma opção!\n"))
        except:
            print("Opção inválida")
            continue
        if escolha == 1:
            nome = input("digite o nome\n")
            cpf = input("digite o cpf\n")
            cadastrado = False
            for i in clientes:
                if i.cpf == cpf:
                    cadastrado = True
            if cadastrado: print("Cliente já cadastrado")
            else: 
                clientes.append(Cliente(nome=nome, cpf=cpf))
                print(f"Cliente adicionado:\nnome: {nome}\nCPF: {cpf}\n")
        elif escolha == 2:
            cpf_selecionado = input("Digite o CPF do cliente para selecioná-lo")
            for i in clientes:
                if i.cpf == cpf_selecionado:
                    cli_sel = i
                    break
            if cli_sel: 
                print(f"Cliente Selecionado: {cli_sel.nome}")
                break
            else: print(f"CPF não cadastrado.")
        elif escolha == 3: sys.exit()
        else:print("opção inválida")

def f_contas():
    global sequencial
    global conta_sel
    while True:
        print(f"Cliente selecionado: {cli_sel.nome}")
        print("digite:\n1 para cadastrar uma conta\n2 para selecionar uma conta\n3 para voltar\n4 para sair\n")
        try:
            escolha = int(input("Escolha uma opção!\n"))
        except:
            print("Opção inválida")
            continue
        if escolha == 1:
            cli_sel.contas.append(Conta(numero=sequencial))
            sequencial += 1
            print(f"Conta cadastrada: {cli_sel.contas[-1].numero}")
        elif escolha == 2:
            num_conta = int(input("Digite o numero da conta para selecioná-la"))
            for i in cli_sel.contas:
                if i.numero == num_conta:
                    conta_sel = i
                    break
            if conta_sel: 
                print(f"Conta Selecionada: {conta_sel.numero}")
                break
            else: print(f"conta não cadastrada.")
        elif escolha == 3: f_clientes()
        elif escolha == 4: sys.exit()
        elif escolha == 5: 
            for i in cli_sel.contas: 
                print(i.numero)
        else:print("opção inválida")

def operacoes():
    while True:
        print(f"Cliente / Conta selecionada: {cli_sel.nome} / {conta_sel.numero}")
        print("\ndigite:\n1 para depósitos\n2 para saques\n3 para mostrar o extrato\n4 para mostrar o saldo\n5 para voltar\n6 para sair\n")
        try:
            escolha = int(input("Escolha uma opção!\n"))
        except:
            print("Opção inválida")
            continue
        if escolha == 1:
            try:
                valor = round(float(input("Digite o valor do depósito\n")),2 )
                conta_sel.deposito(valor)
            except:
                print("Valor inválido. Operação cancelada!")
        elif escolha == 2:
            try:
                valor = round(float(input("Digite o valor do saque\n")),2 )
                conta_sel.saque(valor)
            except:
                print("Valor inválido. Operação cancelada!")
        elif escolha == 3:
            conta_sel.mostra_extrato()
        elif escolha == 4:
            conta_sel.mostra_saldo()
        elif escolha == 5: f_contas()
        elif escolha == 6: sys.exit()
        else: print("Opção inválida.")

f_clientes()
f_contas()
operacoes()