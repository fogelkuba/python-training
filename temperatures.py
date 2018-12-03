temperatures = [10, -20, -289, 100]

def c_to_f(c):
    if  c< -273.15:
        return 'That temperature makes no sense!'
    else:
        f = c * 9/5 + 32
        return f


for t in temperatures:
    res = c_to_f(t)
    mytemps = open('temps.txt', 'a')
    mytemps.write('\n' + 'C:' + str(t) + ' F:' + str(res))
    mytemps.close()
    print(t, res)


    