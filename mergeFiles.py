import datetime, os

def mergeFiles(path = './filesDir/', baseName = 'file'):
    date = str(datetime.datetime.now().strftime("%Y-%M-%d-%H-%M-%s"))
    print(date)

    mergedFile = open(path + date + ".txt", 'a')

    for fileName in os.listdir(path):
        if baseName in fileName:
            print('Processing:', fileName)
            content = open(path + fileName).read()
            mergedFile.write(content + '\n')
    mergedFile.close()


mergeFiles()
