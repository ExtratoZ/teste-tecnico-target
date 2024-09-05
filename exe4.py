sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

valueTotal = sp + rj + mg + es + outros

percentSp = sp / valueTotal * 100
percentRj = rj / valueTotal * 100
percentMg = mg / valueTotal * 100
percentEs = es / valueTotal * 100
percentOutros = outros / valueTotal * 100

print(f'O percentual de cada estado foi respectivamente: \n São Paulo: {(percentSp):.2f} %\n Rio de Janeiro: {(percentRj):.2f} %\n Minas Gerais: {(percentMg):.2f} %\n Espírito Santo: {(percentEs):.2f} %\n Outros: {(percentOutros):.2f} %\n')