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