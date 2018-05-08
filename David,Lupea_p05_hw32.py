#David Lupea
#IntroCS2 pd5
#HW32 -- MiddleOfFilesTake 2
#2018-5-06


punc = '.,;:!?'
#Question 1
word = raw_input("Enter a word: ")

def countTimes(filename, word):
    fileIn = open(filename, 'rU')
    
    words = fileIn.read().split()

    count = 0
    
    for item in words:
        
        if word.lower() == item.strip(punc).lower():
            count += 1

    fileIn.close()
    
    return count


#Question 2
def deleteSpaces(filename):
    
    fileIn = open(filename, 'rU')

    text = ''
    for line in fileIn:
        text += ''.join(line.split()) + '\n'

    fileIn.close()

    fileOut = open('output.txt', 'w')

    fileOut.write(text)

    fileOut.close()


#Question 3
def scrambleFile(filename):
    
    fileIn = open(filename, 'rU')

    text = ''
    for line in fileIn:
        text += '*'.join(line.lower().replace('a', 'u').replace('e', 'i').split()) + '\n'

    fileIn.close()

    fileOut = open('scrambled.txt', 'w')

    fileOut.write(text)

    fileOut.close()
