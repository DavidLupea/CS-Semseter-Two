#David Lupea
#IntroCS2 pd5
#HW15 -- Loop-De-Loop
#2018-3-11

#WhileLoop2.py

import random
import time

#Question 1
number = None
while (number < 1) or (number >= 10):
    number = float(raw_input("Enter a number within [1,10): "))
print "Thanks \n"


#Question 2
my_number = float(raw_input("Enter a positive number: "))
iteration = 1

while (iteration < my_number):
    if iteration % 2 == 1:
        print iteration
    iteration += 1
print "DONE \n"


#Question 3
first_num = float(raw_input("Enter a positive integer: "))
second_num = float(raw_input("Enter another: "))

iteration = min(first_num, second_num)
maximum = max(first_num, second_num)

while iteration < maximum:
    if iteration % 2 == 1:
        print int(iteration)
    iteration += 1
print "\n"

#Question 4
n = int(raw_input("Enter a positive integer: "))

divisors = 0
iteration = 1

if n == 1:
    print n, "is not prime"
else:
    while iteration < n:
        if n % iteration == 0:
            print iteration
            divisors += 1
        iteration += 1
    if divisors > 1:
        print n, "is not prime"
    else:
        print n, "is prime"
print "\n"


#Question 5
total_slots = 8
iteration = 1

print "Welcome to the slot machine simulation."
print "Here's a spin....."
time.sleep(2.2)

while iteration <= total_slots:

    choice1 = random.choice(['orange   ', 'lemon    ', 'lime     ', 'cherry   '])
    choice2 = random.choice(['orange   ', 'lemon    ', 'lime     ', 'cherry   '])
    choice3 = random.choice(['orange   ', 'lemon    ', 'lime     ', 'cherry   '])

    time.sleep(1)
    print choice1 + choice2 + choice3 + "\n"

    if iteration == 8:
        if choice1 == choice 2 and choice 1 == choice3:
            print "All values are the same.  You win!!!"
        elif choice1 != choice 2 and choice2 != choice3:
            print "All values are different. You win!!!"
        else:
            print "You lose :("


    iteration += 1









        
