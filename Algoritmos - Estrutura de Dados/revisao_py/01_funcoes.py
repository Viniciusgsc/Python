""" Função para calcular o Índice de Massa Corpórea (IMC) """
def imc(peso, altura): # Declaração da função
    return peso / (altura ** 2)
    
# print(f"Peso: 89, altura: 1.75, IMC: {imc(89, 1.75)}")

# p = float(input("Qual o peso?"))
# a = float(input("Qual a altura?"))
# i = imc(p, a) # Chamada da função

# print(f"Peso: {p}, altura: {a}, IMC: {i:.3f}")

# Importa o número pi
from math import pi

""" Função que calcula a área de uma forma geométrica especificada """
def calcular_area(base, altura, forma):
    if forma == "R":    # Retângulo
        return base * altura
    elif forma == "T":  # Triângulo
        return base * altura / 2
    elif forma == "E":  # Elipse
        return (base / 2) * (altura / 2) * pi # Número PI
    else:   # Forma desconhecida
        return None
        
# Exemplos de chamada da função calcular_area
print(f"Retângulo 15x25: {calcular_area(15, 25, 'R')}")
print(f"Triângulo 12x16: {calcular_area(12, 16, 'T')}")
print(f"Elipse 10x20: {calcular_area(10, 20, 'E')}")
        
        
    