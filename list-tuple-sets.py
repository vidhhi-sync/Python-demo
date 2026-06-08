#List
student = [ "anvi",88,"vishu",94,"vidhi",89,"tiya",100]
print(student[1])
"""for x in range(0,len(student),2):
    print(student[x],"scored",student[x+1])"""

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