# Strings

## Definição

Strings em Python são basicamente uma cadeia de caractéres, representada por uma lista imutável deles. E é identificada no código com aspas simples (`'`) ou aspas duplas (`"`) no começo e no final da string.

## Caractéres especiais

Existem alguns caractéres dentro de strings que são reservados para representar algumas coisas específicas no conteúdo, como por exemplo uma quebra de linha usando `\n`. 

Dois exemplos de caractéres especiais em strings no Python são `"` (aspas duplas) e `\` (contra-barra)

Para usar caractéres especiais (reservados) como caracteres normais da string, basta colocar uma contra-barra antes dele (isso serve para inserir contra-barra no texto também).

## Acesso a elementos de uma string

Como já dito anteriormente, string nada mais é que uma cadeia de caracteres, uma lista de caracteres, portanto, como uma lista, é possível acessar os caracteres (itens) dessa string (lista) usando a mesma sintaxe de `lista[índice]`

### Acessando intervalos

Assim como em listas comuns, é possível selecionar um intervalo de uma string como se faz para uma lista qualquer. Observe o exemplo a seguir.

```python
palavra = "abacate"
print(palavra[1:3:1]) # Retorna 'ba'
print(palavra[2:6:2]) # Retorna 'aa'
```

## Formatação de strings

### Usando a **função** `format()`

A função `format()` recebe um valor qualquer e uma string contendo qual a formatação desejada. Como resposta, ela devolve uma string com a formatação desejada.

### Usando o **método** `.format()`

Quando usado como um método de uma string, o método `.format()` recebe como parâmetros uma quantidade qualquer de variáveis que substituirão marcações especiais em strings. Observe o exemplo abaixo.

```python
mensagem = "A soma entre {} e {} é {}"
print(mensagem.format(2, 3, 5)) # Retorna 'A soma entre 2 e 3 é 5'
```

É possível também alterar a ordem e a formatação usando o método `.format()`, para isso, dentro das chaves (`{}`) você pode inserir a ordem e a formatação. Observe o exemplo a seguir.

```python
mensagem = "A soma entre {1:.2f} e {0:.2f} é {2:.2f}"
print(mensagem.format(2, 3, 5)) # Retorna 'A soma entre 3.00 e 2.00 é 5.00'
```

Note que no exemplo acima, a ordem dos números foi invertida na soma, ao invés de exibir 2 + 3 ele exibiu 3 + 2 (escrito por extenso). Isso ocorre pois dentro das chaves na string, nós indicamos que a posição do primeiro número seria a segunda a ser recebida. Como não especificamos ordem nas chaves antes, ele seguiu a ordem dos parâmetros, nesse caso, porém, nós informamos que queremos primeiro o segundo parâmetro e depois o primeiro.

## Concatenação

É possível concatenar das strings em uma só, para isso, usa-se o operador `+` para concatenar as strings

## Replicação

É possível também, replicar uma string um número determinado de vezes. Para isso, usa-se o operador `*`

## Tamanho da string

Para descobrir o tamanho de uma string (ou seja, quantos caracteres ela tem), usa-se a função len()

## Comparação de strings

Para comparar duas strings, pode-se usar `==`, ele devolverá `True` se as strings forem idênticas no momento da comparação, e `False` caso sejam diferentes.

## Verificar inclusão de uma sequência de caracteres de uma string

Assim como em uma lista, é possível usar o `in` para descobrir se um item ou sequência de itens existe em uma string. Observe o exemplo abaixo.

```python
print("thon" in "Python") # Retorna True
print("Thon" in "Python") # Retorna False
```

Também é possível verificar se a sequência de caracteres inicia com uma sequência específica, usando o método `startswith()`. Esse método recebe uma string e verifica se ela é igual ao começo da string que chamou o método. Observe o exemplo a a seguir.

```python
message = "Hello World"
message.startswith("Hello") # Retorna True
message.startswith("World") # Retorna False
```

### Método `index()`

O método `index()` recebe uma string como parâmetro e retorna o índice dessa string na string que chamou o método. Caso esse índice não exista (a string não está incluida na string que chamou o método) ele retorna um erro.

### Método `find()`

O método `find()` é bem semelhante ao `index()`, com a diferença de que ele retorna `-1` ao invés de um erro caso ele não encontre a string desejada dentro da string na qual se faz a busca.

### Método `strip()`

O método `strip()` é usado para remover formatação de uma string, ela remove espaços antes do texto, depois, remove tabulação e outros tipos de formatação.

## Manipulando strings

### Método `split()`

O método `split()` recebe uma string como parâmetro, contendo um separador e retorna uma lista com a string separada utilizando o separador escolhido ou separando por espaço caso nenhum separador tenha sido especificado.

Exemplo

```python
print("Hello World".split()) # Retorna ['Hello', 'World']
print("Hello World".split("o")) # Retorna ['Hell', ' W', 'rld']
```

### Método `join()`

O método `join()` une os uma lista de strings usando um separador escolhido ou espaço caso não seja especificado nenhum, observe o exemplo a seguir.

```python
message = ["Hello", "World"]
print(" ".join(message)) # Retorna 'Hello World'
```

### Função `replace()`

A função `replace()` busca uma string dentro de outra, e quando encontra, substitui a string encontrada por outra. Ela recebe como parâmetro duas strings, a que será buscada e substituida e a que vai substituir. Essa função altera todas as ocorrências da string definida, não apenas a primeira ou a última.

## Formatação do texto da string

### Método `capitalize()`

Garante que a primeira letra da string será maiúscula.

### Método `lower()`

Deixa todas as letras da string minúsculas

### Método `upper()`

Deixa todas as letras da string maiúsculas

## Verificação com string

### Método `isnumeric()`

Devolve `True` se os caracteres da string forem numéricos e `False` caso isso não se aplique a todos os caracteres.

### Método `isalpha()`

Devolve `True` se os caracteres da string forem letras e `False` caso isso não se aplique a todos os caracteres.

### Método `isalnum()`

Devolve `True` se os caracteres da string forem numéricos ou letras, e devolve `False` caso isso não se aplique a todos os caracteres.