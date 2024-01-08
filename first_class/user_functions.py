def welcome_to_class():
    name = input('what is your name? ')
    gender = input('what is your gender orientation? ')
    if gender == 'male':
        print(f'welcome to backend class mr {name}')
    elif gender == 'female':
        print(f'welcome to backend class mrs {name}')

# welcome_to_class() 

def add_number():
    num1 = [5, 6, 7, 8, 9]
    num2 = 15
    numlist = []
    for i in num1:
        num = i + num2
        print(num, numlist)
        list.append(numlist, num)

# add_number()

def add_numbers():
    num1 = 10
    num2 = 15
    add = num1 + num2
    return add

result = add_numbers()
# print(result)

# NB: arguments == actual values; parameters == characters used when definining functions 
# NB: if you combine positional and keyword arguments, keyword arguments must come first!

def addition(a, b):
    print(a)
    print(b)
    return a + b

# print(addition(5, 6)) # using positional arg
# print(addition(b = 9, a = 4)) # keyword args...notice the order is inconsequential

def multiplication(n1, n2):
    return n1 * n2 

# print(multiplication(5, 10))
# NB: you can provide multiple arguments, but you have to provide the values 

# '*args' and '**kwargs' allow you to pass an unlimited number of arguments...
# python represents '*args' values as tuples while '**kwargs' are represented as dictionaries

def addition(*args): #()
    result = 0
    print(args)
    for n in args:
        result += n
    return result

# using positional args
# print(addition(5, 6, 7, 8)) 
# print(addition(5, 6, 7))               
# print(addition(5, 6))              
# print(addition(5))             

def multiplication(*args):
    result = 1    
    print(args)
    for x in args:
        result *= x
    return result

# using positional args
# print(multiplication(5, 6, 7, 8)) 
# print(multiplication(5, 6, 7))                 
# print(multiplication(5, 6))                
# print(multiplication(5))               

# '**kwargs'
def multiplication(**kwargs): #{}
    result = 1
    for i, v in kwargs.items():
        result *= v
    return result  

# using keyword args
print(multiplication(a = 10, b = 5, c = 5)) 
print(multiplication(a = 10, b = 5)) 
print(multiplication(a = 5)) 

def get_smallest_from_list(nums:list[list]):
    """This function takes a list of lists and returns the smallest element."""
    smallest = nums[0]
    for a in nums:
        if a < smallest:
            smallest = a
        return smallest 
      
numb = [4, 2, 5, 7, 9, 1, 6]
numbers = [4, 3, 10, 7, 9, 8, 6]
less = get_smallest_from_list(numb)
# print(less)
least = get_smallest_from_list(numbers)
# print(least)

def get_highest_from_list(nums:list[list]):
    highest = nums[0]
    for x in nums:
        if x > highest:
            highest = x
        return highest 

numb = [10, 2, 5, 7, 9, 1, 6]
greatest = get_highest_from_list(numb)
# print(greatest)

def get_biggest_from_list(nums:list[list]):
    highest = nums[0:]
    for x in highest:
        if x > x+1:
            return x
    # return highest

numb = [10, 2, 5, 7, 9, 1, 6]
biggest_num = get_biggest_from_list(numb)
# print(biggest_num)

# def find_target(list, target):
#     for x in list:
#         if target == x:
        
# numbers = [4, 2, 5, 7, 9, 1, 6]
# val = 8
# print(find_target(numbers, val))

def sum_of_list(num_list):
    total = 1 
    for i in num_list:
        total += i
        return total
    
numbers = [4, 2, 5, 7, 9, 10]
# print(sum_of_list(numbers))

# def int_num(integ):
#     result = []
#     for x in integ:
#         if type(x) == int:
#             return list(integ)

# numo = [5, 10, ]

def filter_list(numList):
    result = []
    for val in numList:
        if isinstance(val, int):
            result.append(val)
    return result

dirty_list = [3, 5.00, '30', 4, 9, True, 'two', 0.002, 7]
# print(filter_list(dirty_list))