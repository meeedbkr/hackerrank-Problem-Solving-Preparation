#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Sum the elements in the array using the built-in sum function
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the size of the array from input
    ar_count = int(input().strip())

    # Read the elements of the array from input and split them by space
    ar = list(map(int, input().rstrip().split()))

    # Call the function to get the sum of the array elements
    result = simpleArraySum(ar)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()
