# Inicialize uma lista vazia para frutas
frutas_desejadas = []
#  loop infinito para inserir frutas
while True:
    # digite oque deseja
    fruta = input("Digite o nome da fruta que deseja comprar (ou 'sair' para encerrar): ")
    # compra ou encerra
    if fruta.lower() == 'sair':
        break  # vai sair do loop se o usuário digitar "sair"
    # adicionar frutas
    frutas_desejadas.append(fruta)
# imprima a lista
print("Lista de frutas desejadas:")
for fruta in frutas_desejadas:
    print(fruta)