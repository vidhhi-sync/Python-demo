#For loop execution (Numbers)
for a in range (5):
    print("OK",a)
print("Outside the for loop")

#for a particular range
for b in range (2,5):   #here it will follow the index rule like before.
    print("Range",b)

#Skipping numbers
for c in range(2,5,2): #it will skip numbers, only even number will be printed
    print("Even",c)

# For loop in strings
name = "VidhiBansal"
for m in name:
    print(m)

# for loop in list
list = ["A","B","C","End of list"]
for n in list:
    print(n)

#Bailing out of loop
name = "VidhiBansal"
for s in name:
    print(s)
    if s=="h":
        break    #here using the break statement follows the if till condition

name1="Tiyabansal"
for f in name1:
    if f=="b":
        continue
    print(f)

#Nested loop
list=["A","B","C"]
for w in list:
    for y in range(3):
        print(y)
    print(w)