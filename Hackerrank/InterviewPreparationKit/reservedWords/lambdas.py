"""
    Add 10 to argument a, and return the result:
"""

x = lambda a: a + 10
print(x(5))

y = lambda a, b : a * b
print(y(5, 6))


z = lambda a, b, c : a + b + c
print(z(2, 4, 5))

def multiply_constant(n):
    return lambda x: x * n

print(multiply_constant(5)(10))