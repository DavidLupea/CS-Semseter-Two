#David Lupea
#IntroCS2 pd5
#HW14 -- WhileAllThisIsHappening
#2018-3-7

#countDown.py
number = int(raw_input("Enter a positive integer: "))

if number > 0:
    while number > 0:
        print number
        number = number - 1
    print "Blast off"
else:
    print "Please type in a positive integer"
    

#largestOdd10.py
iterations = 0
largest_odd = None

while iterations < 10:
    number = int(raw_input("Type in an integer: "))
    if number % 2 == 1 and number > largest_odd:
        largest_odd = number
    iterations += 1

if largest_odd == None:
    print "None of the numbers were odd"
else:
    print "The largest odd number is", largest_odd


#allVowels.py
string = raw_input("Enter a word: ")
iterations = len(string)

cur_iteration = 0

statement = "The vowels are:"
while cur_iteration < iterations:
    letter = string[cur_iteration]
    if letter in "aeiouAEIOU":
        statement = statement + " " + letter
    cur_iteration += 1

print statement
        
