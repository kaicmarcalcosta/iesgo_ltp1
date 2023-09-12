# Solicita ao usuário que digite um texto
texto = input("Digite um texto: ")

# Inicializa uma variável para contar as ocorrências da letra 'a'
contagem_a = 0

# Percorre cada caractere no texto
for caractere in texto:
    # Verifica se o caractere é igual a 'a' (maiúsculo ou minúsculo)
    if caractere == 'a' or caractere == 'A':
        # Se for 'a' ou 'A', incrementa a contagem
        contagem_a += 1

# Exibe o resultado
print(f"A letra 'a' aparece {contagem_a} vezes no texto.")
