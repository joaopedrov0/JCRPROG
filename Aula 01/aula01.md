# Anotações da Aula 01 da disciplina JCRPROG

## Entendendo a função "print()"

A função print() é uma função responsável por imprimir valores na tela. Ela pode receber múltiplos argumentos separados por vírgula, e os exibe na tela com um separador definido na chamada, ou o separador padrão " " (espaço)

```python
# Exemplo simples de uso da função "print()"
print("Hello world")

# Exemplo de uso com concatenação de múltiplas variáveis
print("Hello", "world")

# Alterando o separador padrão da função print() para múltiplos argumentos.
print("Hello", "World", sep="+")

# Alterando final do retorno da função print()
print("Hello World", end="!")

# Quebra de linha
print("Hello\nWorld")
```

## Entendendo Tipos Primitivos

Python tem uma série de tipos de dados, alguns deles foram apresentados nesta primeira aula

### String (str)
O tipo "string" é usado para representar textos, cadeias de caracteres, e normalmente são acompanhados de aspas simples ou duplas no começo e no final

```python
"Hello world"
'Hello world'
```

### Integer (Inteiro ou int)
O tipo "integer" é usado para representar números inteiros, como 0, -1, 10, 10000, 5000...

### Float
O tipo "float" é usado para representar números com casas decimais, como por exemplo 3.14, 10.5, 2.5, etc...
Um detalhe importante, diferente do que costumamos fazer na linguagem cotidiana ou durante cálculos matemáticos, em python os números com casas decimais separam a parte inteira da decimal usando um ponto (.) ao invés de uma vírgula (,).

### Boolean
O tipo "boolean" é usado para definir valores que são "True" ou "False".

## Atribuição de variáveis

### Atribuição simples
```python
nome = "Murilo"
```

### Atribuição de múltiplas variáveis
```python
nome, idade, id = "Fábio", 47, "234"
print(nome, idade, id) # Retorna 1 2 3
```

### Múltiplas atribuições em um comando
```python
a = b = c = 3
print(a,b,c) # Retorna 3 3 3
```

## Características do Python

### Case Sensitive
Significa que ele considera se uma letra é maiúscula ou minúscula para saber se uma variável é igual a outra. Por exemplo, definir uma variável chamada `nome` seria diferente de uma variável chamada `NOME` ou `Nome`.

### Tipagem Fraca
Python é uma linguagem que não é fortemente tipada, isso significa que uma mesma variável pode receber variáveis de diferentes tipos sem problema nenhum. Apesar do termo "fraca" isso não é necessariamente ruim, há vantagens e desvantagens em usar uma linguagem que não tem uma tipagem forte.
Um exemplo de uma linguagem fortemente tipada é o C, que você precisa definir qual vai ser o tipo de uma variável quando vai iniciá-la.

## Operações matemáticas

### Soma - "+"
```python
print(10 + 5) # Retorna 15
```

### Subtração - "-"
```python
print(10 - 5) # Retorna 5
```

### Multiplicação - "*"
```python
print(10 * 5) # Retorna 50
```

### Divisão - "/"
```python
print(10 / 5) # Retorna 2
print(5 / 2) # Retorna 2.5
```

### Divisão inteira - "//"
Esse operador matemático funciona de maneira similar ao apresentado anteriormente, porém ele ignora a parte decimal do resultado.
```python
print(10 / 5) # Retorna 2
print(5 / 2) # Retorna 2
```

### Resto da Divisão - "%"
Esse operador retorna o resto da divisão de dois números.
```python
print(10 % 5) # Retorna 0
print(9 % 2) # Retorna 1
print(5 % 2) # Retorna 1
```

### Potenciação - "**"
```python
print(2**2) # Retorna 4
print(2**4) # Retorna 16
print(2**10) # Retorna 1024)

# O primeiro número (lado esquerdo do operador) é a base, e o segundo (lado direitor do operador) é o valor do expoente.
```

### Operadores de incremento - "+="
```python
a = 5
print(a) # Retorna 5
a = a + 5
print(a) # Retorna 10
a += 5 
print(a) # Retorna 15
```

### Operadores de decremento - "-="
```python
a = 20
print(a) # Retorna 20
a = a - 5
print(a) # Retorna 15
a -= 5
print(a) # Retorna 10
```
