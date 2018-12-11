def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Nie ma takiego dzielenia !1'
    # except TypeError:
    #     return 'Podaj argument'


print(divide(1,0))
print(divide(1))
# print('end')