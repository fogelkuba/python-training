import datetime, os

def mergeFiles(path = './filesDir/'):
    date = str(datetime.datetime.now().strftime("%Y-%M-%d-%H-%M-%s"))
    print(date)

    file = open(path + date + ".txt", 'a')

    for filename in os.listdir(path):
        print(filename)


mergeFiles()
