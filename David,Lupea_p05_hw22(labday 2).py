#Team David + Kevin
#Kevin Mesta
#IntroCS2 pd 5
#HW22 -- Labday WooHoo
#2018-03-27


#Problem 1
def find(sub, s, start = 0):
    '''Assume both sub and s are strings and start is an int.
    Return the lowest index in s where substring sub is found,
    such that sub is contained within S[start:].  Optional
    argument start is interpreted as in slice notation.
    Return -1 on failure.'''

    if sub not in s:                                                    #Immediatley checks to see if the character is in it. If it is not, it returns -1
        return -1
    place = 0                                                           #Starts with the place value being 0
    for x in range(len(s[start:])):                                     #Iterates through the string starting at the start point
        if sub == s[start + x:start +x + len(sub)]:                     #Checks each group of letters, seeing if the group is equal to the substring
            place = place + start + x                                   #If it is, it adds the start value and the current iteration value to place and breaks out of the for loop
            break                                                       #             ^This is equal to the index value of the first character of the substring in the string  
    return place                                                        #Returns the place value

print find('at', 'cat')                                                 #Test cases
print find('is', 'mississippi', 2)
print find('z', 'python') 

   
#Problem 2(without recursion)
def fib(n, first = 0, second = 1):
    '''Assumes 3 integers. Returns the nth value of the
    fibonacci sequence, given the first and second values.
    The default values for first and second are 0 and 1,
    respectively''' 
    values = [first, second]                                            #Creates a list called values and sets the first two values in it to first and second
    if n == 1:                                                          #Checks to see if n is one or two, in  which case it would return that
        return values[0]
    if n == 2:
        return values[1]
    for i in range(2,n + 1):                                            #Iterates through the list between two and n+1,
        values += [values[i-1] + values[i-2]]                           #each time adding a value to the list, equal to the sun of the last two values
    return values[n - 1]                                                #Returns the nth value of the sequence
    
print fib(1)                                                            #Test cases
print fib(1,2,3)
print fib(2,2,3)
print fib(6,first = 1)
print fib(10,second = 2)


#Problem 2(with recursion)
def alt_fib(n, first = 0, second = 1):
    '''Assumes 3 integers. Returns the nth value of the
    fibonacci sequence, given the first and second values.
    The default values for first and second are 0 and 1,
    respectively'''
    return first if n == 1 else alt_fib(n - 1, second, first + second)      #It returns the first value if n is equal to one. Otherwise, it runs itself but with n - 1 instead of n,
                                                                            #the previous second value as the first value and the sum of the previous first and second values as the
                                                                            #second value. 
    
print alt_fib(1)                                                            #Test cases
print alt_fib(1,2,3)
print alt_fib(2,2,3)
print alt_fib(6,first = 1)
print alt_fib(10,second = 2)








































    

