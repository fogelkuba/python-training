address = ["Flat Floor Street", "18", "New York"]
pins = {
    "Mike": 1111,
    "Joe": 2222,
    "Jack": 3333,
}

print(address[0], address[1])

pin = int(input("Enter Your pin: "))

def find_in_file(f):
    myfile = open("sample.txt")
    fruits = myfile.read()
    fruits = fruits.splitlines()
    if f in fruits:
        return "That fruit is in the list."
    else:
        return "No such fruit found!"

if pin in pins.values():
    fruit = input('Enter fruit: ')
    print(find_in_file(fruit))
else:
    print