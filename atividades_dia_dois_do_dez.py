#personalizando nome e idade
"""
class pessoa:
    def __init__(self, nome, idade ):
        self.nome = nome 
        self.idade = idade
 
def __str__(self):
    return f"o seu nome é {self.nome} e a sua idade é {self.idade}."
 
def maioridade(self):
    if self.idade > 17:
        print(f"você é maior de idade, você tem {self.idade}.")
"""
"""
usuario1 = pessoa("joão", 18)
usuario2 = pessoa("maria", 33 )
 
print(usuario1.idade)
print(f"o seu nome é{usuario1.nome}")
"""
class Carro:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.vendido = False
 
    def exibir_informacoes(self):
        status_venda = "Vendido" if self.vendido else "Não vendido"
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Status de venda: {status_venda}")
        print("")

   
 
    def vender(self):
        if not self.vendido:
            self.vendido = True
            print(f"O carro {self.marca} {self.modelo} foi vendido.")
        else:
            print("Este carro já foi vendido.")
 
    def ajustar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"O preço do carro {self.marca} {self.modelo} foi ajustado para R$ {novo_preco:.2f}")
 
# Instanciando pelo menos 5 objetos de carros
carro1 = Carro("Toyota", "Corolla", 2022, 85000.0)
carro2 = Carro("Ford", "Mustang", 2023, 120000.0)
carro3 = Carro("BMW", "X5", 2021, 110000.0)
carro4 = Carro("Chevrolet", "Cruze", 2022, 75000.0)
carro5 = Carro("Honda", "Civic", 2023, 80000.0)
 
# Exibindo informações dos carros
carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()
carro4.exibir_informacoes()
carro5.exibir_informacoes()
 
# Vendendo o primeiro carro
carro1.vender()
 
# Ajustando o preço do terceiro carro
carro3.ajustar_preco(105000.0)
 
 
