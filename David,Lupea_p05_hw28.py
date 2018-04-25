#Team David + Ling
#David Lupea
#IntroCS2 pd 5
#HW28 -- Pell Sequence
#2018-04-24

#global variable
numCalls = 1

#Question 1: Iterative process
def pell_iter(n):
    '''Assumes n is a postive integer,
    Returns nth term of the pell sequence
    Uses iterative'''
    values = [0,1]
    if n < 2:
        return values[n]
    for i in range(2, n + 1):
        values.append(2 * values[i - 1] + values[i - 2])
    return values[-1]


#Question 2: Tail Recursive 
def pell_tail(n, zeroth=0, first=1):
    '''Assumes n is a postive integer,
    Returns nth term of the pell sequence
    Uses tail recursive'''
    if n == 0:
        return zeroth
    if n == 1:
        return first
    global numCalls
    numCalls += 1
    return pell_tail(n-1,first,(2 * first) + zeroth)


#Question 3: Tree Recusive 
def pell_tree(n):
    '''Assumes n is a postive integer,
    Returns nth term of the pell sequence
    Uses tree recursive'''
    if n == 0:
        return 0
    if n == 1:
        return 1
    global numCalls
    numCalls += 2
    return 2 * pell_tree(n-1) + pell_tree(n-2)


#Question 4: Dynamic Programming
def pell_dp(n ,pells = [0,1]):
    '''Assumes n is a postive integer,
    Returns nth term of the pell sequence
    Uses dynamic programming'''
    if len(pells) < 2:
        pells.insert (0,0)
    if n < len(pells):
        return pells[n]
    global numCalls
    numCalls += 2
    pells.append(2 * pell_dp(n -1) + pell_dp(n-2))
    return pells[-1]


#Question 5
#The pell_iter(10) has 1 function call
#The pell_tail(10) has 46 function calls
#The pell_tree(10) has 443 function calls
#The pell_dp(10) has 19 function calls

#Tester function
def pell_tester(f,n):
    """Assumes f is a function and n is a postive integer
    Does not retrun anything but return the n terms of pell sequnce"""
    global numCalls
    numCalls = 1
    print str(f)
    for i in range(n+1):
        print i,"nth term",f(i),"numCalls = ", numCalls
    print "Done testing"


#Main function
def main():
    n = int(raw_input("Enter a postive integer: ") )
    pell_tester(pell_iter,n)
    pell_tester(pell_tail,n)
    pell_tester(pell_tree,n)
    pell_tester(pell_dp,n)

main()


#Question 6
#The last term the tail recursive function can compute is the 995th term, in which the number of function calls was 494516
#The value of pel_tail(995) is 25719464244931240522975804518708127252367658320032553109179213802659130517407514390947048896296835519408397
#62201944221272466028366488603863043725465053867026857818203783356456492206558954678928840724806799630070797738571453800044110660503306419
#58023205479618071709979463890080537840653960293983999547466013650285725986503539114249073888973265583686768882420357855027541838823986021













