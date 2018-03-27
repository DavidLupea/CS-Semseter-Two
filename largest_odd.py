x = int(raw_input("Enter an integer: ")) 
y = int(raw_input("Enter another integer: "))
z = int(raw_input("Enter a final integer: "))

isodd = lambda x : x % 2 == 1

x = x if isodd(x) else None
y = y if isodd(y) else None
z = z if isodd(z) else None

ans = max(x, y, z)

if ans == None:
    print "None of the values were even"
else:
    print ans
