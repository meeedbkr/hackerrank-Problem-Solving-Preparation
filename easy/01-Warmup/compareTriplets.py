def compareTriplets(a, b):
    # create a list of scores for each comparison using a list comprehension
    # 1 if x > y, -1 if y > x, and 0 if x == y
    s = [1 if x > y else -1 if y > x else 0 for x, y in zip(a, b)]
    
    # count the number of 1's and -1's in the score list and return as a tuple
    return s.count(1), s.count(-1)
