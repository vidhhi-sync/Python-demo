# Using Arithmetic Operators
a=3
b=1
#Subtraction
print(a-b)
print(type(a-b))
#Addition
print(a+b)
print(type(a+b))
print(1+1)
#Multiplication
print(a*b)
print(type(a*b))
#Division
c=a/b
print(c)
print(type(c))
#Modulous
print(a%b)
print(type(a%b))
#Extra
a= 1*2
b= 5*6
print(a*b)


#Comparison Operator
a=5
b=9
print(a<b)
print(a>b)
print(a!=b)
print(5==5)
print(a==b)
print("abcd"=="abcd")
print("abcd"=="abc")
print("abcd">="abc") #string is greater in number here
print(len("abcd")>=len("abc")) #Length of the string is compared
print(len("abcd")==len("abcd"))
print("abcd"=="1234") #here it is considering number as string as it is in quotation
print("abcd"=="123")
print(5 is 5)
print(5 is not 10)
print(5 is 10)

#Boolean Operators
a=True
b=False #false with small f cannot be considered as per boolean syntax
print(a or b) #either one should be true
print(a and b) #both should be true
print(not a) #prints the opposite