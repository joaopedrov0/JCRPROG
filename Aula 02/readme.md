# Anotações da Aula 02 da disciplina JCRPROG

## Tipos na entrada de dados em Python

Todo dado de entrada em Python é armazenado como o tipo "String", portanto, para fazer outras operações, como por exemplo cálculos matemáticos, é necessário fazer a conversão de tipo dessa variável para que ela seja um número ao invés de um texto.

## Casting

Para fazer a conversão dos tipos de variáveis em Python é possível usar o método de Casting para fazer essa conversão.

### int()

Função usada para converter uma variável para o tipo "Inteiro" (int ou integer)

- Se receber um `float`, retorna o número ignorando a sua parte decimal.
- Se receber uma `string`, retorna um erro se tiver algum caractere não numérico, e se todos forem numéricos ele retorna o número. Outro detalhe interessante é que ele não converte um float em uma string para int, ou seja, se tiver uma variável com o seguinte valor: `"3.4"`, ele retorna um erro, e não o valor `3`.
- Se receber um `boolean` ele retorna 1 caso seja `True` ou 0 caso seja `False`.

### float()

Função usada para converter uma variável para o tipo "Float" (ponto flutuante, número com casas decimais)

- Se receber um `int`, retorna o inteiro com uma casa decimal, ainda que esta casa decimal tenha valor 0.
- Se receber um `boolean` ele retorna 1.0 caso seja `True` e 0.0 caso seja `False`.
- Se receber uma `string` ele retorna um erro caso tenha algum caractere não numérico, retorna o número com casas decimais caso seja isso que esteja na string, e caso a string tenha um número sem casas decimais, ele converte para float e acrescenta casas decimais com 0.

### str()

Função usada para converter uma variável para o tipo "String" (texto, cadeia de carateres)

### bool()

Função usada para converter uma variável para o tipo "Boolean" (True ou False)

- Retorna `True` caso receba uma string com conteúdo ou um número diferente de zero.
- Retorna `False` caso receba uma string vazia, 0 inteiro ou 0.0 float.

### Conversões incorretas de tipos

É possível que a tentaiva da conversão de tipos de uma variável retorne um erro, nesse caso, pode ser que o tipo de dado usado na função tenha um conteúdo que não possa ser convertido para o tipo que você está tentando converter.
Veja alguns exemplos de tentativas de conversão que retornam em erro.

```python
int("abacate")
float("abacate")
```

Nessas duas tentativas de conversão, eu tentei transformar uma string que não era um número em um tipo de número inteiro e um outro com casas decimais. Ambos me retornaram erro pois não é possível fazer essa conversão.


## Entrada de dados em Python

Um dos métodos de realizar a entrada de dados em Python é usando a função `input()`. Ao usar essa função, quando o programa se deparar com ela durante a execução, ele vai permitir que o usuário digite um valor qualquer para ser armazenado na variável que está designada no código-fonte.
Como mencionado alguns parágrafos acima, se não for convertido corretamente, qualquer dado que o usuário digitar será armazenado como uma string.