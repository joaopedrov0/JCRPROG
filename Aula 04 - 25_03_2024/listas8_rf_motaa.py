countries = ["Brasil", "Germany", "Brasil", "Italy", "England", "Brasil", "Brasil"]

#vamos contar quantas vezes um elemento aparece em uma lista
#para isso, utiliza-se o .count()
#o método recebe um parâmetro como elemento

print("How many times Brasil appears in the list?")
print(countries.count("Brasil"))

#remover todos os elementos com o .count

print("removing all elements")
#deve-se colcar o nome do país  que você quer remover]
x = str(input("Which country should be removed?"))
if x in countries:
    c = countries.count(x)
    for i in range(c):
        countries.remove(x)
    print(countries)
else:
    print("This element isn't in the list")

print("\n")

#invertendo a ordem dos elementos
#ocorre pelo método .reverse()
#esse comando não recebe parâmetros

print(countries)
print("lets reverse the list")
countries.reverse()
print(countries)
