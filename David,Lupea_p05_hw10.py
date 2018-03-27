#David Lupea
#IntroCS2 pd5
#HW10 -- LetsStringItAllTogether
#2018-3-1


#strDemo.py
String = raw_input("Type in a string:  ")                                                       #Takes in the user's raw input

print "The length is:                                       ", len(String)                      #Prints the length of the string
print "The first character is:                              ", String[0]                        #Prints the first character(index value 0) of the string
print "The last character is:                               ", String[len(String) - 1]          #Prints the last character(index value of length - 1) of the string
print "The middle character is:                             ", String[len(String) / 2]          #Prints the middlle character(index value of length / 2) of the string
print "The first half of the string is:                     ", String[0: len(String) / 2]       #Prints the first half of the string(index value 0 to index value length / 2, the middle value)
print "The last half of the string is:                      ", String[len(String) / 2 : ]       #Prints the second half of the string(index value length / 2, the middle caracter onward
print "The double of the string is:                         ", (String * 2)                     #Prints the string repeated 2 times
print "The 'aaa' and 'zzz'-ified version of the string is:  ", ("aaa" + String + "zzz")         #Prints the string but with "aaa" at the beginning and "zzz" at the end. Concotonates "aaa" and "zzz"

