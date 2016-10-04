def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    #Reverse de nested lists van L
    for i in L:
        i.reverse()
    #reverse de lists van L
    L.reverse()

#testcase
#L =  [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
#deep_reverse(L) 
#print(L)
