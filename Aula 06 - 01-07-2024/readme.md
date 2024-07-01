# Dicionários

## O que são?

Dicionários são uma coleção de pares organizados em "chave":"valor" que nós chamamos de "itens". Como em um dicionário (o da vida real), os dicionários da computação são organizados com uma chave, e logo em seguida o que essa chave significa, ou sejam, seu valor para o programa.

Imagine que você esteja em um ambiente social e alguém se refira a você com o termo "honorável", mas você não sabe o que isso significa, então você recorre a um dicionário para descobrir como você deve interpretar isso.
Então você abre o dicionário e encontra o seguinte trecho:

`Honorável: digno de consideração, de respeito etc., segundo as normas sociais vigentes (diz-se de alguém ou algo)`

Agora, você sabe que quando alguém se referir a você ou outra pessoa com o termo honorável, ela está querendo atribuir a você as qualidades do adjetivo que você acabou de ler.

De modo mais resumido, o dicionário tem a palavra (chave) e seu significado, ou como você deve interpretá-la (valor).

## Iniciando um dicionário
Existem duas maneiras possíveis de se declarar um dicionário. A forma  `implícita` e a `explícita`. Confira as duas formas logo a baixo

### Declaração Implícita
A forma implícita é uma declaração um pouco mais discreta, você não "verbaliza" que quer criar um dicionário mas sinaliza com as chaves (`{}`).

Sintaxe:

```
<nome do dicionário> = {...}
```

Exemplo:

```python
dictionary = {}
```


### Declaração Explícita

A forma explícita é uma declaração onde você usa a função dict() para criar um dicionário.

Sintaxe

```
<nome do dicionário> = dict({})
```

Exemplo:

```python
dictionary = dict({})
```

### Inicializando um dicionário não vazio

Os exemplos a seguir são de dicionários inicializados tanto da maneira implícita quanto explícita.

```python
# Declaração implícita

carro = {
    "rodas": 5,
    "portas": 2,
    "lugares": 5,
}

pikachu = {
    "tipo": "elétrico",
    "hp": 35,
    "ataque": 55
}

# Declaração explícita

Julia = dict({
    "cor favorita": "Amarelo",
    "numero da sorte": 7
    "idade": 19
})

login = dict({
    "username": "Paulo",
    "token": "837j23",
    "vencimento": "22/12/2024"
})

```

## Tipos de chaves e valores diferentes

É possível que sua chave e seu valor tenha tipos variados. Por exemplo, você pode ter um item com uma chave numérica e outro com um texto na chave.

```python
dicionario_exemplo = {
    123: "Primeira contagem",
    "123": "Segunda contagem",
}

dicionario_exemplo[123] # Retorna "Primeira contagem"
dicionario_exemplo["123"] # Retorna "Segunda contagem"
```

No primeiro caso, eu usei uma chave numérica, mas no segundo, eu usei uma string. Apesar de serem números dentro de uma string, o Python está interpretando como um texto por conta do tipo `string` que está sendo usado ao invés de um inteiro. Resumindo, preste atenção no tipo das chaves e valores, pois eles são relevantes para que o Python encontre o que você precisa dentro do seu dicionário.

## Acessando valores dos dicionários

Para acessar valores de dentro de dentro de um dicionário, você pode usar a chave desse valor, como no exemplo abaixo

```python
dictionary = {
    "chave 1": "valor 1",
    "chave 2": "valor 2",
    "chave 3": "valor 3",
}

print(dictionary["chave 1"]) # "valor 1"
```

Sempre que quiser acessar um valor dentro de um item de um dicionário com uma chave, siga a sintaxe `<nome do dicionário>[<chave do item que você quer>]`.

## Acessando chaves que não existem

Caso a chave que você tenha tentado encontrar no dicionário não exista, o Python retornará um erro.

## Verificando a existência de chaves

Para evitar a ocorrência de erros, em alguns casos é recomendável verificar se uma chave existe antes de tentar chamar seu valor de dentro de um dicionário.

### Usando `in`

```python
dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
print("a" in dictionary) # True
print("d" in dictionary) # False
```

### Usando `get`

```python
dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(dictionary.get("a")) # 1
print(dictionary.get("d")) # Não retorna nada.
```

## Verificando o tamanho de um dicionário

É possível, assim como em listas e outros tipos de dados, verificar o tamanho de um dicionário usando a função `len()`.

```python
dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(len(dictionary)) # 3
```

## Adicionando valores

Para adicionar novos itens ao dicionário basta selecionar uma chave que não está sendo usada e definir um valor para ela, como no exemplo abaixo.

