import datetime, os
print(str(datetime.datetime.now().strftime("%y-%m-%d-%H-%M")))


def mergeFiles(path = './filesDir'):

    for filename in os.listdir(path):
        print(filename)