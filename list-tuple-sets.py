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