import json

with open("dados.json") as faturamento:
    dados = json.load(faturamento)

# print(dados)

maxDay = -1
maxValue = -1
minDay = -1
minValue = -1
dayFat = 0
fatTotal = 0

for i in dados:
    fatTotal += i['valor']
    if i['valor'] > 0 :
        dayFat += 1
    if minDay == -1 and i['valor'] > 0:
        minValue = i['valor']
        minDay = i['dia']
    elif minDay != -1 and i['valor'] <= minValue and i['valor'] > 0:
        minValue = i['valor']
        minDay = i['dia']
    if maxDay == -1 and i['valor'] > 0:
        maxValue = i['valor']
        maxDay = i['dia']
    elif maxDay != -1 and i['valor'] >= maxValue and i['valor'] > 0:
        maxValue = i['valor']
        maxDay = i['dia']

print(f'o faturamento mínimo foi {minValue}\n, o faturamento máximo foi {maxValue}\n e a média de faturamento mensal foi {(fatTotal / dayFat):.4f}.' )