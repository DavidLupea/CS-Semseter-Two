#David Lupea
#IntroCS2 pd5
#HW26 -- MapsMaps
#2018-4-16

def mymap(f,L):
    '''Assume f is a function and L is a list
    Returns a list'''
    returned = []
    for i in L:
        returned += [f(i)]
    return returned

        
print mymap(lambda x: x**2, [1,2,3])
print mymap(lambda s: len(s) , ['cat' , 'frog'])

def factorial(x):
    total = 1
    for i in range(1, x + 1):
        x *= i
    return x

print mymap(factorial, [7,8,9,10])
