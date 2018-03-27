#David Lupea and Kevin Mesta
#avid Lupea
#IntroCS2 pd5
#HW16 --Labwork2
#2018-3-11

import random

#Problem 1
w = int(raw_input("Enter the width: ")) #asks user to input a width
h = int(raw_input("Enter the length: ")) #asks the user to input a length

print "\n" + str(w) + " x " + str(h) + " rectangle" #Specifes the dimensions of the rectangle

iteration = 1 #Sets up how many times the loop will run

while iteration <= h: #While loop will run as long as
    print "*" * w #print * by a number that is determined by the width
    
    iteration += 1 #sets the iternation to the iternation + 1


#Problem 2
length = int(raw_input("enter a positive #: "))

iteration = 1 #sets iternatio to 1

while iteration <= length: #each line of the rectangle will be dteremined by how big the inputed length value is
    if iteration % 2 == 1: #If the iternation is odd the following happens
        output = "" #empty string to add the following charcaters to
        width = 0 #this is how wide the rectangle is
        while width < length: # only happens as long as the the width is less than the inputed value
            if width % 2 == 1: #if the width is odd it will add "+"
                output += "+" #adds the plus sign to the string
            else:
                output += "-" #adds the - sign to the string
            width += 1 #regardless adds the 1 to the width
        print output      
    else: #this section is identical to the part above except that the pattern is inverted
        output = ""
        width = 0
        while width < length:
            if width % 2 == 1:
                output += "-"
            else:
                output += "+"
            width += 1
        print output  
    iteration += 1 #every time a line is printed it sets the iternation to +1


#Problem 3
flipCoin = lambda : random.choice(['H','T']) #function to prit either H or T

flips = int(raw_input("Enter # of trials: ")) #ints the value that the user inputs

output = "" #empty string to add the eniter sequence of heads and tails
prev = "" #this is the prvious string
iterate = 1 #the number os iternations

while iterate <= flips: #loop will only run for the number of trials you put in
    result = flipCoin() #sets the result to the result of the coin flip
    output += result #adds either h or t to the empty string
    
    iterate += 1 #sets the iternation to +1
print output #prints the entire string of hs and ts

iteration = 1
LongestTRow = 0 #keeps track how long the tails streak is
LongestHRow = 0 #keeps track how long the heads streak is
CurrentRow = 1 #the current streak of either hs or ts

while iteration < len(output): #only occurs depending how long the string is
    if output[iteration] == "H": #cheks if the element at a certain index is H
        if output[iteration] == output[iteration - 1]: #checks if the letter before it is also H
            CurrentRow += 1 #sets the row to +1
        else:
            CurrentRow = 1 #if they are not sequentical the streak breaks and becomes 1 
        if CurrentRow > LongestHRow: #trhen checks i the current row is longer than the longest row
            LongestHRow = CurrentRow #if true sets the longest row to the row you just got
    else: #this entire section is the same as above but just with tails instead of hedas
        if output[iteration] == output[iteration - 1]:
            CurrentRow += 1
        else:
            CurrentRow = 1
        if CurrentRow > LongestTRow:
            LongestTRow = CurrentRow        
    iteration += 1 #sets the iternation to +1

print "The longest sequence of H: " + str(LongestHRow) #these two print statments give back the longest streak of tails and heads
print "The longest sequence of T: " + str(LongestTRow)












    







    
