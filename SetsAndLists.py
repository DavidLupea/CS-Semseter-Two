#Given L = [1,3,5,2,1,5], write code to remove duplicates and set the list L in descending order

L = [1,3,5,2,1,5]

L = list(set(L))
L.sort(reverse = True)

print L
