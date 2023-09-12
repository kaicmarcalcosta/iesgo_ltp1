import math

# Solicita ao usuário o raio do círculo em metros
raio = float(input("Digite o raio do círculo em metros: "))

# Calcula a área do círculo
area = math.pi * raio ** 2

# Calcula o perímetro do círculo
perimetro = 2 * math.pi 

# resultados no console
print(f"A área do círculo é {area:.2f} m²")
print(f"O perímetro do círculo é {perimetro:.2f} m")