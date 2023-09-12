import random

# criar um número qualquer entre 1 e 10
numero_aleatorio = random.randint(1, 10)

# Pedir para adivinhar o número
while True:
    try:
        palpite = int(input("Adivinhe o número entre 1 e 10: "))
        if 1 <= palpite <= 10:
            break
        else:
            print("Por favor, digite um número válido entre 1 e 10.")
    except ValueError:
        print("Por favor, digite um número válido entre 1 e 10.")

# Verificar se o palpite está correto
if palpite == numero_aleatorio:
    print("Você acertou!")
else:
    print(f"Você errou! O número correto era {numero_aleatorio}.")
