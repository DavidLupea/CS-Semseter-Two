#Team David + Ling
#David Lupea
#IntroCS2 pd 5
#HW27 -- Labday PigLatin
#2018-04-16

#Part 2
global letters
letters = 'abcdefghijklmnopqrstuvwxyz'

global test_cases
test_cases = ['hello', 'sky', 'stuyvesant', 'computer', 'zzz', 'strong', 'orange', 'apple', 'fly', 'quiet',  'semi-perimeter', 'annoy', 'international']

global tests
tests = ['apple', 'orange', 'strong', 'program', 'zzz', 'you', 'fly', 'unique', 'quiet', 'semi-perimeter']

global phrases
phrases = ['How are you, Bob?', 'Stop YELLING!', 'I have a two-year-old.']

def isvowel(ch):
    '''Assumes ch is a character.
       Returns true if ch is a vowel.'''
    return ch.lower() in 'aeiou'

def testisvowel():
    ''' Tests isvowel.'''
    for letter in letters:
        print 'isvowel("' + letter + '")  ->  ' + str(isvowel(letter)) 

def beginswithvowel(word):
    '''Assumes word is a str.
       Returns true if word begins with a vowel.'''
    return isvowel(word[0])

def testbeginswithvowel():
    ''' Tests begins with vowel'''
    for word in test_cases:
        print 'beginswithvowel("' + word + '")  ->  ' + str(beginswithvowel(word))

def vowelindex(word, ind = 0):
    '''Assumes word is a str.
       Returns the index of the first vowel.
       -1 if not found.'''
    for i in range(ind, len(word)):
        if isvowel(word[i]):
            return i
    return -1

def testvowelindex():
    for word in test_cases:
        print 'vowelindex("' + word + '")  ->  ' + str(vowelindex(word))

def capitalization(word, cap):
    if cap == 1:
        return word.title()
    if cap == 2:
        return word.upper()
    return word.lower()

def singleTranslate(word):
    '''Assumes word is a word of either case, may have punctuation.
       Returns the pig latin translation.
    '''
    words = word.split('-')
    mylist = list()
    for word in words:      
        if word.istitle():
            cap = 1
        elif word.upper() == word:
            cap = 2
        else:
            cap = 3

        word = word.lower()
        end = ''

        for i in range(len(word)):
            if word[i] in ',.!?':
                end += word[i]
                word = word[0:i] + word[i + 1:]
        if vowelindex(word) == -1:
            if 'y' not in word or (word.count('y') == 1 and word[0] == 'y'):
                mylist += [capitalization(word + 'ay' + end, cap)]
                continue
        
        if word[vowelindex(word)] == 'u' and word[vowelindex(word) - 1] == 'q':
            u_index = vowelindex(word)
            mylist += [capitalization(word[vowelindex(word, u_index + 1) : ] + word[0:vowelindex(word, u_index + 1)] + 'ay' + end, cap)]
            continue

        if vowelindex(word) == 0:
            mylist += [capitalization(word + 'way' + end, cap)]
            continue
        if vowelindex(word) > 0 or 'y' in word:
            mylist += [capitalization(word[vowelindex(word):] + word[0:vowelindex(word)] + 'ay' + end, cap)]
            continue
        
    return '-'.join(mylist)

def testsingleTranslate():
     for word in tests:
         print 'singleTranslate("' + word + '")  ->  ' + singleTranslate(word)


def engtopig(text):
    '''Assumes text is a str.
       Returns the pig latin translation of text.'''
    engwords = text.split()
    pigwords = map(singleTranslate,engwords)
    print ' '.join(pigwords)

def testengtopig():
    returned = ''
    for sentence in phrases:
        returned = returned + '\n' + str(engtopig(sentence))

#Part 1
#'cabbage'[::-1]                       -> 'egabbac'
#                                       The [::-1] operator returns the word but backwards
                                            
#'cabbage'[:: 2]                       -> 'cbae'
#                                       The [::2] operator returns the word but with every other number ommitted

#[1,3,5,7][::-2]                       -> [7, 3]
#                                       The [::-2] operator returns every other element in the reverse of a string

#(abs,lambda x: x + 3)[-1](5)          -> 8
#                                       The absolute value of 5 is 5 and 5 + 3 is 8

#type(())                              -> tuple
#                                       Tuples are surrounded by parentheses

#type([])                              -> list
#                                       Lists are surrounded by square brackets

#' '.join(['how', 'are', 'you'])       -> 'how are you'
#                                       The 'x.join(List)' operator joins the items of the list by x(a string)

#list('abc')                           -> ['a', 'b', 'c']
#                                       The list(str) operator creates a list where each item is a letter in str

#(list('abc'))                         -> ('a', 'b', 'c')
#                                       The (list(str)) operator  creates a list where each item is a letter in str, surrounded by parentheses

#map(str.lower,'AbcD')                 -> ['a', 'b', 'c', 'd']
#                                       The map(f,L) function calls function, f on each item of list L. The .lower function returns the lowercase value of each item 

#'324'.isdigit()                       -> True
#                                       The .isdigit method checks to see if a string is a number

#'ab-9'.isalnum()                      -> False
#                                       The .isalnum method checks a string, returning True if all values are numbers, False if they are not

#'abc'.isalpha()                       -> True
#                                       Checks to see if all the values in the string are letters. If so, returns True. Otherwise, False

#'?ab?cd.!?'.strip('.!?')              -> 'ab?cd'
#                                       The x.strip(str) method removes all characters in str from x

#'\thi  '.strip()                      -> 'hi'
#                                       The x.strip(str) method removes all characters in str from x, defaulting to ' '(space values' 

#'Hi'.istitle()                        -> True
#                                       The str.istitle() method returns True if the first letter of the string is capitalized and no other. Returns False otherwise.

#'HI'.istitle()                        -> False
#                                       The str.istitle() method returns True if the first letter of the string is capitalized and no other. Returns False otherwise.

#'see'.find('e')                       -> 1
#                                       The str.find(x) method returns the index value of the first instance of x

#'see'.rfind('e')                      -> 2
#                                       The str.find(x) method returns the index value of the first instance of x

#'see'.find('z')                       -> -1
#                                       The str.find(x) method returns the index value of the first instance of x
