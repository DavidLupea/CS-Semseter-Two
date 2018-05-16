#David Lupea
#IntroCS2 pd5
#HW35 -- SetsFormatted
#2018-5-09

def makeset(a,b):
    if a == b:
        output = '{' + '{}'.format(a) + '}'
    else:
        output = '{' + '{}, {}'.format(a, b) + '}'
    return output

def main():
    print 'makeset(1,1)     ->       ' + makeset(1,1)
    print 'makeset(1,2)     ->       ' + makeset(1,2)
    print 'makeset(-1,-1)   ->       ' + makeset(-1,-1)
    print 'makeset(5,10     ->       ' + makeset(5,10)
    print 'makeset(-37,-37) ->       ' + makeset(-37,-37)

main()


    
