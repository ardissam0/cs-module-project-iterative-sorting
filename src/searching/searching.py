def linear_search(arr, target):
    # Your code here
    #loop through the elements in the array
    for i in range(len(arr)):
        #if the element is the target then return it
        #if not then keep going 1 by 1
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # define what is low, mid, and high
    low = 0
    high = len(arr) -1
    mid = 0
    #while low is less than or equal to high
    while low <= high:
        #mid is high divied by low
        mid = (high + low)//2
        #if mid is less than the target
        if arr[mid] < target:
            #then low is mid + 1
            low = mid + 1
        # if mid is greater than the target
        elif arr[mid] > target:
            #high is mid -1
            high = mid -1
        #otherwise return the mid element
        else:
            return mid


    return -1  # not found
