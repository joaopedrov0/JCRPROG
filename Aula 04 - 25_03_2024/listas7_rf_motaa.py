#verificar se um elemento está na lista
#ocorre pelo operador de incçusão "in"
#Retorna TRUE ou FALSE

fruits = ["Banana", "Pineapple", "Grape", "Apple"]
print("Banana" in fruits)
print("Pineapple" in fruits)
print("Watermelon" in fruits)
print("\n")

#Inserir um elemento na lista
#Ocorre através do método append()
#é adicionado no final

fruits.append("Cherry")
print(fruits)
print("\n")

#já para adicuionar um elemento em uma posição especifica
#utuiliza-se o método insert()
#insert(i, "")

fruits.insert(2, "Pear")
print(fruits)
print("\n")

#já o método .index() 
#serve para descobrir a posição de um elemento dentro de uma lista
#sua primeira ocorrência no caso
#caso não esteja na litsa, retorna um erro

print(fruits.index("Banana"))
print(fruits.index("Pear"))
print("\n")

#para evitar uma mensagem de erro podemos adicionar uma condicional relacionada ao .index

print("banana position")
if "Banana" in fruits:
    print(fruits.index("Banana"))
    print("\n")
else:
    print("Banana is not in the list")
    print("\n")

#no caso de um elemento que não está na lista
    
print("strawberry position")
if "Strawberry" in fruits:
    print(fruits.index("Strawberry"))
    print("\n")
else:
    print("Strawberry is not in the list")
    print("\n")

#tambem pode ser necessario remover coisas da lista, para isso o método .remove()
    
good_countries = ["Brasil", "Germany", "Brasil", "Italy", "England", "Brasil", "Brasil"]
print(good_countries)
good_countries.remove("Brasil")
print("\n")
#vai remover a primeira ocorrência
print(good_countries)
#se mandar remover um elemento que não está na lista, vai dar erro, que pode ser evitado com uma conmdicional
print("Argentina in the list?")

if "Argentina" in good_countries:
    good_countries.remove("Argentina")
else:
    print("Argentina is not a good country to be in the list")
print("\n")

#para remover todos, só é necessário colocar o remove em um laço
    
print("Já removemos 1 vez o Brasil, mas vamos remover todos")
print("Hora de remover o Brasil")
while "Brasil" in good_countries:
    good_countries.remove("Brasil")
print(good_countries)
print("\n")

#tambem existem outras possibilidades de remover elementos
#uma é utilizando o método .pop()
#sua sintaxe é
# print(list.pop(i))
#se o parâmetro estiver omitido, ele vai remover o ultimo

letters = ["A", "U", "O", "D", "W", "E"]
print(letters)
print("Vamos remover elementos")
print(letters.pop(4))
print(letters)
#não é necessário printar
letters.pop(2)
print(letters)
#parâmetro vazio
letters.pop()
print(letters)