#David Lupea
#IntroCS2 pd5
#HW 8 -- Script Writing
#2018-02-27

#largest_odd.py
num1 = int(raw_input("Enter an integer: "))                 #Takes in the inputs
num2 = int(raw_input("Enter another integer: "))
num3 = int(raw_input("Enter a final integer: "))

if num1 % 2 == 1 or num2 % 2 == 1 or num3 % 2 == 1:         #Checks to see if all of them are even. If they are, it tells you none of them were odd
    if num1 % 2 == 0:                                       #Checks each number and if it is even sets it to None. This makes it so miniscule it is not accounted for in determining 
        num1 = None                                         #the maximum value
    if num2 % 2 == 0:
        num2 = None
    if num3 % 2 == 0:
        num3 = None
    print max(num1, num2, num3)                             #Prints the maximum value of the three numbers
else:
    print "None of the numbers were odd"


#sort3.py
n1 = float(raw_input("Enter a number: ")                    #Takes in the inputs
n2 = float(raw_input("Enter another number: "))
n3 = float(raw_input("Enter a final number: "))

#With conditionals
if n1 >= n2 and n1 >= n3:                                   #Checks if n1 is the biggest number
    if n2 >= n3:                                            #Chechs which number is the second biggest between n2 and n3
        print n3, n2, n1
    else:
       print n2, n3, n1
elif n2 >= n1 and n2 >= n3:                                 #Checks if n2 is the biggest number
    if n1 >= n3:                                            #Chechs which number is the second biggest between n1 and n3
        print n3, n1, n2
    else:
        print n1, n3, n2
elif n3 >= n1 and n3 >= n2:                                 #Checks if n3 is the biggest number
    if n1 >= n2:                                            #Chechs which number is the second biggest between n1 and n2
        print n2, n1, n3
    else:
        print n1, n2, n3


#Without conditionals
minimum = min(n1, n2, n3)
middle = (n1 + n2 + n3 - max(n1, n2, n3) - min(n1, n2, n3))
maximum = max(n1, n2, n3)

print minimum, middle, maximum
