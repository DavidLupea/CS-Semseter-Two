#isDivisor script

#Definitions
isDivisor = lambda n, d: n%d == 0
n = int(raw_input("Enter an integer: "))

#Method 1
if isDivisor(n, 2):
    if isDivisor(n, 3):
        print n, "is divisible by 2 and 3"
    else:
        print n, "is divisible by 2 not 3"
else:
    if isDivisor (n, 3):
        print n, "is divisible by 3 not 2"
    else:
        print n, "is not divisible by 2 or 3"

#Method 2
if isDivisor(n, 2):
    if isDivisor(n, 3):
        print n, "is divisible by 2 and 3"
    else:
        print n, "is divisible by 2 not 3"
elif isDivisor(n, 3):
    print n, "is not divisible by 3 not 2"
else:
    print n, "is not divisible by 3 or 2"

#Method 3
if isDivisor(n, 6):
    print n, "is divisible by 3 and 2"
elif isDivisor(n, 2):
    print n, "is divisible by 2 not 3"
elif isDivisor(n, 3):
    print n, "is divisible by 3 not 2"
else:
    print n, "is not divisible by 3 or 2"
