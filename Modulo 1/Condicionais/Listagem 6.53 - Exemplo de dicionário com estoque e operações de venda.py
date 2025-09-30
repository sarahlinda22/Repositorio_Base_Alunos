estoque={"tomate": [ 1000, 2.30],
        "alface": [ 500, 0.45],
			  "batata": [ 2001, 1.20],
			  "feijão": [ 100, 1.50] }

sei_lá_oque = input("Digite o produto: ") 
venda = [ [ sei_lá_oque, int(input("Digite a quantidade: ")) ] ]

total = 0
print("Vendas:\n")
if sei_lá_oque in estoque:
  for operação in venda:
    produto, quantidade = operação 
    preço = estoque[produto][1] 
    custo = preço * quantidade
    print("%12s: %3d x %6.2f = %6.2f" %
		(produto, quantidade,preço,custo))
    estoque[produto][0] -= quantidade 
    total+=custo
else:
   print("Insuficiente!")
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])