def verifica_multiplo_5_e_3(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        print(f"{numero} é múltiplo de 5 e de 3")
    else:
        print(False)

# Exemplo de uso da função:
numero = int(input(" digite um numero inteiro: "))
verifica_multiplo_5_e_3(numero)