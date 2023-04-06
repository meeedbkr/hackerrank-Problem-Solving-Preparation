def miniMaxSum(arr):
    # sort the input array in ascending order
    sorted_arr = sorted(arr)
    
    # calculate the sum of all elements in the array
    total_sum = sum(sorted_arr)
    
    # calculate the minimum and maximum values by excluding the last and first elements in the sorted array respectively
    min_val = total_sum - sorted_arr[-1]
    max_val = total_sum - sorted_arr[0]
    
    # print the minimum and maximum values separated by a space
    print(min_val, max_val)
