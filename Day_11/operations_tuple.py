countries = ("Nepal", "India", "China", "Australia")
temp = list(countries)
print(type(temp))
temp.append("Japan") #Adding at the last in the list
# temp.pop(3) #Removes the item.
temp[2]= "USA"
countries = tuple(temp)
print(countries)

countries_2  = ("Bangladesh", "Pakistan",  "Srilanka", "Vietnam")
Asia = countries + countries_2
print(Asia)


tuple1 = (1,2,2,1,3,2,4,2,4,3,2,3,3,2,3,2,1,4,1)
res = tuple1.count(2)
print("Count of 2 in touple is", res)
occurence = tuple1.index(3) #Gives the first index of occurence of element 3.
print(occurence)
occurence_slicing = tuple1.index(3, 5,10 ) # 4 is starting, 10 is ending. 3 is the element to be indexed in this range.
print(occurence_slicing)


