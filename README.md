# 📦 Sistema de Gerenciamento de Estoque e Pedidos

## Descrição

Este projeto consiste em um sistema simples de gerenciamento de estoque e registro de pedidos, desenvolvido em **Python**. O programa funciona por meio de um menu interativo no terminal, permitindo cadastrar produtos, consultar o estoque, realizar vendas e registrar pedidos.

O objetivo do projeto é praticar conceitos fundamentais da linguagem Python, como:

- Listas;
- Dicionários;
- Funções;
- Estruturas condicionais;
- Estruturas de repetição;
- Manipulação de datas com o módulo `datetime`.

---

## Funcionalidades

- ✅ Cadastro de produtos no estoque;
- ✅ Visualização do estoque;
- ✅ Verificação da disponibilidade de produtos;
- ✅ Criação de pedidos;
- ✅ Atualização automática do estoque;
- ✅ Cálculo do valor total da compra;
- ✅ Pagamento por cartão ou dinheiro;
- ✅ Cálculo do troco;
- ✅ Registro de pedidos realizados;
- ✅ Consulta do histórico de pedidos.

---

## Estrutura dos Dados

### Estoque

Cada produto é armazenado como uma lista no seguinte formato:

```python
[
    nome,
    preco,
    quantidade,
    data_de_cadastro
]
```

Todos os produtos são armazenados na lista:

```python
estoque = []
```

---

### Pedido

Cada item do pedido possui a seguinte estrutura:

```python
[
    nome_do_produto,
    quantidade,
    data_do_pedido
]
```

---

### Pedidos registrados

Cada pedido é armazenado como um dicionário:

```python
{
    "Itens": [...],
    "Data": ...,
    "Total": ...,
    "Forma de pagamento": ...,
    "Troco": ...
}
```

Todos os pedidos ficam armazenados em:

```python
pedidos_registrados = {}
```

---

## Menu Principal

Ao executar o programa, o usuário poderá escolher uma das seguintes opções:

```text
1 - Ver o estoque
2 - Criar o pedido
3 - Adicionar itens no estoque
4 - Mostrar todos os pedidos
5 - Sair
```

---

## Funcionamento

### 1. Cadastro de produtos

O usuário informa:

- Nome;
- Preço;
- Quantidade disponível.

O sistema registra automaticamente a data e o horário do cadastro.

---

### 2. Visualização do estoque

Exibe todos os produtos cadastrados com:

- Nome;
- Preço;
- Quantidade disponível;
- Data de cadastro.

Caso o estoque esteja vazio, será exibida a mensagem:

```text
Estoque vazio
```

---

### 3. Criação de pedidos

Durante a criação do pedido, o sistema:

- Exibe o estoque disponível;
- Verifica se o produto existe;
- Confere a quantidade disponível;
- Permite adicionar vários produtos ao mesmo pedido;
- Atualiza automaticamente o estoque após a confirmação.

Caso o produto não exista ou esteja indisponível, uma mensagem é exibida ao usuário.

---

### 4. Pagamento

Após finalizar o pedido, o sistema calcula automaticamente o valor total da compra.

São aceitas duas formas de pagamento:

**Cartão**

- Finaliza a compra sem troco.

**Dinheiro**

- Solicita o valor recebido;
- Calcula o troco automaticamente.

---

### 5. Histórico de pedidos

Cada pedido registrado contém:

- Produtos comprados;
- Quantidade de cada item;
- Data da compra;
- Valor total;
- Forma de pagamento;
- Troco (quando aplicável).

Esses pedidos podem ser consultados posteriormente pela opção **Mostrar todos os pedidos**.

---

## Tecnologias Utilizadas

- Python 3
- Módulo `datetime`

---

## Conceitos Aplicados

Este projeto utiliza diversos conceitos introdutórios de programação:

- Modularização por funções;
- Manipulação de listas;
- Manipulação de dicionários;
- Estruturas condicionais (`if`, `elif`, `else`);
- Estruturas de repetição (`for` e `while`);
- Entrada e saída de dados;
- Manipulação de datas e horários;
- Atualização dinâmica de dados.

---

## Exemplo de execução

```text
Olá! Qual ação deseja realizar?

1 - Ver o estoque
2 - Criar o pedido
3 - Adicionar itens no estoque
4 - Mostrar todos os pedidos
5 - Sair
```

---

## Possíveis Melhorias

Algumas funcionalidades que podem ser adicionadas futuramente:

- Persistência dos dados em arquivos (`JSON` ou `CSV`);
- Utilização de banco de dados;
- Cadastro de clientes;
- Exclusão e edição de produtos;
- Busca de produtos por nome;
- Interface gráfica;
- Relatórios de vendas;
- Controle de estoque mínimo;
- Estatísticas de vendas.

---

## Autor

Projeto desenvolvido como exercício de programação em Python para praticar lógica de programação, manipulação de listas, dicionários, funções e controle de estoque.
