n = 0
while True:
    user = int(input("Digite um inteiro maior que zero: "))
    if user <= 0:
        print(str(user) + " não é um número inteiro maior que zero.")
        break
    n = n + 1
    print(str(user) +  " é um número inteiro maior que zero! Você já digitou " + str(n) + " números inteiros maiores que zero!")