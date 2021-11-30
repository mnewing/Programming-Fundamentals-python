# extend the code to calculate a ticket price to ask the user how many tickets
# work out the price per ticket for the number they ask for
# keep a running total of the cost and display at the end


noTickets = int(input("how many tickets do you want: "))

noCal = 0
totalPrice = 0
while noCal < noTickets :
    #work out the price of a single ticket
    age = int(input("enter the age (between 0 and 120) for ticket no " + str(noCal+1) +": "))
    if age < 5:
        print("infant")
        totalPrice = totalPrice + 0
    elif age >= 5 and age <13 :
        print("child")
        totalPrice = totalPrice + 10
    elif age >= 13 and age < 18 :
        print("teen")
        totalPrice = totalPrice + 20
    elif age > 60:
        print("senior")
        totalPrice = totalPrice + 18
    else :
       print("adult")
       totalPrice = totalPrice + 30
    noCal = noCal + 1

print("total price for "+str(noTickets)+" is "+str(totalPrice))
