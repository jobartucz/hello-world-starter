# this is an example program to help understand how the debugger works in Thonny

# a and b are variables. They can contain anything.
a = 5
b = 6
print (a + b)

# here we are going to call a function to do the multiplication
print (multiply(a, b))

# Here is a function definition. You can see that it takes two input variables
# This part of the code won't run by itself. It has to be called specifically
def multiply(x, y):
    result = x * y
    return result