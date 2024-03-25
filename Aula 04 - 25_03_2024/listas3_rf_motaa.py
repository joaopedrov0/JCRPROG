#Verificar elementos dentro de uma lista, por posição
#Essa busca ocorre por 
#print(list[i])
#Lembrando que o primeiro elemento tem o indice 0, não 1

letters = ["A", "U", "O", "D", "W", "E"]
print(letters[1])
print(letters[0])
print(letters[4])
print(letters[-1])

#Tambem é possível adicionar indices negativos, visto que os mesmos recomeçam a lista da esquerda para a direita
#Mas só até as posições válidas

print(letters[82]) #Resulta em erro
print(letters[-9]) #Resulta em erro