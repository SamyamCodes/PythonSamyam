birthdays = {"Rachel" : "Aug 9", 
             "Samyam": "Oct 2", 
             "Bob" : "Dec 22",
             "Issac Newton": "Dec 25"}
while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":
        break
    
    if name in birthdays:
        print(f"{birthdays[name]} is the birthday of {name}")
    else:
        print(f"I do not have the birthday information for {name}.")
        print("What is their birthday?")
        bday = input()
        birthdays[name] =  bday
        print("Birthday Database updated!")

