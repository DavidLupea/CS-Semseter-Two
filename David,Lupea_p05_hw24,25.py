#David Lupea
#IntroCS2 pd5
#HW24,25 -- Caesar Encryotion
#2018-4-10

#Part one
global LETTERS
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Part two
word = raw_input("Enter some plaintext: ").upper()

#Part three
def find(char, text):
    """Assumes two strings, char and word.
    Returns the first instance of char in word."""
    for i in range(len(text)):
        if text[i] == char:
            return i
    return -1

#Part four
def testFind():
    for LETTER in LETTERS:
        print 'find(' + LETTER + ', "STUYVESANT") : ' + str(find(LETTER, "STUYVESANT"))

#Part five
def encryptOne(char):
    """Assumes a one character string, consisting of a letter.
    Returns the Caesar cipher of that letter."""
    return LETTERS[(find(char.upper(), LETTERS) + 3) % 26]

#Part six
def testEncryptOne():
    for LETTER in LETTERS:
        print 'encryptOne(' + LETTER + ') : ' + encryptOne(LETTER)

#Part seven
def encryptWord(plaintext):
    """Assumes a string in plaintext.
    Encrypts it using a Caesar Ciper"""
    returned = ''
    for letter in plaintext:
        returned += encryptOne(letter)
    return returned      

#Part eight
tests = ['STUYVESANT', 'HELLO', 'COMPUTER', 'CAESAR', 'FISH', 'PUPPY', 'FUN', 'WATER', 'MATH', 'SCIENCE']
def testEncryptWord():
    for word in tests:
        print 'encryptWord(' + word + ') : ' + encryptWord(word)
    

#Part nine
def decryptWord(ciphertext):
    returned = ''
    for letter in ciphertext:
        returned += LETTERS[(find(letter.upper(), LETTERS) - 3)]
    return returned

#Part ten
tests = ['STUYVESANT', 'HELLO', 'COMPUTER', 'CAESAR', 'FISH', 'PUPPY', 'FUN', 'WATER', 'MATH', 'SCIENCE']
def testDecrypt():
    for word in tests:
        print 'decrypt("' + encryptWord(word) + '") : ' + decryptWord(encryptWord(word))

#Part eleven
def encryptRot13(ciphertext):
    return encryptAny(ciphertext, 13)

def decryptRot13(ciphertext):
    return decryptAny(ciphertext, 13)

#Part twelve
tests = ['STUYVESANT', 'HELLO', 'COMPUTER', 'CAESAR', 'FISH', 'PUPPY', 'FUN', 'WATER', 'MATH', 'SCIENCE']

def testEncryptRot13():
    for word in tests:
        print 'encryptRot13("' + word + '") : ' + encryptRot13(word)

def testDecryptRot13():
    for word in tests:
        print 'decryptRot13("' + encryptRot13(word) + '") : ' + decryptRot13(encryptRot13(word)) 

#Part thirteen
def encryptAny(ciphertext, rot = 3):
    returned = ''
    for char in ciphertext:
        returned += LETTERS[(find(char.upper(), LETTERS) + rot) % 26]
    return returned

def decryptAny(ciphertext, rot = 3):
    returned = ''
    for char in ciphertext:
        returned += LETTERS[(find(char.upper(), LETTERS) - rot) % 26]
    return returned



