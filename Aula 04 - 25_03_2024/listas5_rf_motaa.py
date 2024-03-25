#A estrutura da lista conta copm 3 campos
# list(start:stop:step)
# o trecho imnicio na posição "start", encerra na "stop", e varia de acordo com o "step"

fruits = ["Banana", "Pineapple", "Grape", "Apple"]
numbers = [1,2,43,342,456,6,34,356]
letters = ["A", "U", "O", "D", "W", "E"]
data = ["Rafael", 17, 1.83, True, 2006]

#caso não seja especificado, os valores padrão de pyhon serão list(0, (len(list)), 1)

#exemplos
print(fruits[1:4])
print(numbers[:3])
print(letters[-4:])
print(data[::2])
print(fruits[1::2])
print(numbers[::-1])
