#David Lupea
#IntroCS2 pd5
#HW12 -- CoincidentallyPalindromeIsNotAPalindrome
#2018-3-5

string = raw_input("Enter a string: ") #Takes in the input

if string[ : :-1] == string: #Checks if the reverse of the string is the same as the regular string and displays messages accordingly
    print "String is a plaindrome"
else:
    print "String is not a plaoindrome"
