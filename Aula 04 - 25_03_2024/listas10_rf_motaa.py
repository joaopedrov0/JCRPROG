#copiando listas utilizando o método .copy
#ele retorna a cópia de uma lista
#a cópia pode ser atribuida a uma variável

a = [1]
b = a.copy()
b.append(2)
c = b.copy()
c.append(3)
print(a)
print(b)
print(c)
print("\n")

#diferente de uma atribuição a 3 listas ao mesmo tempo
#quando atribuimos um novo valor a lista, acabamos atualizando as 3 ao mesmo tempo

a = [1]
b = a
b.append(2)
c = b
c.append(3)
print(a)
print(b)
print(c)
print("\n")

#tambem é possível concatenar listas utilizando "+"

a = [1,2]
b = [3,4]
c = [5,6]
print(a + b + c)
print(b + a + c)
print(c + b + a)
print(a + a + a)
print("\n")

#menção para fuinções úteis dentro do contexto de listas

numbers = [1,2,43,342,456,6,34,356,]

#print no menor numero
print(min(numbers))
#print no maior numero
print(max(numbers))
#print na soma dos numeros da lista
print(sum(numbers))