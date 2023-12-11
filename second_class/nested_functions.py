# nested functions
# this is a function within another function

# reasons to use nested functions
# 1. data encapsulation a.k.a data hiding/data privacy
# 2. closures/factory functions

# data encapsulation
# ex1
def greeting(first, last):
    # nested helper function 
    def getFullName():
        return first + " " + last 
    
    print("Hi, " + getFullName() + "!")

# greeting('ini-ubong', 'isemin')

# ex2
def outer():
    print("i'm the outer function.")
    def inner():
        print("and i'm the inner function.")
    inner()

# outer()

# closures
# here, the outer function returns the inner function itself...they do not "hide" the inner function!
# conditions for creating closures in python:
# 1. there must be a nested function
# 2. the inner function has to refer to a value that is defined in the enclosing scope
# 3. the enclosing function has to return the nested function 
# ex1
def num1(x):
    def num2(y):
        return x + y
    return num2

print(num1(10)(5)) 
# closures make it possible to pass data to inner functions without first passing them to outer functions with parameters like the greeting function
# they also enable us to invoke the inner function from outside of the encapsulationg outer function...along with the benefit of data encapsulation 


# def greeting():
#     print('i am the outer function')
#     def inner_fn():
#         print('yo! i am the child function')
#     return inner_fn()

# print(greeting())

# def process_dividend(total_sales, selling_price):
#     cost_price = 10
#     def calc_profit():
#         profit = selling_price - cost_price
#         total_profit = profit * total_sales
#         return total_profit
#     return calc_profit() 
    
# print(process_dividend(7, 12)) 


