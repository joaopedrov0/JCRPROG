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
```

### Alterando um trecho da lista

### Verificando inclusão de elemento

