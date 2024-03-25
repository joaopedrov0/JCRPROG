# Programa para imprimir números pares de uma lista de números

inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in inteiros:
    if n % 2 == 1:
        continue
    print(str(n) + " é um número par!")