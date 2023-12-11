# decorator functions
# python decorators allow you to change the behaviour of a function without modifying the function itself

# when to use a decorator function in python
# when you need to change the behaviour of a function itself without modifying the function itself e.g when to add logging, test performance, caching, verify permission, when you need to run the same code on multiple functions, avoids code duplicity e.t.c

# recall: since a function can be nested inside another function, it can also be returned
# e.g
def outer_function():
    '''Assign task to student'''   

    task = 'Read Python Book Chapter 3.'
    def inner_function():
        print(task)
    return inner_function

homework = outer_function()
# print(homework()) # notice that to access the function you have to put the "()" in the print function!

# nested functions revised 
def outer_function():

    def inner_function():

        print('I came from the inner function.')
        
    # executing the inner function inside the outer function
    inner_function()

# outer_function() 

# passing a function as an argument 
def friendly_reminder(func):
    '''reminder for wifey'''

    func()
    print('don\'t forget to bring my wallet')

def action():

    print('i am going to the store to buy you something nice.')

# calling the friendly_reminder function with the action function used as an argument 
# friendly_reminder(action)

# how to create a python decorator
# syntax
def my_decorator_func(func):

    def wrapper_func():
        # do something before the function.
        func()
        # do something after the function.
    return wrapper_func

# to use a decorator, you attach it to a function as demonstrated below 
# we use a     ''     by placing the name of the decorator directly above the function you want to use it on and prefix the decorator function with a "@" symbol 
@my_decorator_func
def my_func():

    pass

# e.g decorator function that logs the date and time a function is executed:
from datetime import datetime

def log_datetime(func):       
    """log the date and time that a function is executed"""
                 
    def wrapper():        
        print(f'function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*27}')
        func()
    return wrapper

@log_datetime
def daily_backup():

    print('Daily backup job has finished.')
    
daily_backup()

# how to add arguments to decorators in python
# to add arguments, use the (*args) and (**kwargs)
# NB: (*args) takes an unlimited number of positional arguments e.g 10, True, 'inie'
# while (**kwargs) takes an unltd number of keyword arguments e.g count = 99, is_authenticated = True, backend_engineer = 'inie'
# e.g of decorator with arguments
from functools import wraps
def decorator_func(func):

    def wrapr_func(*args, **kwargs):
        # do something before the function
        func(*args, **kwargs)
        # do something after the function
    return wrapr_func

@decorator_func
def my_function(my_args):
    '''example docstring for function'''

    pass

# NB: decorators hide the function they are decorating; hence the unexpected result
# to fix the issue, use functools. functools wraps will update the decorator with the decorated functions attributes
print(my_function.__name__)
print(my_function.__doc__)
  
# ex1
# def add_message(func):
#     def inner_func(name):   
#         print('i am the extra message')
#         return func(name)
#     return inner_func

# def to_uppercase(func):
#     def to_capital(name):         
#         value = func(name)
#         return value.upper()
#     return to_capital

# @add_message 
# @to_uppercase 
# def greet(name):
#     # print(f'welcome {name}')
#     return f'welcome {name}'

# print(greet('inie'))

# ex2
# def prevent_error(func):
#     def wrapper(operation_type, num1, num2):
#         if not isinstance(num1, int) and isinstance(num2, int):
#             print('oops sorry only int or float are allowed')
#             return
#         else:
#             func(operation_type, num1, num2)
#     return wrapper

# @prevent_error
# def calculator(operation_type, num1, num2):
#     if operation_type == 'add':
#         return num1 + num2
#     elif operation_type == 'sub':
#         return num1 - num2
#     elif operation_type == 'mult':
#         return num1 * num2

# print(calculator('add', '20', True))

# # ex3
# def avoid_error(num_list):
#     def wrapper(number):
#         if not isinstance(number, int):
#             print('oops please provide a numerical value!')
#             return
#         else:
#             num_list(number)
#     return wrapper

# @avoid_error
# def sum_of_list(num_list):
#     total = 0
#     for i in num_list:
#         total += i
#         return total 

# numbers = [4, 2, 5, 7, 9, 10]
# print(sum_of_list(numbers))
