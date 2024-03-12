# Desenhar um retângulo

width = int(input("Digite a largura do retângulo: "))
height = int(input("Digite a altura do retângulo: "))

for i in range(1, height + 1):
    for j in range(1, width + 1):
        print("#", end="")
    print()