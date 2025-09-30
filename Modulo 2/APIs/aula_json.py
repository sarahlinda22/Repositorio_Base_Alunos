import json
# uma string no formato de json
dados_json='{"nome":"sarah","idade":15,"cidade":"santana de parnaiba"}'

# convertende a dtring json em um dicionario python

dados_python = json.loads(dados_json)


# agora voce~pode acessar os dados como um dicionario

print(dados_python["nome"])# saioa de string
print(dados_python["idade"])# saida de inteiro


pythonValue={'iscat':True,'miceCaugt':0,'name': 'loki', 'raça':'yorkshire', 'genero':'masculino','peso':'4 quilos', 'caracteristica':'carinhoso','pelo':'medio','cor':'preto e marrom','é cachorro?':'true or false','comida preferida':'banana','come o que?':'ração'}

string0fJsonData = json.dumps(pythonValue)
print(string0fJsonData)