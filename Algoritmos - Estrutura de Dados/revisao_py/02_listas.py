# LISTAS EM PYTHON
# Listas são uma forma de armazenar vários valores em uma única variável
# Tais valores podem ser de tipos diferentes
valores = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23, "batata", "cenoura", True]

# Operações sobre listas

# 1) Percurso: percorre a lista do primeiro ao último elemento, fazendo algo com
# cada um deles. No caso, vamos exibir cada um dos elementos da lista com print()
for v in valores:
    print(v)
    
# 2) Inserindo um novo elemento no final da lista: append()
valores.append("cebola")
valores.append(29)

print('Após inserção de 2 valores no fim:', valores)

# 3) Inserindo um novo elemento especificando a posição: insert()
# Parâmetros:
# 1º: posição para inserir
# 2º: valor a ser inserido
valores.insert(4, 8) # Inserindo o valor 8 na posição 4
valores.insert(0, "chuchu") # Inserindo o valor "chuchu" na posição 0 (início da lista)

print('Após 2 insert():', valores)

# 4) Determinando a quantidade de elementos da lista: len()
print('Número de elementos na lista:', len(valores))

# 5) Removendo o último elemento da lista: pop()
ultimo = valores.pop()
print(f"{ultimo} era o último elemento da lista")
print('Após remoção do último elemento:', valores)

# 6) Removendo por posição: del
del valores[7] # Remove o elemento da posição 7
print('Após remoção da posição 7:', valores)

del valores[0] # Remove o elemento da posição 0 (primeiro elemento)
print('Após remoção da posição 0:', valores)

# 7) Removendo por valor: remove()
valores.remove(17) # Remove o valor 17
print('Após a remoção do valor 17:', valores)

valores.remove('cenoura')
print('Após a remoção do valor "cenoura":', valores)

# 8) Fatiando uma lista

# Cria uma sublista fatiando a lista valores, INCLUINDO a posição 0 mas EXCLUINDO
# a posição 6
sublista1 = valores[0:7] 
sublista2 = valores[4:10]
print('Sublista 1:', sublista1)
print('Sublista 2:', sublista2)
print('Valores:', valores)
print('Sublista de 5 a 9:', valores[5:9])

# Sublista do início até uma posição determinada
print('Sublista de 0 até 8:', valores[:8])

# Sublista de um determinado ponto até o final
print('Sublista de 6 até o final:', valores[6:])
