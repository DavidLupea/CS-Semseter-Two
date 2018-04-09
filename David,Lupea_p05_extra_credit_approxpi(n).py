#David Lupea
#IntroCS2 pd 5
#Extra credit -- approxpi(n)
#2018-04-04

#Recursively
def approxpi_recursive(n, iteration = 0, total = 1, current = 3.0):
    if iteration == n:
        print total * 4
    elif iteration % 2 == 0:
        approxpi_recursive(n, iteration + 1, total - (1 / current), current + 2.0)
    else:
        approxpi_recursive(n, iteration + 1, total + (1 / current), current + 2.0)

approxpi_recursive(0)
approxpi_recursive(1)
approxpi_recursive(2)
approxpi_recursive(100)

#Non recursively
def approxpi(n):
    x = 0
    value = 1
    while x < n:
        if x%2 == 0:
            value -= 1.0/(2 * (x + 1) + 1)
        else:
            value += 1.0/(2 * (x + 1) + 1)
        x += 1
    value = 4 * value
    return value

print approxpi(0)
print approxpi(1)
print approxpi(2)
print approxpi(100)
