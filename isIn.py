def isIn(x,y):
    '''Takes in two strings.
    Returns True if either string is a substring of the other.'''
    return x in y or y in x

#Function call
print isIn("at", "cat")
print isIn("reverse", "erse")
print isIn("crow", "cow")
