a = ['a', 'b', 'c', 'd']
b = [1, 2, 3]


# zip() - merges two for double loop
for i, j in zip(a, b):
    print("%s is %s" %(i, j))