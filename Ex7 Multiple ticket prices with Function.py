# Builds on the multiple ticket price code calculator
#
# create a function to calculate the cost of a ticket, pass in the age and return the cost
# call the function to calcuate the cost
# ask the user to decide whether to enter an age or finish
# display the final cost when the program has finished


# =================
# Possible Solution

#work out the price of a ticket based on age
#inputs:
#  age - int
#return: price of ticket as an int
def priceCal(age):

    if age > 59:
        print("Senior price: £18")
        return 18
    elif age < 5 :
        print("baby price: £0")
        return 0
    elif age > 5 and age < 12 :
        print("child price: £10")
        return 10
    elif age > 12 and age < 18 :
        print("teen price: £20")
        return 20
    else:
        print("adult price: £30")
        return 30
#end priceCal


#Main Body start
calTicket = "y"  #user set to anything other than y to stop input loop
totalPrice = 0

#ask for an age, keep going as long as say yes`
while calTicket == "Y" or calTicket == "y" or calTicket == "Yes" or calTicket == "yes" :
    age = int(input("age please "))
    totalPrice = totalPrice + priceCal(age)
    calTicket = input("another ticket (Yes/yes)? ")

print("The total pice for you tickets is £"+str(totalPrice))
