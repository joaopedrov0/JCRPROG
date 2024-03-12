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

## Usando `break` e `continue` em laços de repetição

### `break`

O `break` é usado para interromper um laço de repetição.

Observe o exemplo a seguir utilizando `break`:

```python
# Programa para descobrir se o número que o usuário digitou está entre os 10 primeiros números primos

primos = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]

n = int(input("Digite um número inteiro: "))

for num in primos:
    if num == n:
        print("O número que você digitou está entre os 10 primeiros números primos!")
        break
    elif primos[-1] == num:
        print("O número que você digitou não está entre os 10 primeiros números primos.")
```

No exemplo anterior, quando o programa encontra um número na lista de números primos que é igual ao número digitado pelo usuário, ele para o laço de repetição, mesmo havendo mais números para passarem pela iteração, ou seja, quando ele encontra o que está procurando, ele encerra o laço ao invés de continuar procurando.

Observe mais um exemplo utilizando `break`:

```python
n = 0
while True:
    user = int(input("Digite um inteiro maior que zero: "))
    if user <= 0:
        print(str(user) + " não é um número inteiro maior que zero.")
        break
    n = n + 1
    print(str(user) +  " é um número inteiro maior que zero! Você já digitou " + str(n) + " números inteiros maiores que zero!")
```

O código anterior teve a seguinte saída utilizando os números 3, 2, 3, 5, 7 e -23 respectivamente:

```
Digite um inteiro maior que zero: 3
3 é um número inteiro maior que zero! Você já digitou 1 números inteiros maiores que zero!
Digite um inteiro maior que zero: 2
2 é um número inteiro maior que zero! Você já digitou 2 números inteiros maiores que zero!
Digite um inteiro maior que zero: 3
3 é um número inteiro maior que zero! Você já digitou 3 números inteiros maiores que zero!
Digite um inteiro maior que zero: 5
5 é um número inteiro maior que zero! Você já digitou 4 números inteiros maiores que zero!
Digite um inteiro maior que zero: 7
7 é um número inteiro maior que zero! Você já digitou 5 números inteiros maiores que zero!
Digite um inteiro maior que zero: -23
-23 não é um número inteiro maior que zero.
```

### `continue`

O `continue` é usado para interromper o bloco de código de um laço de repetição, pulando para o próximo iterador do laço.

Observe um exemplo usando `continue`:

```python
# Programa para imprimir números pares de uma lista de números

inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in inteiros:
    if n % 2 == 1:
        continue
    print(str(n) + " é um número par!")
```

O código anterior apresenta a seguinte saída:

```
2 é um número par!
4 é um número par!
6 é um número par!
8 é um número par!
10 é um número par!
```

## Laços aninhados

É possível utilizar laços de repetição dentro de outros laços de repetição, essa técnica é chamada por algumas fontes de "aninhamento de laços".

Observe o exemplo abaixo:

```python
# Programa para exibir uma tabuada de multiplicação até o 10

for i1 in range(1, 11):
    print("Tabuada do " + str(i1))
    for i2 in range(1, 11):
        print(str(i1) + " * " + str(i2) + " = " + str(i1 * i2))
```

O código anterior tem a seguinte saída:

```
Tabuada do 1
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10
Tabuada do 2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
Tabuada do 3
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30
Tabuada do 4
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
4 * 10 = 40
Tabuada do 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
Tabuada do 6
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = 60
Tabuada do 7
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70
Tabuada do 8
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
8 * 10 = 80
Tabuada do 9
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90
Tabuada do 10
10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
10 * 6 = 60
10 * 7 = 70
10 * 8 = 80
10 * 9 = 90
10 * 10 = 100
```

Observe mais um exemplo, onde usamos dois laços de repetição para desenhar um retângulo:

```python
# Desenhar um triângulo

width = int(input("Digite a largura do retângulo: "))
height = int(input("Digite a altura do retângulo: "))

for i in range(1, height + 1):
    for j in range(1, width + 1):
        print("#", end="")
    print()
```

Observe duas saídas de teste do código anterior:

```
Digite a largura do retângulo: 4
Digite a altura do retângulo: 5
####
####
####
####
####
```

```
Digite a largura do retângulo: 25
Digite a altura do retângulo: 3
#########################
#########################
#########################
```