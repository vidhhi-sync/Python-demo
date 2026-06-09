#List
student = [ "anvi",88,"vishu",94,"vidhi",89,"tiya",100]
print(student[1])
for x in range(0,len(student),2):
       print(student[x],"scored",student[x+1])

#Append is used to add more items in the same list
student.append("Lalita")
student.append(98)
for x in range(0,len(student),2):
    print(student[x],"scored",student[x+1])

#consider if we make a mistake in the list while appending so we can change it:
student[-1] = 92 #as the append is added in the last so we can get it from inverse index
print(student)

#appending a list into another list can be done using extend\
student2 = ["vidya", 77]
student.extend(student2)
print(student)

#Removing from a string
student.remove("vishu") #the keyword remove() helps in removing item from the list
student.remove(94)
print(student)

#another way of removing item is using keyword pop()
student.pop(0) #here 1st item anvi is removed
student.pop(-1) #here last item marks of vidya is removed
print(student)

#we can also totally clear out the list of student using the keyword clear()
student.clear()
print(student) #we get square brackets as an output itself

#to count how many times does a item repeated in the list we use count()
count = student.count(88)
print(count)
count1 = student.count("anvi")
print(count1)

#to find the index number of the item in the list using index()
index = student.index("vidhi")
print(index)
index1 = student.index(100)
print(index1)

#Using of sort() keyword
name = ["mom","dad","sis","bro"]
name1= [4,3,7,5]
print(name)
print(name1)
name.sort() #here the name and no. are sorted out according to alphabetical and smaller to larger
name1.sort()
print(name)
print(name1)

#Reversing the list using reverse() keyword
name.reverse()  #the order of the list is reversed
print(name)

#copying a list using copy() keyword
name_bkup = name.copy()
print(name_bkup)

#inserting an item in the middle of the list using insert() keyword
name.insert(2,"vartika") #this inserted another string in middle of list
print(name)