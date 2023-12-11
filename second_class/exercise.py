# exercise
# write a function that takes in an array of numbers (list) and a target number and checks if the target number is present in the list and returns the index, if the number is not present in the list, return -1

arr = [13, 14, 7, 8, 9, 6, 4]
tar = 8

def arr_index(array, target):
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

index = arr_index(arr, 8)
print(index)

# def arr_index(ind, target):
#     for n in ind:
#         if n == target:
#             return arr.index(target)
#         else: 
#             if n != target:  
#                 return -1
        
# print(arr_index(arr, tar))      

# def find_my_target(my_array, target):
#     for a in my_array:
#         if a == target:
#             return my_array.index(target)
#         else:
#             if a != target:
#                 return -1
            
# my_array = [13, 14, 7, 8, 9, 6, 4]
# target = 1
# print(find_my_target(my_array, target))