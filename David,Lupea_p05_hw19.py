#David Lupea
#IntroCS2 pd5
#HW19 -- OnTarget
#2018-3-22

def upTo(target, L):
    '''Takes in an target and a list
    If the target is the first value of the list,
    it returns an empty list. Otherwise, it
    prints all the values in the list up to but
    not including the target'''
    returned_list = []
    if target not in L or target == L[0]:
        return returned_list
    else:
        for item in L:
            if item == target:
                break
            else:
                returned_list.append(item)
        print returned_list
