#Tuples
prices = (25.3, 5.6, 98.4, 47.90)
print(prices.count(5.6)) #count the number of times 
print(prices[1])
# prices[1] = 23.3 #as it is a tuple so it can't be changed
# print(prices[1])
print(prices)
for x in prices:
    print(x)
# in and not in checks the availability of the item in the list
print(5.6 in prices)
print(1.6 not in prices)
print(4.5 in prices)

#Sets
prices = { 29.95 , 4.5 , 1.5, 4.5}
print(prices) #repeated numbers are eliminated
prices.add(20) #can add any item using add() keyword
print(prices)
prices.update([10,25,30]) #can update the full list with another list using update() keyword
print(prices)