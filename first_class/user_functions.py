# def welcome_to_class():
#     name = input('what is your name? ')
#     print(f'welcome to backend class mr/mrs {name}')

# welcome_to_class()

# def add_numbers():
#     num1 = [5, 6, 7, 8, 9]
#     num2 = 15
#     for i in num1:
#         print(i + num2)

# add_numbers()

# def add_numbers():
#     num1 = 10
#     num2 = 15
#     add = num1 + num2
#     return add

# result = add_numbers()
# print(result)

# NB: arguments == actual values; parameters == characters used when definining functions 
# NB: if you combine positional and keyword arguments, keyword arguments must come first!

# def addition(a, b):
#     print(a)
#     print(b)
#     return a + b

# def multiplication(n1, n2):
#     return n1 * n2 

# print(addition(5, 6)) # using positional args
# print(addition(a = 10, b = 12)) # keyword args
# print(addition(b = 9, a = 4)) # keyword args
# print(multiplication(5, 10))
# NB: you can provide multiple arguments, but you have to provide the values 

# '*args' and '**kwargs' allow you to pass an unlimited number of arguments...
# python represents '*args' values as tuples while '**kwargs' are represented as dictionaries

# def addition(*args): #()
#     result = 0
#     print(args)
#     for n in args:
#         result += n
#     return result

# def multiplication(*args):
#     result = 1
#     print(args)
#     for x in args:
#         result *= x
#     return result

# print(addition(5, 6, 7, 8)) # using positional args
# print(addition(5, 6, 7)) # using positional args
# print(addition(5, 6)) # using positional args
# print(addition(5)) # using positional args

# print(multiplication(5, 6, 7, 8)) # using positional args
# print(multiplication(5, 6, 7)) # using positional args
# print(multiplication(5, 6)) # using positional args
# print(multiplication(5)) # using positional args

# print(multiplication(a = 10)) # keyword args
# print(multiplication(b = 9)) # keyword args
# print(multiplication(a = 5))

# '**kwargs'
def multiplication(**kwargs): #{}
    result = 1
    for i, v in kwargs.items():
        result *= v
    return result 

print(multiplication(a = 10, b = 5, c = 5)) # using keyword args
print(multiplication(a = 10, b = 5)) # using keyword args
print(multiplication(a = 5)) # using keyword args

# def get_smallest_from_list(nums:list[list]):
#     smallest = nums[0]
#     for a in nums:
#         if a < smallest:
#             smallest = a
#         return smallest 
    
# numbers = [4, 2, 5, 7, 9, 1, 6]
# numbers2 = [4, 3, 10, 7, 9, 8, 6]
# less = get_smallest_from_list(numbers)
# print(less)
# less2 = get_smallest_from_list(numbers)
# print(less2)

# def get_smallest_from_list(nums:list[list]):
#     smallest = nums[0]
#     for a in nums:
#         if a > highest:
#             highest = a
#         return highest 

# def find_target(list, target):
#     for x in list:
#         if target == x:
        

# numbers = [4, 2, 5, 7, 9, 1, 6]
# val = 8
# print(find_target(numbers, val))

# def sum_of_list(num_list):
#     total = 0
#     for i in num_list:
#         total += i
#         return total
    
# numbers = [4, 2, 5, 7, 9, 10]
# print(sum_of_list(numbers))

# def int_num(integ):
#     result = []
#     for x in integ:
#         if type(x) == int:
#             return list(integ)

# numo = [5, 10, ]

# def filter_list(numList):
#     result = []
#     for val in numList:
#         if isinstance(val, int):
#             result.append(val)
#     return result

# dirty_list = [3, 5.00, '30', 4, 9, True, 'two', 0.002, 7]
# print(filter_list(dirty_list))
    




