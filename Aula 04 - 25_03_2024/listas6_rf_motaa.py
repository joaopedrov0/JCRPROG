#Alterando um elemento
#Ocorre por
# list[i] = value

fruits = ["Banana", "Pineapple", "Grape", "Apple"]
fruits[1] = "Orange"
print(fruits)

#tambem é possível aterar um trecho da lista 

numbers = [0, 1, 2, 3, 4, 5, 6, 7]
numbers[2:4] = ["A","B"]
print(numbers)

#o tamanho do trecho pode ser maior do que a quantidade de elementos que vão ser inseridos
numbers2 = [0, 1, 2, 3, 4, 5, 6, 7]
numbers2[2:5] = ["A","B"]
print(numbers2)
