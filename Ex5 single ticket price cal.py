# get name and age then display a message with their name and cost of a ticket
# work out the price based on the following rules
#   0 - 5 infant and free
#   5 -12 child and £10
#   13 - 18 teen £20
#   18 - 60 adult £30
#   60 senior £18

name = input("enter your name: ")
age = int(input("enter your age: "))

price = 30
if age < 5:
    price = 0
elif age >= 5 and age < 13:
    price = 10
elif age >= 13 and age < 18 :
    price = 20
elif age > 60:
    price = 18    

print(name + " price £" + str(price))
