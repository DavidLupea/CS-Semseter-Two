#With conditionals
def smth(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:                       #Checks if n1 is the biggest number
        if n2 >= n3:                                #Chechs which number is the second biggest between n2 and n3
            print n3, n2, n1
        else:
           print n2, n3, n1
    elif n2 >= n1 and n2 >= n3:                    #Checks if n2 is the biggest number
        if n1 >= n3:                                 #Chechs which number is the second biggest between n1 and n3
            print n3, n1, n2
        else:
            print n1, n3, n2
    elif n3 >= n1 and n3 >= n2:                     #Checks if n3 is the biggest number
        if n1 >= n2:                                #Chechs which number is the second biggest between n1 and n2
            print n2, n1, n3
        else:
            print n1, n2, n3


#Without conditionals
minimum = min(n1, n2, n3)
middle = (n1 + n2 + n3 - max(n1, n2, n3) - min(n1, n2, n3))
maximum = max(n1, n2, n3)

print minimum, middle, maximum
