from os import listdir
from zipfile import ZipFile

my_list = listdir('input')
print(my_list)


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

n = 50
x = list(divide_chunks(my_list, n))
print(len(x))

for i in range(len(x)):
    fileName = 'sample'+str(i)+'.zip'
    zipObj = ZipFile(fileName, 'w')
    for j in x[i]:
        j = 'input/'+j
        print(j)
        zipObj.write(j)
    zipObj.close()

