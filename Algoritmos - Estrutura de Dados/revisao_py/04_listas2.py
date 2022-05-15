frutas = ["laranja", "maçã", "uva", "pera", "mamão", "abacate", "amora"]

# Imprimindo apenas a fruta na TERCEIRA posição
print(f"Fruta na terceira posição: {frutas[2]}")

# Substituindo "pera" por "melancia"
frutas[3] = "melancia"

# Imprimindo a lista
print(frutas)

print(25 * '-')

# Percorrendo a lista e exibindo seus elementos do primeiro
# ao último
for f in frutas:
    print(f)

print(25 * '-')

# Percorrendo a lista e exibindo seus elementos do último para
# o primeiro
for f in reversed(frutas):
    print(f)

print(25 * '-')

# Exibindo a posição e o valor de cada elemento da lista
for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")

print(25 * '-')

# Exibindo a posição e o valor de cada elemento da lista,
# em ordem reversa
for i in range(len(frutas) - 1, -1, -1):
    print(f"{i}: {frutas[i]}")