#String Manipulation

#cancatenating string
num1 = "vid"
num2 = "hi"
sum = num1 + num2
print("My name is ", sum)

#Length of the string
name = "Vidhi"
print(len(name))
name1 = "Tiya"
print(len(name1))
name2 = "Sanskriti"
print(len(name2))
name3= "vid hi" #here the space is also counted in the length of the string
print(len(name3))
#Even only spaces can have length 
a = ""
b = " "
c = "v x y "
print(len(a))
print(len(b))
print(len(c))

#using in and not in
#this checks whether a particular character is in the string or not
print("a" in name1)
print("a" not in num1)
print("v" in num2)

#printing only specific characters from name
name4 = "Tisha"
print(name4[0])
print(name4[:]) #prints the full string
print(name4[2])
print(name4[-2]) #inverse index, will begin from last
print(name4[-1])
print(name4[0:2])
print(min(name4)) #prints minimum and maximum ASCII value of the characters in the name.
print(max(name4)) 
print(name4.upper()) #capitalize every character
print(name4.swapcase()) #swap the upper and lower case in the string
print(name4.title()) #starts the string with a capital letter
print(name4.istitle()) #checks true or false, works as is

#apna college

str1 = "this is a string"
str2 = 'this is also a string'
str3 = """This is also considered as string"""
print(str1)
print(str2)
#adding escape characters to modify text
str4 = "this is a string.\nIt is used in python"
str5 = "this is a string.\t It is used in python"
print(str4)
print(str5)
#performing concatenation on string
print(str1 + " " + str2) #this empty quotation marks adds a space.
#printing length of a string
print(len(str1)) #it counts the spaces in between also.
#Indexing
str6 = "Vidhi"
ch = str6[0] #index 0 is the position of first character
print(ch) #prints the character whose index we are calling, if there is a space we can print it too
print(str6[3])
#slicing
print(str6[0:3]) #it prints characters on index 0,1,2 , it won't print 3 index character