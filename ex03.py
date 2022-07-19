import json

with open('dados.json', encoding='utf-8') as dadosJson:
    dados = json.load(dadosJson)

for i in dados[0]:
    print(dados[0]['dia'])