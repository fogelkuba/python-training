numbers = [1, 2, 3]
mfile = open('openLoop.txt', 'w')
for n in numbers:
    mfile.write(str(n) + '\n')
mfile.close()
