# exercise
# write a function that takes in an array of numbers (list) and a target number and checks if the target number is present in the list and returns the index, if the number is not present in the list, return -1

arr = [13, 14, 7, 8, 9, 6, 4]
tar = 8

def arr_index(target):
    """this function checks if a target number is present in an array and returns its index
    args:
    arr: a list of integers
    target: the target number to search for
    returns: 
    the index of the target number if found, else -1"""
     
    # loop through the array 
    for i, num in enumerate(arr):
        # check if the current number is the target
        if num == target:
            return i

    # if target is not found;
    return -1

index = arr_index(8)
print(index)