```python
dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
dictionary["d"] = 4
print(dictionary) # Exibe o dicionário atualizado, agora com a chave "d" apontando para o valor "4"
```

> Caso você coloque uma chave já existente entre os colchetes, o valor referente aquela chave será atualizado com o novo valor que você definiu.

## Removendo valores

É possível usar vários métodos diferentes para excluir itens de dicionários, observe os exemplos abaixo com alguns desses métodos

### Remoção com `pop()`

```python
# Sintaxe: <nome do dicionario>.pop(<chave>)
dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(dictionary.pop("a")) # Retorna "1"
print(dictionary) # Retorna os pares b:2 e c:3 apenas.

# Se a chave a ser exluída do dicionário não existir, será gerado um erro.
```

### Remoção com `popitem()`

```python
# Sintaxe: <nome do dicionario>.popitem()
dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(dictionary.popitem("a")) # Retorna ("c", 3), ou seja, uma tupla com o par chave/valor excluído do dicionário
print(dictionary) # Retorna os pares a:1 e b:2 apenas.

# Se o dicionário não tiver nenhum item, será gerado um erro.
```

> O método `.popitem()` não recebe argumentos/parâmetros obrigatórios para a remoção, ele sempre remove por padrão o último item do dicionário.

### Remoção com `del`

```python
dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
del dictionary["b"]
print(dictionary) # Retorna os pares a:1 e c:3 apenas.
```

## Atualizando valores - O método `update`

O método `.update()` recebe como argumento outro dicionário, e com base no seu conteúdo ele adiciona conteúdos que o segundo dicionário tem a mais no dicionário original, e sobrescreve valores que tem a mesma chave. Observe o exemplo abaixo para que fique mais claro

```python
dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
dictionary_2 = {
    "a": 1,
    "b": 5,
    "d": 4
}
dictionary.update(dictionary_2)
print(dictionary) # Retorna ('a': 1, 'b': 5, 'c': 3, 'd': 4)
```

Observe que o dicionário original não tinha a chave `'d'`, e ela foi adicionada pelo segundo dicionário. O dicionário já tinha a chave `'b'` só que com um valor diferente, que foi atualizado de acordo com o segundo dicionário, e a chave `'a'` que coexistia em ambos não foi alterada, nem a chave `'c'`, ausente no dicionário original.


## Listando chaves e valores

As vezes você pode querer listar todos os valores ou todas as chaves de um dicionário, ou até mesmo ambos. Com os métodos `.keys()`, `.values()` e `.items()` você pode fazer isso

### Listando chaves

```python
dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(list(dictionary.keys())) # Retorna ['a', 'b', 'c']
```

### Listando valores

```python
dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(list(dictionary.values())) # Retorna [1, 2, 3]
```

### Listando itens

```python
dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(list(dictionary.items())) # Retorna [('a', 1), ('b', 2), ('c', 3)]
```

## Iterando sobre chaves, valores e itens

Como você viu, listar chaves, valores e itens retornam listas, ou seja, métodos de iteração que usam laços de repetição funcionam perfeitamente, da mesma forma que funcionam com listas comuns.

## Criando cópias independentes

Para criar uma cópia independente, você pode usar o método `.copy()`, como no exemplo abaixo.

```python
dictionary_1 = {
    'a': 1,
    'b': 2,
    'c': 3,
}
dictionary_2 = dictionary_1.copy()
```

Evite atribuir o valor de um dicionário a outro diretamente quando quiser uma cópia, pois fazer isso gera uma cópia dependente.

## O problema de cópias dependentes

Você pode querer entender qual é o problema de atribuir diretamente o valor de um dicionário á outro para fazer uma cópia, e é uma questão válida. Acontece que quando você faz dessa forma, ao alterar o valor de quaisquer cópias, ou a original, todas as versões daquele dicionário serão alterados também, o que normalmente não é o que se quer quando copiamos um dicionário. Na maioria das vezes você pode querer uma cópia de um dicionário para poder alterá-lo da forma que quiser, justamente sem modificar o original, pois caso modificar o original nao fosse o problema, isso poderia ser feito nele.

## Usando a função `zip()`

A função `zip()` recebe duas listas e cria uma relação de pares entre seus itens. A primeira lista será a lista das chaves, enquanto a segunda, dos valores, observe o exemplo abaixo

```python
list_1 = ['a', 'b', 'c']
list_2 = [1, 2, 3]
print(dict(zip(list_1, list_2))) # Retorna o dicionário {'a': 1, 'b': 2, 'c': 3}
```