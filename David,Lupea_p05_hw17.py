#David Lupea
#IntroCS2 pd5
#HW15 -- WhatFor?
#2018-3-12

#Problem 1
a = int(raw_input("Enter a positive integer: "))
b = int(raw_input("Enter another: "))

a, b = min(a, b), max(a, b)

for i in range(a, b):
    if i % 2 == 1:
        print i

#reverseWord.py
string = raw_input("Enter a string: ")
output = ""

for i in range(len(string)):
    output += string[-1 - i]
print string, "backwards is", output
if output == string[::-1]:
    print "It works"
else:
    print "It does not work"

#Problem 3 using for loops
string = raw_input("Enter word: ")
checked = ""
output = ""

for letter in string:
    if letter in checked:
        output = "The first letter that repeats is " + letter
        break
    else:
        checked += letter

if output == "":
    print "No letters repeat"
else:
    print output

#Problem 3 using while loops
string = raw_input("Enter word: ")
checked = ""
output = ""
iteration = 0

while iteration <= len(string):
    if string[iteration] in checked:
        output = "The first letter that repeats is " + string[iteration]
        break
    else:
        checked += string[iteration]
    iteration += 1

if output == "":
    print "No letters repeat"
else:
    print output



    
