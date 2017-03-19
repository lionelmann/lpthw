ten_things = "Apples Oranges Crows Telephone Light Sugar"

print(ten_things)

print("Wait, there are not 10 things in that list. Let's fix that")

stuff = ten_things.split(" ") #split method turns a string into a list
print(stuff)

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
print(more_stuff)

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    print(stuff)
    stuff.append(next_one)
    print("There are {} items in now".format(len(stuff)))

print("There we go: ", stuff)
print()
print("Let's do some stuff with stuff")

print(stuff[1]) #Oranges
print(stuff[-1]) #Corn
print(stuff.pop()) #pops last item off of list
print(stuff.pop()) #pops last item off of list
print()
print(", ".join(stuff)) #.join returns a string which is joined by an element

print("#".join(stuff[3:5]))
