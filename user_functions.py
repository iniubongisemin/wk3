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

def addition(*args):
    result = 0
    print(args)
    for n in args:
        result += n
    return result

def multiplication(*args):
    result = 1
    print(args)
    for x in args:
        result *= x
    return result

print(addition(5, 6, 7, 8)) # using positional args
print(addition(5, 6, 7)) # using positional args
print(addition(5, 6)) # using positional args
print(addition(5)) # using positional args

print(multiplication(5, 6, 7, 8)) # using positional args
print(multiplication(5, 6, 7)) # using positional args
print(multiplication(5, 6)) # using positional args
print(multiplication(5)) # using positional args

# print(multiplication(a = 10, b = 12)) # keyword args
# print(multiplication(b = 9, a = 4)) # keyword args
# print(multiplication(a = 5, b = 10))
