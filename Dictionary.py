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