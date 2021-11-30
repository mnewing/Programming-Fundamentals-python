# create a program to collect a dogs name and age.
# calcuate the dogs age in human years using the formula dogs age * 7. 
# display the dogs name and age in human years
# prints messages suggesting what food based on the dogs age, younger than 2 years then puppy food, older than 7 then senior food otherwise standard food
# requires the following skills
#   using variables
#   collecting user input
#   casting data to different types
#   if statments

name = input("dog name")
age = int(input("dog age"))
humanAge = age * 7
print(name + " age " + str(age) + " human age " + str(humanAge))

if age < 2:
    print("Please buy puppy dog food")
elif age > 7:
    print("Please buy senior dog food")
else:
    print("Please buy adult dog food")
