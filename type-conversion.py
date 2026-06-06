a=2
b=4.25
sum = a + b
print(sum) # here it automatically convert the integer value into float value

#converting string into integer by using type casting
a,b = 1, "2"
c = int(b) #here b which is string is forcefully converted into integer to perform the operation
sum = a + c
print(sum)
print(type(b))
print(type(c))

#converting float number into a string but vice versa is not possible
m=3.21
m=str(m)
print(m)
print(type(m))