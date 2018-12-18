import pandas

csv = pandas.read_csv('./supermarkets.csv', header=None)
print('CSV FILE: ')
print(csv)

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
# xls = pandas.read_excel('./supermarkets.xlsx')
# print(xls)