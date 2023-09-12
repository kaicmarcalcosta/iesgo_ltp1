def é_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True
def main():
    try:
        user_input = int(input("Digite um número inteiro: "))
        if é_primo(user_input):
            print(f"{user_input} é um número primo.")
        else:
            print(f"{user_input} não é um número primo.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
if __name__ == "__main__":
    main()