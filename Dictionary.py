#Dictionaries syntax = name{ key:value , key:value , key:value }
people = {
    'vb':'vidhi bansal',  
    'tb': 'tiya bansal',
    'lb': 'lalita bansal',
    'jp':'jaiprakash bansal'
        }   

print(people['vb']) #accessing dictionary data using key value
print(people['lb'])
person = 'jp'
print(people[person]) #we can find a person with the value of key
print(len(people)) #counts the number of items listed in dictionary
print('jp'in people)
print('tb'in people)

#if we want to change data in dictionary we can, it shows dictionaries are not like tuple
people['jp'] = 'Mr. jaiprakash bansal'
print(people)

#Updating dictionary using key value through update() keyword
people.update({'vb': 'vidhhii bansal'})
print(people)
print(people['vb'])

#used for loop for printing all the values
for person in people:
    print(person +" is the key of the value " + people[person])

#copying one value in another variable using copy() keyword
people_cp = people.copy()
print(people_cp)

#deleting any data from dictionary usig del
del people['jp']
print(people)
 
#clearing the full dictionary using clear() keyword
people.clear()
print(people)
print(type(people)) #dictionary type

#poping out/deleting the variables using pop() keyword
people.pop('tb')
print(people)

#we can normally add a dictionary in a dictionary
people = {
    'vb':'vidhi bansal',  
    'tb': 'tiya bansal',
    'lb': 'lalita bansal',
    'jp':'jaiprakash bansal',
    'people_duplicate' : {   'vb':'vidhi bansal',  
    'tb': 'tiya bansal',
    'lb': 'lalita bansal',}
        }
print(people)
print(people['people_duplicate'])
