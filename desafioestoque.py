from datetime import datetime

estoque = {}
historico_vendas = [] # New list to store sales history

def[] consultar_estoque(produto):
    return produto in estoque

repita = True
menu = ["cadastro", "consulta", "exibir estoque", "venda", "historico de vendas"]

while repita:
  print("\n Menu:")
  for i in menu:
    print(i)
  processo = input("Digite uma das opções ou 'fim' para encerrar: ")

  if processo.lower() == "cadastro":
    cadastro = True # Reset flag to allow re-entry into cadastro mode
    while cadastro:
      nome_prod = input("\n Digite o nome do produto ou 'finalizar' para encerrar o cadastro: ")
      if nome_prod.lower() == 'finalizar':
        cadastro = False
      elif consultar_estoque(nome_prod):
        print("\n Produto já cadastrado.")
      else:
        try:
            preco_prod = float(input("Digite o preço do produto: "))
            estoque_prod = int(input("Digite a quantidade em estoque do produto: "))
            estoque[nome_prod] = [preco_prod, estoque_prod]
            print("\n Produto cadastrado.")
        except ValueError:
            print("Entrada inválida para preço ou quantidade. Por favor, digite um número.")

  elif processo.lower() == "consulta":
    consulta = True # Reset flag to allow re-entry into consulta mode
    while consulta:
      consulta_prod = input("Digite o produto para consulta ou 'fim': ")
      if consulta_prod.lower() == "fim":
        consulta = False
      else:
        if consultar_estoque(consulta_prod): # Corrected function call
          print (f"\n {consulta_prod} - Preço: R${estoque[consulta_prod][0]:.2f} - Qtd: {estoque[consulta_prod][1]}")
        else:
          print("\n Produto não encontrado.")

  elif processo.lower() == "venda":
    venda = True # Reset flag to allow re-entry into venda mode
    produtos_da_venda_atual = [] # List to hold products for the current sale
    total_venda_atual = 0.0 # Total value for the current sale
    print("\n --- Iniciar Nova Venda ---")
    while venda:
      nome_prod = input("Digite o nome do produto ou 'finalizar' para encerrar a venda: ")
      if nome_prod.lower() == 'finalizar':
        if produtos_da_venda_atual: # Only record sale if items were added
            historico_vendas.append({
                'data_hora': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # Format datetime
                'valor_total': total_venda_atual,
                'produtos': produtos_da_venda_atual
            })
            print(f"\n Venda registrada! Valor total: R$ {total_venda_atual:.2f}")
        else:
            print("\n Nenhuma venda realizada nesta sessão.")
        venda = False # Exit current sale session
      elif consultar_estoque(nome_prod):
        try:
            qtd_venda = int(input("Digite a quantidade desejada do produto: "))
            if qtd_venda <= 0:
                print("Quantidade deve ser positiva.")
                continue

            if qtd_venda > estoque[nome_prod][1]:
              print(f"Erro - quantidade disponível: {estoque[nome_prod][1]}")
            else:
              preco_unitario = estoque[nome_prod][0]
              valor_item = qtd_venda * preco_unitario
              estoque[nome_prod][1] -= qtd_venda # Update stock
              total_venda_atual += valor_item # Add to current sale's total
              produtos_da_venda_atual.append({
                  'nome': nome_prod,
                  'quantidade': qtd_venda,
                  'preco_unitario': preco_unitario,
                  'valor_total_item': valor_item
              })
              print(f"Produto '{nome_prod}' adicionado ao carrinho. Estoque restante: {estoque[nome_prod][1]}")
              print(f"Total da venda atual: R$ {total_venda_atual:.2f}")
        except ValueError:
            print("Entrada inválida para quantidade. Por favor, digite um número inteiro.")
      else:
        print("Produto indisponível no estoque.")

  elif processo.lower() == "exibir estoque":
    print("\n Estoque Atual:")
    if not estoque:
        print("Estoque vazio.")
    else:
        for produto, dados in estoque.items():
            print(f"{produto} - Preço: R${dados[0]:.2f} - Qtd: {dados[1]}")

  elif processo.lower() == "historico de vendas": # New menu option to display sales history
    print("\n Histórico de Vendas:")
    if not historico_vendas:
        print("Nenhuma venda registrada ainda.")
    else:
        for i, venda_item in enumerate(historico_vendas):
            print(f"\n --- Venda {i+1} ---")
            print(f"Data/Hora: {venda_item['data_hora']}")
            print(f"Valor Total: R$ {venda_item['valor_total']:.2f}")
            print("Produtos Vendidos:")
            for produto_vendido in venda_item['produtos']:
                print(f"  - {produto_vendido['nome']} (x{produto_vendido['quantidade']}) "
                      f"@ R${produto_vendido['preco_unitario']:.2f} cada = R${produto_vendido['valor_total_item']:.2f}")

  elif processo.lower() == 'fim':
    print("\n Processo encerrado.")
    repita = False
  else:
    print("\n Opção indisponível. Por favor, escolha uma das opções do menu.")
