# My first string
name = "Mrs.Amberlynn Shorrow"
print(name)
print(name[0:13])
print(str(len(name))+"\n")

# My first List
fruit = ["apple","orange","banana"]
print("My list has: ")
for x in fruit:
    if x == 'orange':
        print("grape")
    else:
        print(x)
print("\n")

#Practice String Manipulation
lastName = name[14:21]
print(lastName)
print(str(len(lastName))+"\n")
print(type(lastName))
print("\n")

print(name.count("r"))
print(name.find("A"))
print("\n")

print(lastName.startswith("s"))
print(lastName.endswith("w"))
print(lastName.startswith("h"))
print("\n")
