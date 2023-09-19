"""
# print("olá, mundo.")
texto = "olá, mundo"
print(texto)

texto = "olá mundo, novamente"
print(texto)
"""
"""
#palindromo
def palindromo(palindromosinho):
    # Remove espaços em branco e converte a palavra para letras minúsculas
    palindromosinho = palindromosinho.replace(" ", "").lower()
    
    # Verifica se a palavra é igual à sua inversão
    return palindromosinho == palindromosinho[::-1]

# Solicita ao usuário que insira uma palavra
input_palindromo = input("Digite uma palavra: ")

# Verifica se a palavra é um palíndromo e exibe o resultado
if palindromo(input_palindromo):
    print(f"{input_palindromo} é um palíndromo!")
else:
    print(f"{input_palindromo} não é um palíndromo.")



"""












"""
#solicite ao usuario nome e sobrenome eretorne um usuário para login com as três primeiras letras do nome e as três primeiras do sobrenome
def login():
    nome = input("digite o seu nome: ")
    sobrenome = input("digite o seu sobrenome: ")
    login = nome[0:3] + sobrenome [0:3]
    print("o seu nome de login seria", login)
login()
"""
"""
# lista vazia para frutas
frutas_desejadas = []
#  loop para inserir frutas
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
"""
"""
#lista de frutas
def lista_de_compras():
    lista =[]
    fruta = input("digite o nome da fruta que deseja comprar ou 'sair' para sair: ").lower()
    while fruta != "sair":
        lista.append(fruta)
        print(lista)
        fruta = input("digite o nome da fruta que deseja comprar ou 'sair' para sair: ").lower()
    print(f"lista de compras: \n {lista}")
lista_de_compras()
"""
"""
#faça um programa que o usuario digite o raio de um circulo em m e o programa retorna no console a área

#área do circuito = pi * raio
#perimetro do circulo = 2 * pi * raio
def area_do_perimetro(raio):
    return match.pi ** 2

def perimetro_do_circulo(raio):
    return 2 * math.pi * raio
def dados_do_circuito():
    raio = float(input("digite o raio do circulo  em m: "))
    print(f"raio: ", raio)
    print ( f"Área do círculo: { area_do_circulo ( raio ) } m²" )
    print ( f"Perímetro do círculo: { perimetro_do_circulo ( raio ) } m" )
    exceto  ValueError :
    print ( "O valor inserido não é um número." )
    dados_do_circulo ()


dados_do_circulo ()
"""
"""
def calcular_signo(ano_nascimento):
    signos_chineses = ["Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Cabra", "Macaco", "Galo", "Cachorro", "Porco"]
    ano_base = 1900  # O ano base do horóscopo chinês é 1900
    indice_signo = (ano_nascimento - ano_base) % 12
    return signos_chineses[indice_signo]

# Solicitar o ano de nascimento do usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calcular e exibir o signo chinês
signo = calcular_signo(ano_nascimento)
print(f"Seu signo chinês é {signo}")
"""
"""
import re

# Função para verificar se um email é válido
def verifica_email(email):
    # Define o padrão de expressão regular para validar emails
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Usa a função match() do módulo re para verificar se o email corresponde ao padrão
    if re.match(padrao, email):
        return True
    else:
        return False

# Solicita ao usuário inserir um email
email = input("Digite um endereço de email: ")

# Chama a função verifica_email() para validar o email
if verifica_email(email):
    print("O email é válido.")
else:
    print("O email não é válido.")
"""
"""
import random

# Gera um número aleatório entre 1 e 10
numero_aleatorio = random.randint(1, 10)

# Solicita ao usuário que adivinhe o número
while True:
    try:
        palpite = int(input("Adivinhe um número entre 1 e 10: "))
        if palpite < 1 or palpite > 10:
            print("Por favor, digite um número válido entre 1 e 10.")
        else:
            if palpite == numero_aleatorio:
                print("Você acertou!")
                break
            else:
                print("Você errou!")
    except ValueError:
        print("Por favor, digite um número inteiro válido entre 1 e 10.")
"""


# Solicita ao usuário que escreva um texto
texto = input("Digite um texto: ")

# Inicializa uma variável para contar a quantidade de letras "a"
contagem = 0

# Percorre cada caractere no texto e verifica se é "a" (maiúsculo ou minúsculo)
for caractere in texto:
    if caractere == "a" or caractere == "A":
        contagem += 1

# Exibe o resultado
print(f"A letra 'a' aparece {contagem} vezes no texto.")
