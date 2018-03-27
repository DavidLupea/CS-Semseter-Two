try:
    radius = int(raw_input("Enter the radius: "))

    diameter = 2 * radius

    print diameter

except ValueError:
    print "You didn't type in an integer. Please type in an integer"


