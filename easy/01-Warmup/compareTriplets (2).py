def compareTriplets(a, b):
    # Create a list comprehension that generates a new list 'x' based on the comparison of each element in 'a' and 'b'.
    # If the element in 'a' is greater than the corresponding element in 'b', add 1 to the 'x' list.
    # If the element in 'a' is less than the corresponding element in 'b', add -1 to the 'x' list.
    # If the elements are equal, add 0 to the 'x' list.
    x = [1 if x>y else -1 if x<y else 0 for x,y in zip(a,b) ]
    
    # Return a tuple of the count of the positive values in 'x' and the count of the negative values in 'x'.
    return x.count(1),x.count(-1)
