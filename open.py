myfile = open('sample.txt')
print(type(myfile))
content = myfile.read()

print(dir(myfile))

print(myfile.__sizeof__())

print(content)
print(type(content))
myfile.close()
