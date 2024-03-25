# Listas e Tuplas

## Revisão das aulas anteriores

### Operações

#### Operações aritméticas

- Soma (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)

#### Operações lógicas

- Or (|)
- And (&)

### Dados primitivos

- int
- float
- string (concatenação e replicação)
- bool

### Tripé da programação estruturada

- Sequência
- Condição
- Repetição

## Listas

### Uso

A estrutura de lista em Python serve para armazenar múltiplos dados. Observe os exemplos a seguir: 

```python
fruits = ["Pineapple", "Banana", "Khaki", "Damascus"]
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
data = ["Carlos", 19, True, 1.78, 2001]
```

### Declaração de uso

#### Declaração explícita

Exemplo de declaração explícita de uma lista utilizando a função `list()` do Python:

```python
a = list(range(10))
a = list()
companies = list(["Toyota", "Volkswagen", "Ford"])
ifsp = list("IFSP")
```

### Acesso

Para acessar um item de uma lista, normalmente se usa sua posição para isso (começando em 0), observe o exemplo a seguir:

```python
letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
#           0    1    2    3    4    5    6    7
print(letters[0]) # Retorna "A"
print(letters[1]) # Retorna "B"
print(letters[4]) # Retorna "E"
```

Também é possível inverter a ordem de acesso, usando o índice decrescente, que acessa o item de trás para frente, observe esse exemplo aplicado ao mesmo exemplo anterior:

```python
letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
#          -1   -2   -3   -4   -5   -6   -7   -8
print(letters[-1]) # Retorna "A"
print(letters[-2]) # Retorna "B"
print(letters[-5]) # Retorna "E"
```

Caso o índice, seja ele positivo ou negativo, seja ínvalido, ou seja, superar o tamanho da lista, ele retorna um erro. Observe exemplos de tentativas de acesso que retornam um `IndexError`:

```python
letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
print(letters[10])
print(letters[-99])
```

### Tamanho da lista

Em Python, existe uma função que recebe como parâmetro uma lista ou string, e retorna o tamanho dela (itens no caso de lista, e caractéres no caso de string). Observe um exemplo de uso desta função em uma lista.

```python
numbers = [1, 2, 3, 4, 5]
print("Esta lista tem {} itens!".format(len(numbers)))

# Esta lista tem 5 itens!
```

### Acessando intervalos da lista

#### Estrutura

A estrutura para acessar intervalos de itens em uma lista é a seguinte:

`list[start:stop:step]`

No exemplo da sintaxe acima, `list` deve ser substituido pelo nome utilizado para se referir a lista que contém o item que você deseja acessar. 

`start` deve ser substituido pelo endereço do elemento que você quer começar a seleção do intervalo (com o endereço **incluso**).

`stop` deve ser substituido pelo endereço do elemento que você quer parar a seleção do intervalo (com o endereço **não incluso**).

`step` é o intervalo entre os endereços que ele vai usar para retornar os elementos.

Caso você não especifique algum desses valores, ou até mesmo nenhum deles, o Python assume como padrão os seguintes valores: 

- `start` = 0
- `stop` = `len(list)`
- `step` = 1

Observe o seguinte exemplo de uso:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[1:4:1]) # Retorna [2, 3, 4]
```

### Alterando um elemento

Para alterar um único elemento em uma lista, basta fazer como se faria para redefinir qualquer outra variável, porém no lugar do nome da variável, usa-se o acesso do elemento da lista.

Observe o exemplo a seguir: 

```python
numbers = [1, 2, 3, 3, 5]
numbers[3] = 4
print(numbers)

# Retorna [1, 2, 3, 4, 5]
```

### Alterando um trecho da lista

### Verificando inclusão de elemento

### Adicionando elementos

#### Usando o método `append()`

Para usar o método `append()`, deve-se respeitar a seguinte sintaxe:

`lista.append(elementoParaAdicionar)`

Onde está escrito `lista`, é onde você coloca o nome do array. Onde está escrito `elementoParaAdicionar` é onde você coloca o que você deseja adicionar na lista.

Observe o exemplo a seguir:

```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # Retorna [1, 2, 3, 4, 5, 6]
```

#### Usando o método `insert()`

O método `insert` recebe dois parâmetros, sendo o primeiro a posição de uma lista, e o segundo o elemento que será inserido na posição especificada. Quando o novo elemento é inserido na lista, todos os elementos nas posições seguintes se deslocam um índice afrente para liberar espaço e dar lugar ao novo item da lista.

Observe o exemplo a seguir:

```python
fruits = ["Pineapple", "Banana", "Damascus"]
fruits.insert(2, "Orange")
print(fruits) # Retorna ['Pineapple', 'Banana', 'Orange', 'Damascus']
```

### Obtendo a posição de um elemento

#### Usando o método `index()`

O método `index()` retorna a primeira posição de um elemento dentro de uma lista.

Para usar o método `index()`, deve-se usar a seguinte sintaxe:

`lista.index(elementoParaProcurarEndereco)`

Observe o exemplo a seguir:

```python
fruits = ['Pineapple', 'Banana', 'Orange', 'Damascus']
fruits.index("Pineapple") # Retorna 0
fruits.index("Orange") # Retorna 2
```

Observe que no exemplo, todos os valores usados para teste foram valores válidos dentro da lista. Caso algum dos itens não existisse na lista, o programa retornaria um erro.

##### Evitando erros

Para evitar o erro, pode-se usar uma condicional para apenas retornar o índice do valor caso ele exista na lista, observe o seguinte exemplo:

```python
fruits = ['Pineapple', 'Banana', 'Orange', 'Damascus']
if "Apple" in fruits:
    print(fruits.index("Apple"))
