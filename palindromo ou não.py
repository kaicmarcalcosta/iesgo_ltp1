def palindromo(kkk):
    # Remove espaços em branco e converte a palavra para letras minúsculas
    kkk = kkk.replace(" ", "").lower()
    
    # Verifica se a palavra é igual à sua inversão
    return kkk == kkk[::-1]

# Solicita ao usuário que insira uma palavra
input_palindromo = input("Digite uma palavra: ")

# Verifica se a palavra é um palíndromo e exibe o resultado
if palindromo(input_palindromo):
    print(f"{input_palindromo} é um palíndromo!")
else:
    print(f"{input_palindromo} não é um palíndromo.")
