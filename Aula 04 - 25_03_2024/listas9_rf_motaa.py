#ordenando listas
#para isso vamos usar o método .sort

numbers = [1,2,43,342,456,6,34,356,2]

#tambem podemos adicionar o parâmetro .reverse
#para ordenar de forma decrescente

print(numbers)
#o valor padrão do .sort() é colocar os elementos em forma crescente
numbers.sort()
print(numbers)
#para colocar de forma decrescente
numbers.reverse()
print(numbers)
print("\n")


#o método sorted também ordena os elementos da lista sem altera-los, copiando a lista]
#para testar melhor, comente a parte acima do código
print(sorted(numbers))
#invertendo a lista:
print(sorted(numbers)[::-1])
#ou seja o sorted não aletra a ordem da lista original
print(numbers)

