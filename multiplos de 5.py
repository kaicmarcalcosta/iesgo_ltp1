def e_multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

numero = int(input("digite um numero inteiro: "))
if e_multiplo_de_5(numero):
    print(f"o numero {numero} é multiplo de 5.") 
else:
    print(f"o numero {numero} não é multiplo de 5.")