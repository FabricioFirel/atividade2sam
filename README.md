# Controle de Residência

Avaliação 2 - Python Orientação a Objetos (exercício 1).

Programa de console que permite criar uma residência, cadastrar seus cômodos e
calcular a área total construída.

## Como executar

Requer apenas o Python 3 (sem bibliotecas externas):

```bash
python main.py
```

## Estrutura do projeto

| Arquivo | Responsabilidade |
| --- | --- |
| `comodo.py` | Classe `Comodo`: nome e área em metros quadrados. |
| `residencia.py` | Classe `Residencia`: cria e guarda os cômodos, calcula a área total. |
| `main.py` | Menu interativo no console (interface com o usuário). |

## Menu do programa

Ao iniciar, o programa pede o nome e o endereço da residência. Depois disso o
menu oferece:

1. Adicionar cômodo
2. Visualizar cômodos
3. Calcular área total
4. Remover cômodo
0. Encerrar o programa

## Conceitos de orientação a objetos aplicados

- **Composição**: os objetos `Comodo` são criados dentro de
  `Residencia.adicionar_comodo()` e vivem apenas enquanto a residência existir.
  Nenhum cômodo é instanciado fora da classe `Residencia`.
- **Encapsulamento**: todos os atributos são privados (`__nome`, `__area`,
  `__comodos`) e o acesso acontece por propriedades somente leitura.
  O método `listar_comodos()` devolve uma tupla de pares `(nome, área)`, e não
  a lista interna, para que os cômodos não possam ser alterados por fora.
- **Validação dos dados**: o nome não pode ficar em branco, a área precisa ser
  um número maior que zero e não são aceitos dois cômodos com o mesmo nome.
  Os erros são sinalizados com `ValueError` e tratados no menu.
- **Separação de responsabilidades**: as classes cuidam apenas das regras do
  domínio; toda a leitura de dados e exibição na tela fica em `main.py`.
- **Métodos especiais**: `__str__` e `__len__` deixam o uso dos objetos mais
  natural na hora de exibir e contar os cômodos.
