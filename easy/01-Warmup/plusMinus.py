def plusMinus(arr):
    # create a list of 1s, -1s, and 0s indicating if each element in the input array is positive, negative, or zero
    s = [ 1 if el>0 else -1 if el<0 else 0 for el in arr ]
    # get the length of the input array
    n = len(s)
    # print the ratio of positive elements in the input array
    print( s.count(1)/n )
    # print the ratio of negative elements in the input array
    print( s.count(-1)/n )
    # print the ratio of zero elements in the input array
    print( s.count(0)/n )
