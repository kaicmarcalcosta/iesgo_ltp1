# import array as ar

# obj = ar.array('i', [1,2,3])
# print(type(obj), obj)

# obj2 = ar.array('u', 'iesgo')
# obj2[0] = 'I'

# obj3 = ar.array('d', [1.233, 1.2334, 3.3])
# print(type(obj3), obj3)



"""
#criar meu array
import array as arr 

# Criar um array de inteiros vazio
meu_array = arr.array('i')

# Adicionar cinco no ao array
for i in range(5):
    num = int(input("Insira um número inteiro: "))
    meu_array.append(num)

print("Array resultante: ", meu_array)

# Somar os números do array
print(sum(meu_array))

# Encontrar o min e max
min_valor = min(meu_array)
max_valor = max(meu_array)
print(f"O menor valor é: {min_valor}\nO maior valor é: {max_valor}")

# Remover o último elemento
print(meu_array)
meu_array.pop()
print("Removido o último elemento", meu_array)

# Inverter a ordem
meu_array.reverse()
print("lista invertida: ", meu_array)
for i in range(5):
    num = int(input("insira um número inteiro: "))
    meu_array.append(num)

    print(f"array resultante: {meu_array}")
"""



"""
try:
    num = int(input("digite um numero inteiro: "))
    resultado = 10/num
except(ZeroDivisionError, ValueError):
    print("ocorreu um erro. certifique-se de digitar um numero valido ou não digitar zero")
else:
    print(f"o resultado da operação de 10 / {num} = {resultado}")
"""



# Questão: Gerenciamento de Fila de Banco com Prioridade

# Você foi designado para criar um programa em Python que simula a gestão de uma fila de banco do tipo FIFO (First-In, First-Out) com a capacidade de lidar com clientes prioritários de acordo com a lei. Sua tarefa é criar um programa que permita adicionar clientes à fila, atender o próximo cliente e visualizar a fila.

# A fila funciona da seguinte maneira:

# Quando um cliente chega ao banco, ele pode ou não ter prioridade por lei. Os clientes com prioridade por lei devem ser atendidos imediatamente e, portanto, pulam para a frente da fila.
# Os clientes que não têm prioridade por lei são adicionados ao final da fila.
# O atendimento é realizado no estilo FIFO, ou seja, o próximo cliente na fila é atendido.
# Os clientes podem escolher sair do banco a qualquer momento.
# Aqui está um resumo das funcionalidades que o programa deve ter:

# Adicionar cliente à fila:

# Solicita ao usuário o nome do cliente.
# Pergunta se o cliente tem prioridade por lei (S para Sim, N para Não).
# Se o cliente tiver prioridade, ele é adicionado à frente da fila. Caso contrário, é adicionado ao final da fila.
# Atender próximo cliente:

# Remove o próximo cliente da fila e informa que ele está sendo atendido.
# Visualizar fila:

# Exibe a fila atual, mostrando os nomes dos clientes na ordem em que estão na fila.
# Sair do programa:

# Encerra o programa.
# Lembre-se de que você precisa criar uma classe Cliente para representar as pessoas na fila. A lista fila deve conter objetos dessa classe para acompanhar os clientes e suas prioridades.

# Ao criar o programa, certifique-se de tratar erros e situações em que a fila está vazia.

# Siga as diretrizes acima para criar um programa Python que simule a gestão de uma fila de banco com clientes prioritários. Certifique-se de que o programa funcione corretamente e permita que os usuários interajam com a fila, adicionando clientes, atendendo-os e visualizando a fila.




class Cliente:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade

class FilaDeBanco:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome, prioridade):
        cliente = Cliente(nome, prioridade)
        if prioridade == 'S':
            self.fila.insert(0, cliente)
        else:
            self.fila.append(cliente)

    def atender_proximo_cliente(self):
        if self.fila:
            cliente_atendido = self.fila.pop(0)
            print(f"Atendendo o cliente: {cliente_atendido.nome}")
        else:
            print("A fila está vazia. Nenhum cliente para atender.")

    def visualizar_fila(self):
        if self.fila:
            print("Fila de clientes:")
            for cliente in self.fila:
                print(f"Nome: {cliente.nome}, Prioridade: {cliente.prioridade}")
        else:
            print("A fila está vazia.")

def main():
    fila_banco = FilaDeBanco()

    while True:
        print("\nOpções:")
        print("1. Adicionar cliente à fila")
        print("2. Atender próximo cliente")
        print("3. Visualizar fila")
        print("4. Sair do programa")
        escolha = input("Escolha a opção (1/2/3/4): ")

        if escolha == '1':
            nome = input("Nome do cliente: ")
            prioridade = input("O cliente tem prioridade por lei? (S para Sim, N para Não): ")
            fila_banco.adicionar_cliente(nome, prioridade)
        elif escolha == '2':
            fila_banco.atender_proximo_cliente()
        elif escolha == '3':
            fila_banco.visualizar_fila()
        elif escolha == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()