# factorial

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(5))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n* factorial(n-1)
print(factorial(0))