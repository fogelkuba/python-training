correct_pass = 'python123'
name = input('Your name: ')
password = input("Enter password: ")

while correct_pass != password:
    password = input('Error, try again: ')

print('Hi %s, you are logged in' % name)