#Team David + Kevin
#David Lupea
#IntroCS2 pd 5
#HW22 -- LabdayTake 2 WooHoo
#2018-03-27

#Problem 1
def collatz(n, display = False):
    values = [n]                                                        #Creates a list of values with the first one being n
    while values[len(values) - 1] != 1 :                                #Runs this while the last value of the list is not equal to one
        if values[len(values) - 1] % 2 == 0:                            #if the last value is even, it adds half of it to the end of the list
            values += [values[len(values) - 1] / 2]
        else:                                                           #If the value is odd, it adds triple the last value plus one
            values += [values[len(values) - 1] * 3 + 1]
    if display:                                                         #If display is true, it uses the list of values to generate a string
        returned = ""
        for value in values:
            returned = returned + str(value) + " "
        print returned                                                  #It prints the generated string
    return len(values)                                                  #It prints the length of the list (aka, the length of the sequence anyway)

print "collatz(1) yeilds " + u"\u2193"                                  #Special formatting for test cases
print str(collatz(1)) + "\n"

print "collatz(1,True) yeilds " + u"\u2193"
print str(collatz(1,True)) + "\n"

print "collatz(2,True) yeilds " + u"\u2193"
print str(collatz(2,True)) + "\n"

print "collatz(3,True) yeilds " + u"\u2193"
print str(collatz(3,True)) + "\n"

print "collatz(4) yeilds " + u"\u2193"
print str(collatz(4)) + "\n"

print "collatz(5) yeilds " + u"\u2193"
print str(collatz(5)) + "\n"

print "collatz(50, True) yeilds " + u"\u2193"
print str(collatz(50, True)) + "\n"

def longestSeed(start, end, display=False):
    '''Assumes two integers, with display being False unless otherwise specified
    Compares Cthe length of collatz seqences between start and end, comapring them
    and returning the length of the largest sequence'''
    longest = None  
    for i in range(start,end):                                          #Iterates between start and end
        x = collatz(i, display)                                         #If display is true, this is when it prints the collatz sequence for that particular number
        if x > longest:                                                 #Checks to see if the returned value of each collatz is longet than the longest instance of it. 
            longest = i                                                 #If it is, then it sets the longest to the current iteration value
    return longest                                                      #Returns the value of the longest
            


print "longestSeed(1,4) yeilds " + u"\u2193"                            #Special formatting for test cases
print str(longestSeed(1,4)) + "\n"

print "longestSeed(4,6,True) yeilds " + u"\u2193"
print str(longestSeed(4,6,True)) + "\n"

print "longestSeed(10,20, False) yeilds "  + u"\u2193"
print str(longestSeed(10,20)) + "\n"



