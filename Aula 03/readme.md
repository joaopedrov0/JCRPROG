# Anotações da Aula 03 da disciplina JCRPROG

## Comandos de repetição

Comandos de repetição, ou laços de repetição, são estruturas usadas para realizar uma tarefa repetidas vezes, ainda que você não saiba quantas vezes precisará repetir a tarefa.

### Estrutura `while`

Observe abaixo a sintaxe utilizada para o laço de repetição `while`

```python
while <condição>
    # Bloco de código a ser executado enquanto a condição seja verdadeira.
    ...
<continuação do código>
```

Agora observe um exemplo de uso da estrutura do while:

```python
contador = 5
while contador > 0:
    print(contador)
    contador = contador - 1
```

O código anterior tem a seguinte saída:

```
5
4
3
2
1
```

Observe que foi usado um contador que não estava na sintaxe apresentada a cima

## Arrays (Listas)

Em Python, listas são uma estrutura de dados muito importantes usada para armazenar várias variáveis em uma ordem específica.

### Inicializando um array

#### Sintaxe

Observe a sintaxe de inicialização de um array

```python
<nome do array> = [item1, item2, item3]
```

#### Exemplo de array

Observe abaixo um exemplo de um array em Python

```python
numeros = [1, 2, 3, 4, 5]
```

### Acessando os valores do array

Para acessar os valores dentro de um array, você deve acessá-los utilizando o índice do elemento entre couchetes (`[]`).

> Lembrete: A contagem SEMPRE começa em 0

Observe o exemplo abaixo de acesso a um valor de um array

```python
numeros = [1, 2, 3, 4, 5]
# Índice   0  1  2  3  4

print(numeros[2]) # Retorna 3
print(numeros[4]) # Retorna 5
print(numeros[5]) # Retorna erro, não existe o índice 5 no array "numeros"
```

### Acessando índices negativos

Python aceita índices negativos para acessar um valor de um array, porém nesse caso, ele começa a contagem do último número até o primeiro, ou seja, na ordem inversa.

Observe o exemplo abaixo:

```python
numeros = [1, 2, 3, 4, 5]
# Índice   0  1  2  3  4
# Índice  -5 -4 -3 -2 -1

print(numeros[0]) # Retorna 1
print(numeros[-1]) # Retorna 5
print(numeros[-2]) # Retorna 4
print(numeros[-6]) # Retorna erro, esse índice não existe no array "numeros".
```

## Outras estruturas de repetição

### Estrutura `for`

Uma estrutura alternativa ao `while` para escrever laços de repetição, é o `for`.

#### Sintaxe

Observe abaixo a sintaxe utilizada para usar o laço de repetição `for`.

```python
for <item da lista> in <lista>:
    # Bloco de código a ser executado para cada item da lista
```

#### Exemplo

Observe abaixo um exemplo usando a estrutura `for`

```python
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
```

O código anterior tem a seguinte saída:

```
1
2
3
4
5
```

#### Funções `range()` e `list()`

##### `range()`

A função `range()` é usada para gerar uma sequência de números inteiros.

##### `list()`

A função `list()` é usada para transformar uma sequência de números inteiros em uma lista.

##### Usando `range()` com `list()`

É possível combinar as duas funções para gerar uma lista de números inteiros, observe o exemplo abaixo:

```python
print(list(range(0, 10)))

# Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Ainda é possível acrescentar um terceiro argumento (diferente de 0) que representa o intervalo entre os números que serão incluidos na lista.

Observe os exemplos a seguir

```python
print(list(range(5, 20))) # Retorna [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list(range(5, 20, 1))) # Retorna [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list(range(5, 20, 2))) # Retorna [5, 7, 9, 11, 13, 15, 17, 19]
print(list(range(5, 20, 3))) # Retorna [5, 8, 11, 14, 17]
```

#### Usando `for` com `range()`

É possível usar a função `range()` para gerar um iterador para a estrutura `for`.

Observe o exemplo a seguir:

```python
for i in range(0, 5):
    print(i)
```

O código anterior tem a seguinte saída:

```
0
1
2
3
4
```

Observe que antes nós usávamos uma lista criada anteriormente para iterar usando o `for`.
Essa estrutura, porém, não é restrita a iteração de listas, você pode usar ela com usos semelhantes ao laço `while`, agora criando um iterador com a função `range`.