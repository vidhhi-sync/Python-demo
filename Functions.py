#Function definition
def greet(name = "User"):
    """name = STR , optional
    the default is "User" """
    print("Hi there" , name)
print(greet('vidhi'))
print(greet())
print(greet(name = "tiya"))
print(greet.__doc__) #calling docstring

#using function to  return a value
def square_n(x):
    return x**2
print(square_n(2))