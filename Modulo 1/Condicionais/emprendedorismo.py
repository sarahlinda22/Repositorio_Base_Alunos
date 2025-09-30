estoque={"blush":[4,2.50],
         "batom":[3,5.90],
         "contono":[2,6.80],
         "base":[6,12.75],
         "corretivo":[15,8.90],
         "iluminador":[10,3.68],
         "po solto":[17,28.50],
         "po compacto":[17,30.99],
         "sombra":[13,6.99],
         "serum":[20,15.00],
         "hidrtante":[60,13.00],
         "rimel":[20,10.99],
         "primer":[39,18.65],
         "cilios falso":[25,8.50],
         "gloss":[20,15.00],
         "blindagem":[30,12.60],
         "demaquilante":[50,6.99],
         "bruma":[37,12.69],
         "lapis de boca":[25,10.00],
         "lapis de olho":[30,3.50]}
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