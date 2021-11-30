# You are going to write an app that allows a user to design their own smoothie. 
# You will need to offer a series of choices and then and the end show them what they picked.
# use a list to store and display the options to the user
#    ask them to pick their smoothie base, suggested choices: [milk, ice, coconut mik]
#    then allow them to pick a fruit suggested choices: ["apple", "banana", "lime", "ginger", "orange", "blueberry"]
#    then allow them to pick a 2nd fruit or stick with one option
#    then allow them to pick a 2nd fruit or stick with two options
#    display the details of the smoothie they are created.

#start point of the program

#setup our smoothie options
base = ["milk", "ice", "coconut milk"]
fruits = ["apple", "banana", "lime", "ginger", "orange", "blueberry"]

#let them choose their smoothie option
counter = 0
while counter < len(base):
    print(counter, base[counter])
    counter = counter + 1
baseChoice = int(input("please choose your smoothie base "))

#choose their 1st fruit
counter = 0
while counter < len(fruits):
    print(counter, fruits[counter])
    counter = counter + 1
f1Choice = int(input("please choose your fruit "))

#choose the 2nd fruit
counter = 0
while counter < len(fruits):
    print(counter, fruits[counter])
    counter = counter + 1
f2Choice = int(input("please choose your fruit "))

#display final choice
print("Your smoothie is "+base[baseChoice]+" with "+fruits[f1Choice]+" and "+fruits[f2Choice])


