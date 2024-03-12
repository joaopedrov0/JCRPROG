# Programa para descobrir se o número que o usuário digitou está entre os 10 primeiros números primos

primos = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]

n = int(input("Digite um número inteiro: "))

for num in primos:
    if num == n:
        print("O número que você digitou está entre os 10 primeiros números primos!")
        break
    elif primos[-1] == num:
        print("O número que você digitou não está entre os 10 primeiros números primos.")