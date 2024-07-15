# Funções

## Por que usar funções?

Funções são uma forma de separar o código em partes reutilizáveis, isto é, criar trechos de código que podem ser executados mais de uma vez ao longo do código sem que você precise fazer um laço de repetição ou escrever novamente o mesmo código.

Funções são excelentes para dividir problemas complexos em partes menores, se concentrando na solução de pequenos problemas que aos poucos resolvem problemas maiores.

Além disso, funções permitem uma abstração maior do código, tornando códigos grandes mais legíveis e fáceis de compreender, permitindo construir coisas "maiores" com mais facilidade, pelo motivo apresentado anteriormente de dividir problemas complexos em partes menores.

## Definindo uma função

Para definir uma função em Python se usa a seguinte sintaxe:

```
def <nome-da-função>(<argumentos>):
    <bloco código a ser executado>
... (continuação do código fora do escopo da função)
```

Assim como em condicionais, laços de repetição, e outras estruturas que envolvem um bloco de código dentro de algum escopo menor, o escopo da função é definido pela indentação do código, que é o espaçamento no canto lateral do código.

Observe um exemplo simples de uma função:

```python
def printMessage():
    print("My first function")
print("Hello, world!")
printMessage()
```

No exemplo anterior, nós definimos uma função chamada `printMessage` que, quando chamada, imprime na tela a mensagem `"My first function!"`. Em seguida exibimos a mensagem `"Hello, world!"` na tela e depois chamamos a função com o nome dela seguido de parênteses fechado, dessa forma: `printMessage()`.

Nesse exemplo, como a função foi chamada apenas depois do "Hello, world!", apesar do `print("My first function")` estar escrito antes do `print("Hello, world!")`, esta segunda mensagem foi exibida somente depois da primeira, pois o conteúdo dentro do bloco do escopo da função somente será executado se e quando a função for chamada.

Além disso, é importante destacar que em python as funções precisam ser declaradas **antes** de serem chamadas, o que nem sempre é verdade em outras linguagens.

Para finalizar, funções podem ser redefinidas, ou seja, você pode atualizar uma função redefinindo-a, da mesma forma que você faria com uma variável porém usando a sintaxe adequada. (def...)

## Entendendo o conceito de Escopo

Em programação, o conceito de escopo de uma variável é o "lugar" do programa onde a variável é acessível.

Esse conceito é importante para que você possa usar variáveis dentro de uma função que não afetem o exterior, evitando conflitos.

Essa separação de escopos criam o conceito de **variável local**, que é uma variável que só está disponível no escopo da função, isto é, dentro do bloco de código da função.

Em contraste com isso, temos também **variáveis globais**, que são variáveis acessíveis em qualquer lugar, tanto fora quanto dentro de qualquer função.

### Redefinindo o valor de uma variável dentro de uma função

Como dito anteriormente, variáveis locais estão apenas acessíveis dentro do escopo da função, enquanto variáveis globais são acessíveis de qualquer lugar. Se você declarar uma variável de **mesmo nome** que uma variável de escopo **global** dentro de uma variável de escopo **local**, a função sobrescreverá o valor da variável global "por cima" como uma variável local, porém apenas no escopo da função.

## Argumentos

Argumentos são valores passados na hora de chamar a função para que ela use o valor passado no bloco de código.

Observe o exemplo abaixo, que segue a mesma sintaxe já apresentada anteriormente:

```python
def printSum(x, y):
    print(x + y)

printSum(3, 4) # Retorna 7
```

### Listas

Diferente de variáveis simples, a passagem de listas como argumento de funções é feita pelo método de **passagem por valor**, isso significa que quando você passa uma lista como argumento, você está passando apenas o endereço de uma lista ao invés do valor da lista, como seria feito caso fosse uma variável simples, (strings, números, etc.).

Na prática isso altera a forma que você trata listas dentro de funções, caso você queira manipular uma lista dentro de uma função sem alterar o valor original, você precisa realizar uma **cópia explícita**, ou seja, **independente**.

## Retorno

O retorno, ou `return` faz com que a função encerre, retornando ou não um valor para o local onde foi chamada.

Por exemplo, caso você passe como argumento da função `print()` umachamada de função que retorna uma string, a função chamada vai passar a string para o local onde foi chamada, ou seja, como argumento da função `print()`, e ela exibirá o conteúdo da string.

## Função `main()`

Existe uma prática comum de utilizar uma função `main()` para englobar todo o código (exceto definições de funções). A utilidade disso é ter um código mais organizado, além de não ter problema com ordem de definição das funções, já que estão sendo definidas fora do escopo da função `main()`

