#David Lupea
#IntroCS2 pd5
#HW18 -- HomeHomeOnTheRange
#2018-3-13

#fractions.py
for i in range(2, 11):
    print "1/" + str(i) + " = " + str(1.0 / i)

#sumOdd.py
sum_num = 0
my_number = int(raw_input("Enter a positive number: "))

for i in range(my_number + 1):
    if i % 2 == 1:
        sum_num += i

print "Sum of odds from 1 to " + str(my_number) + " : " + str(sum_num)

#nPerLine.py
num_per_line = int(raw_input("How many numbers per line: "))
iteration = 1
output = ""

for i in range(10, 31):
    if iteration % num_per_line == 0:
        output = output + str(i) + "  \n"
        
    else:
        output += str(i) + "  "   
    iteration += 1
print output
