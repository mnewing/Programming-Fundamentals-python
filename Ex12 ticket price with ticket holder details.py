# Ex12 ticket price with ticket holder details.py
# based on the ticket price calculator code
# add a list which holds details about each ticket holder, name, age, and price for their ticket
# make a function to collect the information about a ticket holder and calculate their ticket price
# allow the user to add as many tickets holders as they need
# once the user is done display the details for the tickets
#
# this would be best done with a 2d list or a list which holds lists


#=================
#possible solution

#work out the price of a ticket based on age
#inputs:
#  age - int
#return: price of ticket as an int
def priceCal(age):

    if age > 59:
        #print("Senior price: £18")
        return 18
    elif age < 5 :
        #print("baby price: £0")
        return 0
    elif age > 5 and age < 12 :
        #print("child price: £10")
        return 10
    elif age > 12 and age < 18 :
        #print("teen price: £20")
        return 20
    else:
        #print("adult price: £30")
        return 30
#end priceCal()


#get information for the ticket holder including the price of their ticket
#adds the person information as array to the persons array 
#inputs:
#  none
#return: none
def getPerson():
    person = []
    person.append(input("name please "))
    person.append(int(input("age please ")))
    person.append(priceCal(person[1]))
    persons.append(person)
#end of getPerson()


#Main Body start
persons = []
calTicket = "y"  #user set to anything other than y to stop input loop
totalPrice = 0

#collect user information, keep going as long as say yes`
while calTicket == "Y" or calTicket == "y" or calTicket == "Yes" or calTicket == "yes" :
    getPerson()
    calTicket = input("another ticket (Yes/yes)? ")

#print the details for all ticket holders and calcuate the total cost
for p in persons:
    totalPrice = totalPrice + p[2]
    print("The price for "+p[0]+"'s ticket is £"+str(p[2]))

print("The total pice for your tickets is £"+str(totalPrice))

print(persons)
