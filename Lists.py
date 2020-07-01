# Lists are an array like data structure in python
# Lists are ordered and changeable === mutable
mylist = []
mylist.append("Sprint")
mylist.append("Don't give up")
mylist.append("Your hard work will pay off")
mylist.append(23)
print(mylist[0])
print(mylist[1])
print(mylist[2])
mylist.append("You can do it")
mylist.append("One step at a time")
print(mylist[-1])
for x in mylist:
    print(x)
# the js equivalent of this would fer(let index in my list)

# Another Array like data structure is the tuple
# Like the List, the Tuple is an ordered collection but a Tuple is uncageable without a workaround

thistuple = ("Kobe", "Michael", "LeBron")
# Once the values have been added to the tuple they are immutable
print(thistuple[0])
print(thistuple[0:3])
# the work around for chaning elements in a tuple is to create a list based on the tuple, change the value you'd like edit and then recreate the tuple using the list you jjust made
thebest = list(thistuple)
thebest[1] = "Kareem"
thistuple = tuple(thebest)
print(thistuple)
#tuples with one value must be followed by a comma or they won't register as a tuple
