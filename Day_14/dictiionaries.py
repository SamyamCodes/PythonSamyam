dic = {
    "Samyam" : "Human Being",
    "Spoon" : "Object"

}
print(dic)

info= {
    242 : "Samyam",
    253 : "Rohan",
    236 : "Vincy"
}
print(info[253])

infor = {
    'name': "Samyam",
    'age' : 16,
    'eligible': True
}
print(infor)
print(infor['name'])
print(infor.get('name'))

# print(infor['name1']) #This throws an error.
print(infor.get('name2')) #This gives only none value. 

print(infor.keys()) # prints all the keys
print(infor.values())

for key in infor.keys():
    print(infor[key])

print(info.items())
for key, value in infor.items():
    print(f"The value corresponding the key {key} is {value}")
    




