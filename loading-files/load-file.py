import pandas

# csv = pandas.read_csv('./supermarkets.csv', header=None)
csv = pandas.read_csv('./supermarkets.csv')
csv = csv.set_index('ID')
print('CSV FILE: ')
print(csv.shape)
print(csv)


# print(csv.loc["735 Dolores St":"551 Alvarado St":"State"])
# print(csv.loc["551 Alvarado St":"ID"])


# list = list(csv.loc[:,'City'])
# print(list)


# print(csv.iloc[1:3, 1:3])
# print(csv.iloc[1, 2:8])


# print(csv.ix[3, 'Name'])

print(csv.T)

# print('================================')
#
# txt = pandas.read_csv('./supermarkets-commas.txt')
# print(txt)
#
# print('================================')
#
# json = pandas.read_json('./supermarkets.json')
# print(json)
#
# print('================================')
#
# xls = pandas.read_excel('./supermarkets.xlsx', sheetname=0)
# print(xls)