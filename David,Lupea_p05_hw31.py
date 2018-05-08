#David Lupea
#IntroCS2 pd5
#HW31 -- MiddleOfFiles
#2018-5-03

def longestword(filename):
    punc = ',.!?;:'
    fileIn = open(filename, 'rU')
    
    words = fileIn.read().split()

    longest = filter((lambda x: len(x) == max(map(lambda x: len(x), words))), words)
    length = max(map(lambda x: len(x), words))

    output = 'The longest word(s) are '
    for item in longest:
        output += item + ' '
    output += 'with a length of ' + str(length)
    
    fileIn.close()
    return output

def longestwordReduce(filename):
    punc = ',.!?;:'
    fileIn = open(filename, 'rU')
    words = fileIn.read().split()
    word = reduce(lambda x,y: x if len(x) > len(y) else y, words)
    output = 'The longest word is  "' + word + '" with a length of ' + str(len(word))  
    fileIn.close()
    return output


def avLen(filename):
    punc = ',.!?;:'
    fileIn = open(filename, 'rU')
    words = fileIn.read().split()
    total = sum(map(lambda x: len(x.strip(punc)), words))
    fileIn.close()
    return (float(total) / len(words))

    
