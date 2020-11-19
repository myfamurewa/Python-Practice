stringy = "this is a string"
print(stringy * 3)
stringy += "a"
print(stringy)
newOne = "[]"
for char in newOne:
    if char == "[]]mix":
        print("1")
    elif char == "]":
        print("2")

print(newOne.index("["))
last_ind = newOne[::-1].index("]")
print( len(newOne) - (last_ind))
