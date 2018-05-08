#Mimics the bash command wc
#   $wc filename -> number of lines, number of words, number of characters, filename

#filename
filename = 'Tom_Sawyer_Preface.txt'

#create a dile object to read from
fileIn = open(filename, 'r')

#Initialize variables
numlines, numwords, numchars = 0,0,0

for line in fileIn:
    numlines += 1
    numchars += len(line)
    numwords += len(line.split())

#Print resullts
print numlines, numwords, numchars, filename

#Close connection
fileIn.close()
