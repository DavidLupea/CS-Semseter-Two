#David Lupea
#IntroCS2 pd5
#HW33 -- EndOfFiles
#2018-5-07

def sortnoDuplicates(filename):
    fileIn = open(filename, 'rU')
    
    words = fileIn.read().split()

    numbers = []

    for item in words:
        numbers.append(int(item))

    numbers.sort()
    final = []

    for item in numbers:
        if item not in final:
            final.append(item)

    for item in final:
        print item

    fileIn.close()

    
