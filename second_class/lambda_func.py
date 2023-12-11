# def add(a, b):
#     return a + b

# add = lambda a, b: a + b
# print(add(2, 5))

# mult = lambda a, b: a * b
# print(mult(5, 7))

# greet = lambda name: print(f'welcome {name}')
# print(greet('inie'))

# sqr = lambda x, y: x ** y
# print(sqr(2,2))

# recursion 
# when a function calls itself directly or indirectly 

def recursive_factorial(n):
    if n == 1:
        return n 
    else:
        print('recursive call')
        return n * recursive_factorial(n-1)
    
res = recursive_factorial(7)
print(res)

# def recursive_fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
    
# n_term = 10
# for i in range(n_term):
#     print(recursive_fibonacci(i))
