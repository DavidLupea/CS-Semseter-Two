# global variable
numCalls = 1


# Nonrecursive solution - iterative process
def fibI(n):
    '''Assume n is a positive int.
       Return the nth term of the fibonacci sequence starting with 0 and 1.'''
    first, second = 0,1
    while n > 1:
        first, second = second, first + second
        n -= 1
    return first

# Tail Recursive - a recursive function without a delayed operation
def fibTr(n, first=0, second=1):
    if n == 1:
        return first
    if n == 2:
        return second
    global numCalls
    numCalls += 1
    return fibTr(n-1,second, first + second)
# Tree Recusive - a recursive function with a delayed addition
def fibTree(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    global numCalls
    numCalls += 2
    return fibTree(n-1) + fibTree(n-2)
# dynamic programming
def fib_dp(n, fibs=[0,1]):
    if len(fibs)<3:
        fibs.insert(0,0) #adds a dummy value to the list
    if n<len(fibs):
        return fibs[n]
    global numCalls
    numCalls +=2
    fibs.append(fib_dp(n-1)+fib_dp(n-2))
    return fibs[-1]
def fibtester(f, n):
    '''Assume f is a function and n is a positive int.
       Prints the first n terms of the fibonacci sequence.'''
    global numCalls
    numCalls=1
    for i in range(1, n + 1):
        print i, 'th term', f(i) , '# function calls:', numCalls
    print 'Done testing ', f

def main():
    n = int(raw_input('enter a positive integer: '))
 #   fibtester(fibTr, n)
  #  fibtester(fibI, n )
    fibtester(fib_dp,n)
  #  fibtester(fibTree,n)
    
# function call
main()
