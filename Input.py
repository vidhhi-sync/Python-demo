
#Taking input from user in python
name=input("Enter your name: ")
print("Welcome", name)

#No matter what value we write the compiler will show the type of that value as string only while using input 
value=input("Enter some value:")
print(type(value),value)


#if we want to take an integer as input
value=int(input("Enter some value:"))
print(type(value),value)


#We want take data of a student
name = input("Enter your name:")
age= int(input("Enter your age:"))
marks=float(input("Enter your marks:"))
print(type(name),name)
print(type(age), age)
print(type(marks),marks)