# this program will help you get used to using lists
# create a program that creates a list with 2 fruits in in
# add on three more fruits
# use a while loop to allow a user to add some more fruits
# display the whole list, the length of the list and the last item on the list

#==============
#possible solution

#main body
fruits = ["orange","lemon"]
fruits.append("kiwi")
fruits.append("grapes")
fruits.append("bananas")
#add from user input

fruit = input("fruit? ")
while fruit != "n":
    fruits.append(fruit)
    fruit = input("fruit (n to end)? ")

#display the list
print(fruits)
print(len(fruits))
print(fruits[len(fruits)-1])
