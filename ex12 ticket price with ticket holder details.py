# based on the ticket price calculator code
# add a list which holds details about each ticket holder, name, age, and price for their ticket
# make a function to collect the information about a ticket holder and calculate their ticket price
# allow the user to add as many tickets holders as they need
# once the user is done display the details for the tickets
#
# this would be best done with a 2d list or a list which holds lists


#=================
#possible solution

def getPerson():
    person = ['',0,0]
    person[0] = input("ticket holder's name > ")
    person[1] = int(input("ticket holder's age? "))
    person[2] = calPrice(person[1])
    return person

#work out how much the ticket will cost
#input INT age
#return: price INT
def calPrice(age):
    if age >=4 and age <12:
        return 10
    elif age >=19 and age <59:
        return 25
    elif age <=3:
        return 0
    elif age >=13 and age <=18:
        return 15
    else:
        return 15


persons = []
another = 'y'
while another == 'y':
    persons.append(getPerson())
    another = input('more y > ')

for person in persons:
    print('Ticket for '+person[0]+' will cost £'+str(person[2])+'.')
