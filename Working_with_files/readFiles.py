#Read file, Format is one name per line
#Print one name per line

filehandle = open('kids.txt', 'r')          #r = read
#File objects are iterable

for line in filehandle:
    print line[:-1]


filehandle.close()