else:
    print("Apple is not in the list")
```

### Removendo elementos

#### Usando o método `remove()`

O método `remove` recebe um elemento que será procurado na lista, e caso seja encontrado, ele será removido da lista, caso não seja encontrado, ele retornará um erro.

Observe o exemplo a seguir:

```python
fruits = ['Pineapple', 'Banana', 'Orange', 'Damascus']
fruits.remove("Pineapple")
print(fruits) # Retorna ['Banana', 'Orange', 'Damascus']
```

##### Evitando erros

Assim como visto anteriormente no método `index()`, é possível evitar erros usando uma condicional antes de remove o elemento, observe o exemplo a seguir:

```python
fruits = ['Pineapple', 'Banana', 'Orange', 'Damascus']

if "Apple" in fruits:
    fruits.remove("Apple")
else:
    print("Apple is not in the list")
```

##### Removendo todas as ocorrências

Usando o método anterior, ele remove o primeiro elemento encontrado na lista, apenas. Para remover **todas as ocorrências** é possível usar o mesmo conceito, aplicado a um laço de repetição. Observe o exemplo a seguir:

```python
numbers = [1, 2, 3, 4, 2, 3, 2, 5, 2, 3]
while 2 in numbers:
    numbers.remove(2)
print(numbers) # Retorna [1, 3, 4, 3, 5, 3]
```

#### Usando o método `pop()`

O método `pop`, por padrão, remove o último elemento de uma lista. Alternativamente, ele pode receber um argumento com a posição de um elemento a ser removido da lista.

Como resultado, o método retorna o elemento removido, e cada elemento desde a posição especificada até o fim da lista é realocado para preencher o espaço deixado pelo elemento removido.

### Contando elementos

#### Usando o método `count()`

O método `count` recebe como parâmetro um elemento, e ele retorna a quantidade de ocorrências desse elemento nem uma lista.

### Criando listas de forma compacta

### Invertendo a ordem dos elementos de uma lista

Para inverter a ordem dos elementos de uma lista em Python, usa-se o método `reverse()`, esse método não recebe nenhum argumento e modifica a lista original.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.reverse()
print(numbers) # Retorna [9, 8, 7, 6, 5, 4, 3, 2, 1]
```

### Ordenando uma lista

Para ordenar uma lista em Python, usa-se o método `sort()`.

O método `sort` recebe como um parâmetro opcional "reverse", que deve ser um valor booleano que indica se a lista vai estar invertida (ordem descrescebte) ou não (ordem crescente).

Observe o exemplo a seguir:

```python
numbers = [3, 2, 4, 1, 5, 7, 6, 9, 8]
numbers.sort(reverse = False) # O mesmo que numbers.sort() sem nenhum argumento
print(numbers) # Retorna [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
numbers = [3, 2, 4, 1, 5, 7, 6, 9, 8]
numbers.sort(reverse = True)
print(numbers) # Retorna [9, 8, 7, 6, 5, 4, 3, 2, 1]
```

#### Método `sorted()`

O método `sorted` é usado para obter uma cópia ordenada de uma lista, porém, diferente dos métodos mostrandos anteriormente, ela não altera a lista original.

```python
numbers = [3, 2, 4, 1, 5, 7, 6, 9, 8]
print(sorted(numbers)) # Retorna [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers) # Retorna [3, 2, 4, 1, 5, 7, 6, 9, 8]
numbers.sort()
print(numbers) # Retorna [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Copiando uma lista, o método `copy`

O método `copy()` gera uma cópia de uma lista que pode ser atribuida como valor de uma variável, observe o exemplo a seguir:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newNumbers = numbers.copy()
```

### Concatenando listas

O operador `+` pode ser usado para concatenar listas, observe o exemplo a seguir:

```python
a = [1, 2]
b = [3, 4]
c = a + b
print(c) # Retorna [1, 2, 3, 4]
```

### Funções úteis para listas numéricas

#### Função `min()`

Retorna o menor valor numérico da lista.

#### Função `max()`

Retorna o maior valor numérico da lista.

#### Função `sum()`

Retorna a soma de todos os valores numéricos da lista.

## Tuplas

Tuplas são quase que idênticas ás listas, com a única diferença de que são imutáveis, isto é, não podem ter seu valor alterado.