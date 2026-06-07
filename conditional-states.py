#Basic if code
s = 9
if (s>0):
   print(True) #when this space(indentation) is provided the statements are inside the if statement
print("End of Program")  # here space (indentation) is not provided so this statement is not inside the if statement

#Basic if  condition code
m = int(input("Enter value of m:"))
if (m%2==0):
    print("Valid")

#Basic if-else statement code
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
if (a>=b):
    print(True)
else:
    print(False)    

#Elif statement code
c = int(input("Enter value of c:"))
d = int(input("Enter value of d:"))
if (c>d):
    print(True)
elif (c==d) :
    print("Equal")
else:
    print(False)