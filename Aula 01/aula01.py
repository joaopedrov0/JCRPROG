# Função print()

print("Hello World")


# Múltiplos argumentos na função print()

print("Hello", "World")


# Alterando o separador padrão da função print() para múltiplos argumentos.

print("Hello", "World", sep="+")


# Quebra de linha

print("Hello\nWorld")


# Alterando final do retorno da função print()

print("Hello World", end="!")


# Tipos Primitivos
## Inteiro
print(type(10))

## Float
print(type(10.0))

## String
print(type("Hello World"))

## Booleano
print(type(False))
print(type(True))

# Definição de variáveis

pi = 3.1416 # definição da variável
print(type(pi)) # Retorna float

pi = 10 # sobrescrevendo o valor da variável
print(type(pi)) # Retorna int


# Múltiplas atribuições num comando
a = b = c = 3
print(a,b,c) # Retorna 3 3 3

# Valores diferentes em múltiplas variáveis
a,b,c = 1,2,3
print(a,b,c) # Retorna 1 2 3


# Python como linguagem case sensitive
c1 = 5
C1 = 10
print(c1) # Imprime 5
print(C1) # Imprime 10

# Operações matemáticas
# +
# -
# /
# *
# **
# //
# %