#David Lupea
#IntroCS2 pd5
#HW20 -- searCHandFind
#2018-3-25

#Method 1 (brute force/slow)
def findR_01(ch, word):
    '''Assumes a string, ch of length one and a string.
    It returns the index value of the last instance of ch'''
    last = 0
    if ch not in word:
        return "Not in word"
    for i in range(len(word)):
        if ch == word[i]:
            last = i
    return last

#Method 2 (removing the last letter of the word until the last letter is the desired character)
def findR_02(ch, word):
    '''Assumes a string, ch of length one and a string.
    It returns the index value of the last instance of ch'''
    if ch not in word:
        return "Not in word"
    while ch != word[len(word) - 1]:
        word = word[0:len(word) - 1]
    return len(word) - 1

#Method 3 (Optimized using recursion)    
def findR_03(ch, word):
    '''Assumes a string, ch of length one and a string.
    It returns the index value of the last instance of ch'''
    if ch not in word:
        return "Not in word"
    return len(word) - 1 if ch == word[len(word) - 1] else findR_03(ch, word[0:len(word) - 1])
    
    
    
